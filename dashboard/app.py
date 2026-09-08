import streamlit as st
import requests
import pandas as pd
import time

# إعدادات الصفحة
st.set_page_config(page_title="SOAR Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ منظومة الفرز الذكي للتنبيهات الأمنية (SOAR)")
st.markdown("---")

# الرابط الخاص بموزع الحمل (Nginx) - يوجه الطلبات بين soar_backend_1 و soar_backend_2
API_URL = "http://soar_nginx_proxy:8080/api/stats"

# دالة لجلب البيانات من المحرك
def fetch_stats():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
    except Exception as e:
        return None

data = fetch_stats()

if data:
    # تقسيم الشاشة إلى 3 أعمدة لعرض المؤشرات
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.info(f"📥 إجمالي التنبيهات المستلمة\n### {data['total_logs']}")
    
    with col2:
        st.success(f"🛡️ التنبيهات المفلترة (تم استبعادها)\n### {data['filtered_logs']}")
        
    with col3:
        if data['critical_logs'] > 0:
            st.error(f"🚨 التنبيهات الحرجة\n### {data['critical_logs']}")
        else:
            st.warning(f"🚨 التنبيهات الحرجة\n### 0")

    st.markdown("### 📋 أحدث التهديدات الحرجة")
    if data['recent_critical']:
        # تحويل البيانات إلى جدول مرتب
        df = pd.DataFrame(data['recent_critical'])
        df.columns = ["نوع الحدث", "عنوان IP", "درجة الخطورة"]
        st.table(df)
    else:
        st.success("الأنظمة آمنة.. لا توجد تهديدات حرجة حالياً.")
        
else:
    st.error("⚠️ لا يمكن الاتصال بمحرك الفرز (Backend). جاري المحاولة...")

# تحديث تلقائي للصفحة كل 3 ثوانٍ
time.sleep(3)
st.rerun()