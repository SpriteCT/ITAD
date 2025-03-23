import random
from datetime import datetime
from time import sleep
import os

# Создание папки логов, если её нет
log_dir = "log"
os.makedirs(log_dir, exist_ok=True)

nginx_log_file = os.path.join(log_dir, "nginx.log")

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
statuses = load_weighted_data("data/statuses.txt")  # теперь со взвешенными значениями
referrers = load_weighted_data("data/referrers.txt")  # только рефереры с весами
user_agents = load_data("data/user_agents.txt")

# Назначение user-agent для каждого IP
ip_user_agents = {ip: random.choice(user_agents) for ip in ip_addresses}

# Функция генерации логов для Nginx
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

    # Запись в файл
    with open(nginx_log_file, "a+") as file:
        file.write(log_entry + '\n')

print("Началась генерация логов.")

while True:
    generate_nginx_log()
    sleep(random.uniform(0.1, 2))
