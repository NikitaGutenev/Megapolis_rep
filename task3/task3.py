# Пришло время сделать наработку для интерфейса, который будет взаимодействовать с базой данных. 
# Для этого Вам необходимо написать консольную программу, которая будет запрашивать у Вас имя персонажа, 
# а на выход будет выдавать список игр, в которых встречается этот персонаж(ограничьте количество вывода элементов до 5), 
# если ничего не найдено будет выводить: “Этого персонажа не существует”. 
# Программа должна всегда запрашивать название. 
# Прекратить свою работу она сможет только после ввода “game”.

# Поиск необходимо осуществить с помощью двоичного алгоритма поиска.

# Обратите внимание, что данные в файле не отсортированы! 
# Для сортировки воспользуйтесь встроенными сортировками или напишите собственный алгоритм.

# Формат ответа на запрос пользователя:

# “Персонаж <characters> встречается в играх:

# <Игра 1>

# …

# <Игра 5> 

# и др.”

# Строчка “и др.” должна писать только в случае, если значений больше чем пять.

# Поиск необходимо осуществлять в файле game.txt

# Не забудьте сделать комментарии к коду согласно стандартам документирования кода выбранного языка. 
# После выполнения необходимо сделать локальные и удаленные изменения Вашего репозитория


def binary_search(num: int, lst: [int, int, ...]):
    """Бинарный поиск. Суть алгоритма заключается в сдвиге границ писка (искуственно).
    Если границы слишком узкие, то вывод, что элемента нет."""
    l, r = 0, len(lst)
    m = r//2
    res = None
    while True:
        if lst[m] == num:
            res = m
            break
        elif r - l == 1:
            res = None
            break
        elif lst[m] > num:
            r = m
            m = l + (r-l)//2
        else:
            l = m
            m = l + (r-l)//2
    
    return res


with open('game.txt', 'r', encoding='utf-8') as file:
    data = file.readlines()

data = data[1:]
data.sort()
hashes = {}

# Создание словаря с хешами имен персонажей и самими персонажами со списком игр, где они встречаются
for line in data:
    name, characters, error, date = line.split('$')
    error = error.split(':')
    if not hashes.get(hash(characters), False):
        hashes[hash(characters)] = [characters, [name]]
    else:
        lst = hashes[hash(characters)][1]
        lst.append(name)
        lst = list(set(lst))
        hashes[hash(characters)][1] = lst

# Сортированный список ключей (хешей) для бинарного поиска
list_hashes = sorted(list(hashes.keys()))

while True:
    # Основная программа
    game = input("Введите имя персонажа: ")
    if game == 'game':
        break
    ch_index = binary_search(hash(game), list_hashes)
    if ch_index == None:
        print("Этого персонажа не существует")
        continue

    data = hashes[list_hashes[ch_index]]
    txt = f'Персонаж {data[0]} встречается в играх:\n'
    for i in range(5):
        txt += f'{data[1][i]}\n'
    if len(data[1]) > 5:
        txt += 'и др.'

    print(txt)

print('Конец программы.')