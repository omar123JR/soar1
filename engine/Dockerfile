# استخدام نسخة بايثون خفيفة ورسمية
FROM python:3.10-slim

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ ملف المكتبات وتثبيتها
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY . .

# فتح المنفذ 8000 لكي يتواصل معه باقي النظام
EXPOSE 8000

# أمر التشغيل الأساسي للمحرك
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]