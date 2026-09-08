from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
import requests
import google.generativeai as genai

app = FastAPI(title="SOAR Engine API")

# --- إعدادات Telegram الصحيحة ---
TELEGRAM_BOT_TOKEN = "8944953429:AAEs6vYk0g8RKHJ0rGTLCpf8egUhLPq8b_8"
TELEGRAM_CHAT_ID = "5839164391"

# --- إعدادات الذكاء الاصطناعي ---
GEMINI_API_KEY = "AQ.Ab8RN6LM_exGQ6Pzl9kvE1qrViJ558dkHgwazArFM8c9JY6nQg"
genai.configure(api_key=GEMINI_API_KEY)
ai_model = genai.GenerativeModel('gemini-1.5-flash')

# إعداد قاعدة البيانات المحلية SQLite
SQLALCHEMY_DATABASE_URL = "sqlite:///./soar_logs.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SecurityLog(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(String, default=lambda: datetime.now().isoformat())
    event_type = Column(String)
    source_ip = Column(String)
    severity = Column(Integer)
    asset_criticality = Column(Integer)
    attack_frequency = Column(Integer)
    priority_score = Column(Float)
    is_critical = Column(Boolean, default=False)

Base.metadata.create_all(bind=engine)

class LogEntry(BaseModel):
    event_type: str
    source_ip: str
    severity: int
    asset_criticality: int
    attack_frequency: int

# --- تحديد الـ Playbook ديناميكياً بناءً على نوع الهجوم ---
def get_dynamic_playbook(attack_description: str, ip: str) -> str:
    """
    يُحدد خطوات الاستجابة (Playbook) بناءً على نوع الهجوم المُكتشف.
    يُستخدم كنظام احتياطي ذكي عند فشل الذكاء الاصطناعي،
    أو كسياق إضافي لتحسين جودة رد الـ AI.
    """
    desc = attack_description.upper()

    if "SQL" in desc or "SQLMAP" in desc or "INJECTION" in desc:
        return (
            f"1. عزل خادم قاعدة البيانات مؤقتاً عن الويب.\n"
            f"2. حظر عنوان IP ({ip}) على جدار الـ WAF.\n"
            f"3. مراجعة وتطهير (Sanitize) مدخلات التطبيق."
        )
    elif "BRUTE" in desc or "AUTHENTICATION" in desc or "LOGIN" in desc or "PASSWORD" in desc:
        return (
            f"1. قفل الحساب المستهدف فوراً.\n"
            f"2. حظر عنوان IP ({ip}) عبر جدار الحماية.\n"
            f"3. فرض المصادقة الثنائية (2FA) على الحساب."
        )
    elif "TRAVERSAL" in desc or "DIRECTORY" in desc or "PATH" in desc or "ETC/SHADOW" in desc or "ETC/PASSWD" in desc:
        return (
            f"1. تقييد صلاحيات الوصول للمجلدات (Directory Permissions).\n"
            f"2. حظر عنوان IP ({ip}) على جدار الحماية.\n"
            f"3. تحديث فلاتر الـ WAF لمنع مسارات (../)."
        )
    elif "XSS" in desc or "CROSS-SITE" in desc or "SCRIPT" in desc:
        return (
            f"1. تفعيل Content-Security-Policy على الخادم.\n"
            f"2. حظر عنوان IP ({ip}) عبر الـ WAF.\n"
            f"3. تطهير (Escape) جميع مخرجات HTML في التطبيق."
        )
    elif "MALWARE" in desc or "TROJAN" in desc or "RANSOMWARE" in desc:
        return (
            f"1. عزل الجهاز المصاب عن الشبكة فوراً.\n"
            f"2. تشغيل فحص شامل بمحرك مضاد الفيروسات.\n"
            f"3. أخذ صورة جنائية (Forensic Image) قبل المسح."
        )
    elif "FILE" in desc or "INTEGRITY" in desc or "MODIFIED" in desc or "CHANGED" in desc:
        return (
            f"1. التحقق من مصدر التعديل عبر سجلات التدقيق (Audit Log).\n"
            f"2. مقارنة الملف المعدّل بالنسخة الاحتياطية.\n"
            f"3. استعادة الملف الأصلي إن كان التعديل غير مصرح به."
        )
    else:
        return (
            f"1. عزل النظام المستهدف مؤقتاً.\n"
            f"2. حظر عنوان IP ({ip}) عبر جدار الحماية.\n"
            f"3. إجراء فحص أمني شامل وتوثيق الحادثة."
        )

