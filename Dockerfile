FROM python:3.10-slim

# Установка зависимостей
RUN apt-get update && apt-get install -y build-essential libpq-dev libpango1.0-0 libcairo2 libffi-dev libpangoft2-1.0-0 nodejs npm tree

# Установить рабочий каталог
WORKDIR /app

# Копировать файлы зависимостей в контейнер
COPY requirements.txt .

# Установить зависимости pip
RUN pip install --no-cache-dir -r requirements.txt

# Копировать проект в контейнер
COPY . .

# Переместить рабочий каталог в Emais, где находится package.json
WORKDIR /app/Emais

# Установить зависимости npm и запустить сборку
RUN npm install && npm run build

# Переменная окружения для Django
ENV DJANGO_SETTINGS_MODULE=Emais.settings

# Открыть порт 8000
EXPOSE 8000