import random
from datetime import datetime
from time import sleep
import os

# Создание папки логов, если её нет
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

nginx_log_file = os.path.join(log_dir, "nginx.log")
else_log_file = os.path.join(log_dir, "else.log")

# Функция загрузки обычных данных из файла
def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]

# Функция загрузки данных с весами
def load_weighted_data(filename):
    weighted_data = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2 and parts[1].isdigit():
                value, weight = parts[0], int(parts[1])
                weighted_data.extend([value] * weight)
    return weighted_data

# Загрузка данных из файлов
ip_addresses = load_data("data/ip_addresses.txt")
methods = load_data("data/methods.txt")
urls = load_weighted_data("data/urls.txt")
statuses = load_weighted_data("data/statuses.txt") 
referrers = load_weighted_data("data/referrers.txt") 
user_agents = load_data("data/user_agents.txt")
users = load_data("data/users.txt")

# Назначение user-agent для каждого IP
ip_user_agents = {ip: random.choice(user_agents) for ip in ip_addresses}

# Функция генерации логов "Nginx"
# Формат логов 
# 191.69.181.26 - - [24/Mar/2025:12:03:47 +0300] "GET / HTTP/1.1" 200 1405 "https://example.com/product/456" "Mozilla/5.0 (Linux; Linux i676 ) Gecko/20100101 Firefox/72.2"
def generate_nginx_log():
    ip = random.choice(ip_addresses)
    next_url = random.choice(urls)
    user_agent = ip_user_agents[ip]
    referrer = random.choice(referrers)
    status = random.choice(statuses)

    log_time = datetime.now()
    log_entry = (
        f"{ip} - - [{log_time.strftime('%d/%b/%Y:%H:%M:%S +0300')}] "
        f"\"{random.choice(methods)} {next_url} HTTP/1.1\" {status} {random.randint(100, 5000)} "
        f"\"{referrer}\" \"{user_agent}\""
    )

    with open(nginx_log_file, "a+") as file:
        file.write(log_entry + '\n')

# Формат лога
# [192.168.1.10] [user123] [2025/03/24 14:25:10] ["GET /dashboard HTTP/1.1"] [200] [4521] ["https://example.com/home"] ["session=xyz789"] [exec_time=0.237s] [request_id=abc-def-123]
def generate_else_log():
    ip = random.choice(ip_addresses)
    user = random.choice(users)
    log_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    method = random.choice(methods)
    url = random.choice(urls)
    status = random.choice(statuses)
    response_size = random.randint(100, 5000)
    referrer = random.choice(referrers)
    session_id = f"session={random.randint(100000, 999999)}"
    exec_time = f"exec_time={round(random.uniform(0.1, 1.5), 3)}s"
    request_id = f"request_id={random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}"

    log_entry = (
        f"[{ip}] [{user}] [{log_time}] [\"{method} {url} HTTP/1.1\"] "
        f"[{status}] [{response_size}] [\"{referrer}\"] [\"{session_id}\"] "
        f"[{exec_time}] [{request_id}]"
    )
    
    else_log_file = os.path.join(log_dir, "else.log")
    with open(else_log_file, "a+") as file:
        file.write(log_entry + '\n')

for i in range(10000):
    sleep(random.uniform(0.1, 0.5))
    generate_nginx_log()
    generate_else_log()
