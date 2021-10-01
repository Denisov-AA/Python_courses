import os
import time

path_life_time = 120
file_life_time = 60
working_dir = os.getcwd()
monitoring_dir = "\\Test_dir"
try:
    os.mkdir(working_dir + monitoring_dir)
except FileExistsError:
    print("Directory already exists")
while True:
    files = os.walk(working_dir + monitoring_dir)                      # Смотрим папку - получаем генератор кортежей
    path_list = []
    files_list = []
    for directory in files:                                            # Крутим генертор
        path_list.append(directory[0])                                 # Записываем директории
        files_list.append(directory[2])                                # Записываем списки файлов в каждой директории

    for path in path_list:                                             # Крутим директории
        if int(time.time() - os.path.getctime(path)) > path_life_time: # Проверяем время жизни директории
            try:
                os.rmdir(path)                                         # Удаляем, если время превышено
            except OSError:
                pass                                                   # Если папка не пустая - она не удалится
        for files in files_list:                                       # Крутим списки файлов
            for file in files:                                         # Далее будет очень много exceptions
                try:                                                   # это не очень хорошо
                    try_path = path + "\\" + file
                    os.remove(try_path)
                except FileNotFoundError:
                    pass





