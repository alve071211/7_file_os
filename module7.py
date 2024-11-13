import os
import time

directory = (r'D:\PitonHProjects\pythonProject30082024\venv\модуль7')

for root, dirs, files in os.walk(directory):
  for file in files:
    filepath = os.path.join(directory)
    filetime = os.path.getmtime(directory)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    print(formatted_time)
    filesize = os.path.getsize(directory)
    parent_dir = os.path.dirname(directory)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')