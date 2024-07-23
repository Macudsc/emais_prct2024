# Учебная практика 2024

Задание:
https://joepepper.notion.site/95fb9c02299a44f4ae0d4de5b91498f6

Этапы:
<br>https://docs.google.com/document/d/1si5UakF-CcEoS-tG0aMblcXqsk84lVSfO3nemFR6SYg/edit?usp=sharing

Google диск:
<br>https://drive.google.com/drive/folders/17OyzDhIA2ToxNYw8rofAy9L6uW6cPGqj?usp=sharing

---

## Установка

**YOUR_TG_BOT_TOKEN - ваш токен бота**


**Запуск:**

```
git clone https://github.com/Macudsc/emais_prct2024.git
cd emais_prct2024
echo "tokenn='YOUR_TG_BOT_TOKEN'" >> Emais/sensetiv.py
docker-compose up --build
```
Откройте в браузере адрес 0.0.0.0:8000

**Остановка:** `docker-compose down`

## Бизнес-процессы

Общие:
- авторизация
- просмотр данных о себе
- изменение данных о себе
- выход из системы

Пациент:
- регистрация
- запись на приём
- просмотр медкарты
- скачивание отчёта об исследовании
- удаление записи на приём
- отслеживание оповещений от телеграм-бота

Врач:
- просмотр медкарты на время приёма
- изменение медицинских данных пациента на время приёма
- загрузка данных для отчёта об исследовании
- закрытие приёма

Администратор:
- редактирование информации о пользователях
- удаление пользователей

## Some commands

`pip install -r requirements.txt`

`source venv/bin/activate`

`cd Emais/`

`npm run build`

`python manage.py runserver`

`python manage.py runtelegrambot`

`python manage.py makemigrations`

`python manage.py migrate`