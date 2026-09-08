import socket
import time
from datetime import datetime
import requests

WAZUH_IP = "127.0.0.1" # المنفذ المربوط بجهازك
WAZUH_PORT = 514

def send_log(ip, request, user_agent, status="200"):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    time_str_apache = datetime.now().strftime('%d/%b/%Y:%H:%M:%S +0000')
    time_str_syslog = datetime.now().strftime('%b %d %H:%M:%S')
    
    # محاكاة سجلات خادم أباتشي (Apache) الحقيقية
    apache_log = f'{ip} - - [{time_str_apache}] "{request}" {status} 1234 "-" "{user_agent}"'
    syslog_msg = f"<34>{time_str_syslog} wordpress-server apache2: {apache_log}"
    
    sock.sendto(syslog_msg.encode('utf-8'), (WAZUH_IP, WAZUH_PORT))
    sock.close()

print("🚀 [SOAR Presentation] Starting Attack Simulator...\n")

# 1. هجوم متوسط: مسح أمني للبحث عن الثغرات (Vulnerability Scan)
print("[*] 1. Executing Vulnerability Scan (Nikto)...")
try: requests.get("http://localhost:8084/") 
except: pass
send_log("103.45.67.89", "GET / HTTP/1.1", "Nikto/2.1.6")
time.sleep(3)

# 2. هجوم عالي: اختراق مسارات النظام (Directory Traversal)
print("[*] 2. Executing Directory Traversal Attack...")
try: requests.get("http://localhost:8084/../../../../etc/passwd") 
except: pass
send_log("103.45.67.90", "GET /../../../../etc/passwd HTTP/1.1", "Mozilla/5.0")
time.sleep(3)

# 3. هجوم حرج جداً: حقن قواعد البيانات (SQL Injection)
print("[*] 3. Executing SQL Injection (SQLmap)...")
try: requests.get("http://localhost:8084/?id=1+UNION+SELECT+password+FROM+users") 
except: pass
send_log("103.45.67.91", "GET /?id=1+UNION+SELECT+password+FROM+users HTTP/1.1", "sqlmap/1.5")

print("\n✅ All attacks deployed! Check Wazuh Dashboard and Telegram.")