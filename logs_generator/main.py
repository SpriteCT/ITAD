import random
from datetime import datetime
from time import sleep
import os

# Создание папки, если её нет
log_dir = "log"
log_file = os.path.join(log_dir, "nginx.log")
os.makedirs(log_dir, exist_ok=True)

# Функция генерации случайного IP-адреса
def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Варианты HTTP-методов, URL и кодов состояния
methods = ["GET", "POST", "DELETE", "PUT"]
urls = ["/", "/index.html", "/login", "/api/data", "/api/user/123", "/images/logo.png", "/api/logout", "/profile"]
statuses = [200, 201, 301, 302, 400, 401, 403, 404, 500]
referrers = ["http://example.com/", "http://example.com/home", "http://example.com/login", "http://example.com/profile", "-"]
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Pixel 6) Chrome/120.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/115.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 Safari/537.36"
]

print("Началась генерация логов.")

try:
    while True:
        log_time = datetime.now()
        log_entry = (
            f"{random_ip()} - - [{log_time.strftime('%d/%b/%Y:%H:%M:%S +0300')}] "
            f"\"{random.choice(methods)} {random.choice(urls)} HTTP/1.1\" {random.choice(statuses)} {random.randint(100, 5000)} "
            f"\"{random.choice(referrers)}\" \"{random.choice(user_agents)}\""
        )

        # Запись в файл
        with open(log_file, "a+") as file:
            file.write(log_entry + '\n')

        # Случайная задержка от 0.1 до 5 секунд
        sleep(random.uniform(1, 10))

except KeyboardInterrupt:
    print("\nГенерация логов остановлена.")
