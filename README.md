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

## 📑 جدول المحتويات
- [🚀 نبذة عن المشروع](#-نبذة-عن-المشروع)
- [✨ المميزات الرئيسية](#-المميزات-الرئيسية)
- [🏗️ المعمارية التقنية](#-المعمارية-التقنية-system-architecture)
- [📸 معرض الصور](#-معرض-الصور-screenshots)
- [🛠️ كيفية التشغيل](#-كيفية-التشغيل)

---

## 🚀 نبذة عن المشروع
يهدف هذا المشروع إلى إحداث ثورة في كيفية تعامل مراكز العمليات الأمنية (SOC) مع الهجمات المتزايدة. يقوم النظام بأتمتة عملية الفرز (Triage)، وتصفية التنبيهات المزعجة (Noise)، وتوليد مسارات استجابة ديناميكية (Playbooks) باستخدام **الذكاء الاصطناعي (Gemini AI)**. 
تم تصميم النظام ليعمل في البيئات الحساسة عبر تطبيق مبادئ (Enterprise-Grade) وتوفير بنية تحتية لا تتوقف (Zero Downtime).

---

## ✨ المميزات الرئيسية
- 🎯 **تقليل الضوضاء (Noise Reduction):** تصفية التنبيهات الروتينية بصمت وتوفير وقت المحلل.
- 🧠 **استجابة ديناميكية (AI Playbooks):** توليد خطط استجابة مخصصة عبر الذكاء الاصطناعي لكل هجوم.
- 🔄 **مرونة عالية (High Availability):** معمارية تضمن استمرار العمل حتى عند انهيار أحد الخوادم المركزية.
- 📩 **تنبيهات فورية:** تكامل كامل مع **Telegram** لإيصال التنبيهات الحرجة للفريق أينما كانوا.

---

## 🏗️ المعمارية التقنية (System Architecture)
يعتمد النظام بالكامل على حاويات (Docker) ويدمج أحدث التقنيات:

| التقنية | الوصف |
|---------|-------|
| 🛡️ **Wazuh** | نظام (SIEM) لجمع السجلات واكتشاف التهديدات الحرجة عبر قواعد مخصصة. |
| 🔀 **Nginx** | موزع أحمال (Load Balancer) يستخدم خوارزمية Round-Robin لضمان التوافرية. |
| ⚡ **FastAPI** | محرك المعالجة المزدوج (SOAR Engine) لتقييم المخاطر وتحديد الاستجابة. |
| 📊 **Streamlit** | لوحة قيادة تفاعلية واحترافية لمحللي الأمن. |
| 🩺 **Uptime Kuma** | نظام استشعار لمراقبة صحة النظام وحالة الحاويات في الوقت الفعلي. |

---

## 📸 معرض الصور (Screenshots)

<details>
<summary><b>1. شاشة اكتشاف التهديدات (Wazuh Dashboard)</b></summary>
<br>
تُظهر التقاط التهديدات الحرجة وتصنيفها في المستوى 12.

<div align="center">
  <img src="images/wazuh.png" alt="Wazuh Dashboard" width="800"/>
</div>
</details>

<details>
<summary><b>2. لوحة قيادة العمليات الأمنية (Streamlit SOC Dashboard)</b></summary>
<br>
توضح التنبيهات المستلمة، المفلترة (تقليل الضوضاء)، والتنبيهات الحرجة مع درجات الخطورة.

<div align="center">
  <img src="images/streamlit.png" alt="Streamlit Dashboard" width="800"/>
</div>
</details>

<details>
<summary><b>3. اختبار التوافرية العالية (Uptime Kuma - Chaos Test)</b></summary>
<br>
<b>الحالة الأولى (استقرار النظام):</b> الحاوية `soar_backend_1` تعمل بشكل طبيعي.

<div align="center">
  <img src="images/uptime_up.png" alt="Uptime Kuma - Up" width="800"/>
</div>

<b>الحالة الثانية (انهيار محاكى):</b> إيقاف الحاوية عمداً، حيث يقوم Nginx بتحويل التنبيهات للحاوية الثانية بسلاسة.

<div align="center">
  <img src="images/uptime_down.png" alt="Uptime Kuma - Down" width="800"/>
</div>
</details>

<details>
<summary><b>4. إشعارات الاستجابة الذكية (Telegram AI Playbooks)</b></summary>
<br>
الإشعارات اللحظية الواصلة للمحلل وتوضح أدلة الاستجابة المارنة المعتمدة على الذكاء الاصطناعي.

<div align="center">
  <img src="images/telegram.png" alt="Telegram Alerts" width="800"/>
</div>
</details>

---

## 🛠️ كيفية التشغيل

1. **نسخ المستودع:**
   ```bash
   git clone https://github.com/omar123JR/soar1.git
   cd soar1
   ```

2. **تشغيل بيئة العمل عبر Docker:**
   ```bash
   docker compose up -d --build
   ```

3. **الوصول للخدمات:**
   - Wazuh Dashboard: `https://localhost`
   - SOAR Dashboard: `http://localhost:8501`
   - Uptime Kuma: `http://localhost:3001`

---
<div align="center">
<b>تم بناء هذا المشروع بشغف لرفع مستوى الأمان وسرعة الاستجابة في المؤسسات.</b>
</div>
