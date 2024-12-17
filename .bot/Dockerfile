FROM python:3.10-slim

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ARG HF_TOKEN
RUN huggingface-cli login --token $HF_TOKEN

# Копируем код приложения
COPY . .

# Создаём entrypoint для генерации config.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Запуск через entrypoint
ENTRYPOINT ["/entrypoint.sh"]