# دالة توليد توصية الذكاء الاصطناعي (مع نظام Playbook احتياطي ذكي)
def generate_ai_playbook(event_type: str, ip: str) -> str:
    # 1. الحصول على الـ Playbook الديناميكي أولاً (يعمل دائماً أوفلاين)
    dynamic_playbook = get_dynamic_playbook(event_type, ip)

    # 2. محاولة تحسين الرد باستخدام الذكاء الاصطناعي
    try:
        prompt = (f"أنت محلل أمن سيبراني خبير SOC Tier 3. "
                  f"تم رصد هجوم نوعه '{event_type}' من عنوان IP '{ip}'. "
                  f"الخطوات الأولية المقترحة:\n{dynamic_playbook}\n\n"
                  f"حسّن هذه الخطوات واكتب 3 خطوات تقنية حاسمة ومختصرة جداً "
                  f"للاستجابة لهذا الهجوم (Playbook) باللغة العربية. "
                  f"لا تضع مقدمات، ادخل في الخطوات مباشرة.")

        response = ai_model.generate_content(prompt)
        return response.text
    except Exception:
        # 3. في حال فشل الـ AI، يُستخدم الـ Playbook الديناميكي مباشرة
        return dynamic_playbook

# دالة إرسال الإشعار لـ Telegram
def send_telegram_alert(log: LogEntry, score: float):
    if TELEGRAM_BOT_TOKEN == "ضع_التوكن_الخاص_بك_هنا":
        return  # تجاوز الإرسال إذا لم يتم إدخال التوكن بعد

    ai_action = generate_ai_playbook(log.event_type, log.source_ip)
    message = (
        f"🚨 *[SOAR CRITICAL ALERT]* 🚨\n\n"
        f"🔴 *نوع التهديد:* {log.event_type}\n"
        f"🌐 *عنوان المهاجم:* `{log.source_ip}`\n"
        f"📊 *تقييم الخطورة:* `{score:.1f}/100`\n"
        f"⏰ *التوقيت:* {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        f"🤖 *إجراءات الاستجابة المقترحة (AI Playbook):*\n{ai_action}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload, timeout=5)
    except Exception as e:
        print(f"[-] Failed to send Telegram alert: {e}")

# --- مسار مخصص لاستقبال التنبيهات من Wazuh SIEM ---
@app.post("/wazuh-ingest")
def wazuh_ingest(alert: dict):
    # 1. استخراج وصف الهجوم (نوع التهديد) ديناميكياً
    rule_desc = alert.get("rule", {}).get("description", "تنبيه أمني من Wazuh")
    
    # 2. استخراج الـ IP بذكاء (لأن هجمات الملفات لا تحتوي على IP خارجي)
    source_ip = alert.get("data", {}).get("srcip")
    if not source_ip:
        # إذا لم يكن هناك IP، فهذا يعني أن الهجوم داخلي (Local) مثل تغيير ملف
        source_ip = "نظام داخلي (Local System)"
        
    # 3. استخراج مستوى الخطورة الأصلي من Wazuh
    level = alert.get("rule", {}).get("level", 1)
    
    # تحويل مستوى خطورة Wazuh (من 1 إلى 15) إلى تقييم المنظومة (من 0 إلى 100)
    severity_score = int((level / 15.0) * 100)
    
    # إنشاء السجل وتمريره لمحرك الفرز
    log_entry = LogEntry(
        event_type=f"[Wazuh] {rule_desc}",
        source_ip=source_ip,
        severity=severity_score,
        asset_criticality=100,  # سيرفر الشركة (الضحية) يعتبر أصل حساس جداً
        attack_frequency=100
    )
    
    return ingest_log(log_entry)

@app.post("/ingest")
def ingest_log(log: LogEntry):
    score = (log.severity * 0.40) + (log.asset_criticality * 0.40) + (log.attack_frequency * 0.20)
    is_crit = score > 85

    db = SessionLocal()
    new_log = SecurityLog(
        event_type=log.event_type,
        source_ip=log.source_ip,
        severity=log.severity,
        asset_criticality=log.asset_criticality,
        attack_frequency=log.attack_frequency,
        priority_score=score,
        is_critical=is_crit
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    db.close()

    # إطلاق الإنذار الفوري عند تجاوز عتبة الخطورة
    if is_crit:
        send_telegram_alert(log, score)

    return {"status": "success", "priority_score": score, "is_critical": is_crit}

@app.get("/stats")
def get_stats():
    db = SessionLocal()
    total_logs = db.query(SecurityLog).count()
    critical_logs = db.query(SecurityLog).filter(SecurityLog.is_critical == True).count()
    filtered_logs = total_logs - critical_logs
    recent_critical = db.query(SecurityLog).filter(SecurityLog.is_critical == True).order_by(SecurityLog.id.desc()).limit(5).all()
    db.close()

    return {
        "total_logs": total_logs,
        "filtered_logs": filtered_logs,
        "critical_logs": critical_logs,
        "recent_critical": [{"event": r.event_type, "ip": r.source_ip, "score": r.priority_score} for r in recent_critical]
    }