# Учебная практика 2024

Задание:
https://joepepper.notion.site/95fb9c02299a44f4ae0d4de5b91498f6

Этапы:
<br>https://docs.google.com/document/d/1si5UakF-CcEoS-tG0aMblcXqsk84lVSfO3nemFR6SYg/edit?usp=sharing

Google диск:
<br>https://drive.google.com/drive/folders/17OyzDhIA2ToxNYw8rofAy9L6uW6cPGqj?usp=sharing

---

## Текущий план

1. Создать роли

2. Реализовать логин, логаут, регистрацию пациента

3. Воспроизвести таблицы из диаграммы сущностей

4. Настроить вид пациента, воспроизвести логику записи ко врачу, медкарты:
    - запись, выбор параметров
    - просмотр медкарты
    - скачивание исследований в разных форматах

5. Настроить вид врача, воспроизвести логику ведения журнала приёма пациентов:
    - приём пациентов
    - записи в медкарту
    - загрузка изображений 
    - завершение приёма

6. Настроить вид администратора, создать логику удаления пользователей, изменения информации

7. Настроить ТГ-бота на отсылку уведомлений

8. ИБ:
    - ограничение попыток входа, таймаут
    - ограничение/защита полей ввода от чрезмерных/некорректных данных
    - ограничение на размер файлов
    - ограничение доступа к неподходящим страницам
    - хранение паролей в БД не в чистом виде

9. Настройка инфраструктуры:
    - Протокол HTTPS

10. Полировака внешнего вида, доработка функционала:
    - комфортный пользовательский опыт
    - тёмная тема


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
