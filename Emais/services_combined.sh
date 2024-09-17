#!/bin/bash

# Web
python manage.py runserver 0.0.0.0:8000 &

# Bot
python manage.py runtelegrambot &
# Ждем пока ПРОЦЕССЫ завершатся
wait -n
# Если упал хоть один, то проект падает
exit $?