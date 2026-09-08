# استخدام نسخة بايثون خفيفة
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# تشغيل سكربت الهجوم
CMD ["python", "-u", "attacker.py"]