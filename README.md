# telegram-auto-reply
Telegram auto replier bot

Бот-автоответчик отвечает заданным текстом на все сообщения, делая их прочитанными

# Установка и использование

1. Склонировать репозиторий
2. Зайти сюда (https://core.telegram.org/api/obtaining_api_id) и получить API_ID и API_HASH
3. Добавить полученные TELEGRAM_API_ID и TELEGRAM_API_HASH в .env файл, пример есть в .env.sample
5. При первом запуске потребует ввод телефона и кода активации, при последующих требовать не будет и можно будет запускать в фоне

# Запуск

**Запуск через докер**

Первый запуск - docker-compose run telegram-auto-replier

Потом можно - docker-compose up -d

**Запуск без докера**

Установить требуемые пакеты - pip install --no-cache-dir -r requirements.txt

Запуск - python3 autoreplier.py
