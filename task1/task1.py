# Задача 1

# Первая задача, которая стоит перед вами это найти все ошибки с содержанием числа 55, 
# тк это особо важные и опасные ошибки. 
# Для этого составьте отчет в формате: 
# “У персонажа\t<characters>\tв игре\t<GameName>\tнашлась ошибка с кодом:\t <nameError>.\tДата фиксации:\t <date>”. 
# После предоставления отчета измените значение ошибки на “Done”, 
# а в поле дата поставьте “0000-00-00”  и полученные измененные данные сохраните в файле game_new.csv 
# (загрузите файл в поле ответа).

# В задаче запрещено использование сторонних библиотек(Pandas и др)

# Не забудьте сделать комментарии к коду согласно стандартам документировани я кода выбранного языка 
# (для языка Python – PEP 257). 
# После выполнения необходимо сделать локальные и удаленные изменения Вашего репозитория.

import csv


with open('game.txt', 'r', encoding='utf-8') as file:
    new_file = []
    fl = False
    for line in file.readlines():
        name, characters, error, date = line.split('$')
        if fl:
            error = error.split(':')
            if error[1] == '55':
                text = f'У персонажа\t{characters}\tв игре\t{name}\tнашлась ошибка с кодом:\t {":".join(error)}.\tДата фиксации:\t {date}'
                with open('./task1/otchet.txt', 'a', encoding='utf-8') as ot:
                    ot.write(f'{text}')
                new_file.append([name, characters, 'Done', '0000-00-00'])
            else:
                new_file.append([name, characters, ":".join(error), date])
        else:
            new_file.append([name, characters, error, date])
            fl = True
    
with open('./task1/game_new.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='$', lineterminator='\r')
    writer.writerows(new_file)