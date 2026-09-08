import time
import random
import subprocess
from datetime import datetime

print("=====================================================")
print(" 🚀 بدء تشغيل المحاكي الذكي (Smart Attack Simulator) 🚀")
print("=====================================================\n")

def generate_ip():
    # توليد عنوان IP وهمي في كل مرة لتبدو الهجمات موزعة جغرافياً
    return f"{random.randint(11, 250)}.{random.randint(1, 254)}.{random.randint(1, 254)}.{random.randint(1, 254)}"

def simulate_ssh_brute_force():
    ip = generate_ip()
    user = random.choice(["root", "admin", "postgres", "ubuntu", "oracle"])
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🔴 هجوم (SSH Brute Force) من IP: {ip} على حساب: {user}")
    
    # توليد عدة محاولات فاشلة متتالية لتفعيل إنذار Wazuh
    for _ in range(8):
        cmd = f'docker exec single-node-wazuh.manager-1 logger -t sshd "Failed password for invalid user {user} from {ip} port 22 ssh2"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.3)

def simulate_sudo_abuse():
    user = random.choice(["www-data", "guest", "test_user"])
    print(f"[{datetime.now().strftime('%H:%M:%S')}] ⚠️ هجوم (Privilege Escalation) محاولة {user} تخطي الصلاحيات")
    
    # محاكاة مستخدم عادي يحاول تشغيل أوامر بصلاحيات Root وفشله
    for _ in range(3):
        cmd = f'docker exec single-node-wazuh.manager-1 logger -t sudo "pam_unix(sudo:auth): authentication failure; logname= uid=1000 euid=0 tty=/dev/pts/1 ruser={user} rhost=  user=root"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.5)

def simulate_ssh_success_anomalous():
    ip = generate_ip()
    user = "root"
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🚨 هجوم (Anomalous Login) تسجيل دخول ناجح ومريب من IP: {ip}")
    
    # محاكاة نجاح مخترق في الدخول من عنوان غريب
    cmd = f'docker exec single-node-wazuh.manager-1 logger -t sshd "Accepted password for {user} from {ip} port 22 ssh2"'
    subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

while True:
    # اختيار هجوم عشوائي من القائمة
    attacks = [simulate_ssh_brute_force, simulate_sudo_abuse, simulate_ssh_success_anomalous, simulate_ssh_brute_force]
    attack = random.choice(attacks)
    attack()
    
    # الانتظار لوقت عشوائي (من 15 إلى 45 ثانية) لكي تبدو الرسوم البيانية طبيعية وغير مصطنعة
    sleep_time = random.randint(15, 45)
    print(f"⏳ انتظار {sleep_time} ثانية قبل الهجوم التالي...\n")
    time.sleep(sleep_time)