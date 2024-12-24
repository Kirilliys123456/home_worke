import os, time
from os.path import join, getmtime, getsize, dirname
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file)     # 2
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)    # 4 # Исправлено !!!
        parent_dir_ = os.path.dirname(os.path.abspath(filepath))     # полный путь родительского каталога
        parent_dir = os.path.dirname(filepath)  # 5 # Исправлено !!! # относительный путь
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
