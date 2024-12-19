#!/bin/bash

# Генерация config.py с переменными окружения
cat <<EOF > /app/config.py
import os

DB_USER = "${DB_USER}"
DB_PASS = "${DB_PASS}"
DB_HOST = "${DB_HOST}"
DB_PORT = "${DB_PORT}"
DB_NAME = "${DB_NAME}"
BOT_TOKEN = "${BOT_TOKEN}"

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
EOF

echo "config.py создан с данными для подключения к БД."
chmod +rw config.py
# Запуск основного приложения
exec python bot.py
