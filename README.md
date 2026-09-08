<div align="center">

# 🛡️ Smart SOAR System
**Enterprise-Grade Security Orchestration, Automation, and Response**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![FastAPI](https://img.shields.io/badge/FastAPI-High_Performance-009688.svg?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-007ACC.svg?style=for-the-badge&logo=wazuh&logoColor=white)](https://wazuh.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Gemini](https://img.shields.io/badge/Gemini_AI-Smart_Playbooks-8E75B2.svg?style=for-the-badge&logo=google-bard&logoColor=white)](https://deepmind.google/technologies/gemini/)

*نظام ذكي متكامل بمرونة عالية (High Availability) للقضاء على الإرهاق من التنبيهات الأمنية (Alert Fatigue).*

</div>

---

## 📖 سيناريو المشكلة والحل
**تخيل هذا الموقف:** فريق أمني في مؤسسة كبرى تصله يومياً آلاف التنبيهات المزعجة (أخطاء كتابة كلمة المرور، مسح شبكي عشوائي، إلخ). وسط هذه الضوضاء الهائلة، يقوم هاكر حقيقي بتسريب بيانات حساسة، لكن الفريق لم يلاحظ ذلك إلا بعد فوات الأوان بسبب "الإرهاق من التنبيهات" (Alert Fatigue).

**الحل:** هنا يتدخل نظام (Smart SOAR). يقوم النظام باستلام كافة التنبيهات، وبشكل آلي وذكي يقوم بفلترة واستبعاد "الضوضاء" بصمت. وعندما يرصد هجوماً حقيقياً، لا يكتفي بإطلاق إنذار، بل يستعين بالذكاء الاصطناعي (AI) لتوليد خطة استجابة فورية (Playbook) ويرسلها لفريق الأمن أينما كانوا عبر Telegram، وكل هذا في بنية تحتية مقاومة للانهيار (Zero Downtime).

---

## 📑 جدول المحتويات
- [📖 سيناريو المشكلة والحل](#-سيناريو-المشكلة-والحل)
- [🏗️ المعمارية التقنية (Architecture Diagram)](#-المعمارية-التقنية-architecture-diagram)
- [⚙️ التقنيات المستخدمة](#-التقنيات-المستخدمة-technologies)
- [📂 هيكلية المشروع (Project Structure)](#-هيكلية-المشروع-project-structure)
- [⚔️ محاكاة الهجمات (Attack Scenarios)](#-محاكاة-الهجمات-attack-scenarios)
- [🛠️ كيفية التشغيل](#-كيفية-التشغيل)

---

## 🏗️ المعمارية التقنية (Architecture Diagram)

توضح الخريطة التالية كيف تتنقل البيانات بسلاسة من مصدرها حتى تصل للمحلل الأمني، مع ضمان عدم توقف الخدمة:

```mermaid
graph TD
    A[Wazuh SIEM\nيكتشف الهجمات ويرسل التنبيهات] -->|Webhook| B(Nginx Load Balancer\nموزع الأحمال)
    B -->|Round-Robin| C{SOAR Backend 1\nمحرك المعالجة}
    B -->|Round-Robin| D{SOAR Backend 2\nمحرك المعالجة}
    
    C --> E((Gemini AI\nتحليل الهجوم))
    D --> E
    
    C --> F[Telegram Bot\nإرسال الإنذار و الـ Playbook]
    D --> F
    
    C --> G[(Database / Streamlit\nحفظ التنبيهات وعرضها)]
    D --> G
    
    H[Uptime Kuma] -.->|مراقبة مستمرة| B
    H -.->|مراقبة مستمرة| C
    H -.->|مراقبة مستمرة| D
```

يعتمد النظام بالكامل على حاويات (Docker) ويدمج أحدث التقنيات:
- 🛡️ **Wazuh**: نظام (SIEM) لجمع السجلات واكتشاف التهديدات الحرجة عبر قواعد مخصصة.
- 🔀 **Nginx**: موزع أحمال (Load Balancer) يستخدم خوارزمية Round-Robin لضمان التوافرية.
- ⚡ **FastAPI**: محرك المعالجة المزدوج (SOAR Engine) لتقييم المخاطر وتحديد الاستجابة.
- 📊 **Streamlit**: لوحة قيادة تفاعلية واحترافية لمحللي الأمن.
- 🩺 **Uptime Kuma**: نظام استشعار لمراقبة صحة النظام وحالة الحاويات في الوقت الفعلي.

---

## ⚙️ التقنيات المستخدمة (Technologies)
<div align="center">

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
  ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
  ![Wazuh](https://img.shields.io/badge/Wazuh-007ACC?style=for-the-badge&logo=wazuh&logoColor=white)
  ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
  ![Gemini AI](https://img.shields.io/badge/Gemini%20AI-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)
  ![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
  ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
  ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 📂 هيكلية المشروع (Project Structure)

```text
SOAR_Project/
├── docker-compose.yml       # ملف بناء وتشغيل كافة الحاويات
├── ossec.conf               # إعدادات Wazuh (مربوطة بالحاوية)
├── custom_soar_rules.xml    # قواعد اكتشاف الهجمات المخصصة
├── attack_demo.py           # سكربت لمحاكاة الهجمات آلياً
├── custom_web_attacks.log   # ملف السجلات الوهمي لحقن الهجمات
│
├── engine/                  # محرك المعالجة (SOAR)
│   ├── Dockerfile
│   ├── main.py              # كود FastAPI للتعامل مع التنبيهات و Gemini
│   └── requirements.txt
│
├── dashboard/               # واجهة المستخدم (Streamlit)
│   ├── Dockerfile
│   ├── app.py               # كود بناء اللوحة وعرض الإحصائيات
│   └── requirements.txt
│
├── nginx/                   # موزع الأحمال
│   └── nginx.conf           # إعدادات توجيه البيانات للحاويات
│
└── images/                  # صور التوثيق للمشروع
```

---

## ⚔️ محاكاة الهجمات (Attack Scenarios)

لإثبات قوة النظام، تم تنفيذ 3 هجمات فعلية لمحاكاة الواقع. 
**ملاحظة:** يتم إدخال أوامر الهجوم من داخل قلب نظام Wazuh لتجنب أي مشاكل متعلقة بنظام المضيف (Windows) عبر الأمر التالي:
```bash
docker exec -it single-node-wazuh.manager-1 bash
```

### 🟢 الهجمة الأولى: اختبار الفلترة وتقليل الضوضاء (Noise Reduction)
يحاكي هذا الأمر خطأً عادياً ومزعجاً في تسجيل الدخول (401 Unauthorized) تتعرض له السيرفرات طوال الوقت:
```bash
echo "192.168.1.50 - - [$(date +'%d/%b/%Y:%H:%M:%S %z')] \"GET /login HTTP/1.1\" 401 200 \"-\" \"Mozilla/5.0\"" >> /var/log/custom_web_attacks.log
```
**🎯 ماذا يثبت هذا الاختبار؟**
الهدف هو إثبات ذكاء المنظومة. النظام التقط الحدث بنجاح عبر Wazuh، لكن خوارزمية الفرز في الـ SOAR صنفته كتهديد منخفض، فتم استبعاده بصمت ووضعه في خانة التنبيهات "المفلترة" في الـ Dashboard دون إرسال إشعارات مزعجة للمحلل الأمني على تيليجرام (لا يوجد Alert Fatigue).

<details>
<summary><b>📸 صور الهجمة الأولى (اضغط للعرض)</b></summary>
<div align="center">
  <br><b>اكتشاف Wazuh للحدث الروتيني:</b><br>
  <img src="images/وازو الهجوم1.png" width="800"/>
  <br><br><b>شاشة Streamlit تُظهر استبعاد التنبيه للضوضاء:</b><br>
  <img src="images/داشبورد الهجوم رقم1 .png" width="800"/>
</div>
</details>

---

### 🔴 الهجمة الثانية: اكتشاف التهديد الحرج (SQLMap Detection)
يحاكي هذا الأمر محاولة اختراق خطيرة وحقيقية لقواعد البيانات باستخدام أداة SQLMap:
```bash
echo "192.168.1.100 - - [$(date +'%d/%b/%Y:%H:%M:%S %z')] \"GET /index.php?id=1%20OR%201=1 HTTP/1.1\" 200 450 \"-\" \"sqlmap/1.5\"" >> /var/log/custom_web_attacks.log
```
**🎯 ماذا يثبت هذا الاختبار؟**
الهدف إثبات سرعة الاستجابة اللحظية. التقط Wazuh الهجوم وصنفه كتهديد حرج (Level 12). أرسل الـ SOAR التنبيه فوراً لتيليجرام. والأهم من ذلك، أدرك **الذكاء الاصطناعي** أنه هجوم قواعد بيانات (SQL Injection)، فاقترح Playbook مخصصاً يعطي أوامر لعزل قواعد البيانات تحديداً.

<details>
<summary><b>📸 صور الهجمة الثانية (اضغط للعرض)</b></summary>
<div align="center">
  <br><b>اكتشاف Wazuh للهجوم الخطير المستوى 12:</b><br>
  <img src="images/وازو الهجوم2.png" width="800"/>
  <br><br><b>شاشة Streamlit تُظهر تصنيف الحدث كتهديد حرج:</b><br>
  <img src="images/داشبورد الهجوم2.png" width="800"/>
  <br><br><b>رسالة تليجرام الفورية تحتوي الـ AI Playbook لعزل قواعد البيانات:</b><br>
  <img src="images/تلقرام الهجوم2.png" width="400"/>
</div>
</details>

---

### 🔥 الهجمة الثالثة: اختبار الفوضى (Chaos Test & High Availability)
هذا الاختبار مصمم لإثبات استمرارية عمل النظام تحت أسوأ الظروف (Zero Downtime).

**الخطوة الأولى: إسقاط النظام الرئيسي** (محاكاة انهيار الخادم تحت الضغط)
يتم تنفيذ هذا الأمر من نافذة الطرفية للمضيف:
```bash
docker stop soar_backend_1
```
**الخطوة الثانية: إطلاق الهجوم أثناء الانهيار** (من داخل حاوية Wazuh)
يحاكي هجوم استكشاف المسارات وسرقة الملفات السرية (Path Traversal):
```bash
echo "10.10.5.55 - - [$(date +'%d/%b/%Y:%H:%M:%S %z')] \"GET /../../../../etc/passwd HTTP/1.1\" 200 150 \"-\" \"curl/7.68.0\"" >> /var/log/custom_web_attacks.log
```
**🎯 ماذا يثبت هذا الاختبار؟**
رغم أن الخادم الرئيسي للـ SOAR (ميت)، إلا أن موزع الأحمال (Nginx) أدرك ذلك وحوّل الهجوم فوراً للخادم الاحتياطي. تمت معالجة الهجمة، ووصلتني رسالة التهديد بنجاح على تيليجرام. وجاء بـ Playbook مختلف تماماً يركز على مراجعة صلاحيات المجلدات (لأن الهجمة مختلفة).

<details>
<summary><b>📸 صور الهجمة الثالثة (اضغط للعرض)</b></summary>
<div align="center">
  <br><b>اكتشاف Wazuh لسرقة الملفات:</b><br>
  <img src="images/وازو الهجوم 3.png" width="800"/>
  <br><br><b>رسالة تليجرام رغم توقف الخادم، وتحتوي Playbook مختلف:</b><br>
  <img src="images/تلقرام الهجمة 3.png" width="400"/>
</div>
</details>

---

## 🛠️ كيفية التشغيل
```bash
# بناء وتشغيل الحاويات في الخلفية
docker compose up -d --build
```
<div align="center">
<b>تم بناء هذا المشروع بشغف لرفع مستوى الأمان وسرعة الاستجابة في المؤسسات.</b>
</div>
