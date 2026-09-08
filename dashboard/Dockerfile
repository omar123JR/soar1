# استخدام نسخة بايثون خفيفة
FROM python:3.10-slim

# تحديد مجلد العمل
WORKDIR /app

# نسخ وتثبيت المكتبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات الواجهة
COPY . .

# فتح المنفذ 8501 الخاص بـ Streamlit
EXPOSE 8501

# أمر تشغيل لوحة التحكم
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]