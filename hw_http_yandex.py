import yadisk
import os
from datetime import datetime

TOKEN = ''
y = yadisk.YaDisk(token=TOKEN)

date = datetime.strftime(datetime.now(), "%d.%m.%Y-%H.%M.%S")
y.mkdir(f'/test/{date}')

folder = []
for i in os.walk('C:\\folder'):
    folder.append(i)
for address, dirs, files in folder:
    for dir in dirs:
        y.mkdir(f'/test/{date}/{dir}')
        print(f'Папка {dir} создана.')
    for file in files:
        print(f'Файл {file} загружен.')
        y.upload(f'{address}/{file}', f'/test/{date}/{file}')

