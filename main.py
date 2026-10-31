import sys
import platform
import requests

def main():
    print("=== Запуск через Jenkins ===")
    print(f"Python: {platform.python_version()}")
    print(f"Исполняемый файл: {sys.executable}")

    response = requests.get("https://httpbin.org/status/200", timeout=10)
    print(f"HTTP статус ответа: {response.status_code}")

    if response.status_code == 200:
        print("✅ Скрипт выполнен успешно")
        sys.exit(0)
    else:
        print("❌ Ошибка запроса")
        sys.exit(1)

if __name__ == "__main__":
    main()