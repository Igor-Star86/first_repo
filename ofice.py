documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(numbers):
    for doc_numbers in documents:
        if doc_numbers["number"] == numbers:
            print(doc_numbers["name"])
            break
    else:
        print('Такого номера документа нет в базе.')


def people_list():
    for persons in documents:
        print(persons['type'], '"' + persons['number'] +
              '"', '"' + persons['name'] + '"')


def shelf(numbers):
    break_marker = False
    for shelf_directories in directories.items():
        for doc_numbers in shelf_directories[1]:
            if doc_numbers == numbers:
                print('Данный документ должен лежать на полке',
                      shelf_directories[0])
                break_marker = True
                break
        if break_marker == True:
            break
    else:
        print('Такого номера документа нет в базе.')


def add_command(params_type, number, name, directories_number):
    if int(directories_number) == 1 or int(directories_number) == 2 or int(directories_number) == 3:
        documents.append({"type": params_type, "number": number, "name": name})
        directories[directories_number].append(number)
    else:
        print('Введенной полки не существует. Запись не осуществлена.')


def delete():
    doc_number = input('Введите номер документа который нужно удалить: ')
    initial_len = len(documents)
    for i, delete in enumerate(documents):
        if delete["number"] == doc_number:
            documents.pop(i)

    if initial_len == len(documents):
        return "Документ не существует"

    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)

    return "Документ успешно удален"


def move(doc_number, shelf_id):
    doc_existence = False

    if shelf_id not in directories:
        return "Полки не существует"

    for key, value in directories.items():
        if doc_number in value:
            doc_existence = True
            directories[shelf_id] += [doc_number]
            value.remove(doc_number)

    if doc_existence:
        return "Документ успешно перемещен"
    else:
        return "Документ не существует"


def add_shelf():
    shelf = input("Введите номер новой полки: ")
    for direct in directories.items():
        if shelf in direct[0]:
            print(
                f'Такая полка уже существует. Перечень полок на данный момент{list(directories.keys())}')
            break
    else:
        directories[shelf] = []
        print(
            f'Полка добавлена.Перечень полок на данный момент{list(directories.keys())}')


while True:
    command = input('\n \
  Введите одну из команд: p, l, s, a, d, m, as. \n \
  Для выхода наберите exit. \n \
  Для вызов справки наберите help. \n \
  Ваша команда: ')
    if command == 'p':
        people(input('\nВведите номер документа:'))
    elif command == 'l':
        people_list()
    elif command == 's':
        shelf(input('\nВведите номер документа:'))
    elif command == 'a':
        add_command(input('\nВведите тип документа:'), input('Введите номер документа:'), input('Введите имя:'),
                    input('Введите номер полки (1, 2, 3):'))
    elif command == 'd':
        delete()
    elif command == 'm':
        print(move(input('\nВведите номер документа,который хоитите переместить: '),
                   input('\nВведите номер полки, на которую хотите переместить документ: ')))
    elif command == 'as':
        add_shelf()
    elif command == 'exit':
        break
    elif command == 'help':
        print('''\n 
    p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n 
    l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n 
    s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n 
    a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.\n \
    d - delete - команда, которая спросит номер документа и удалит его из каталога и из перечня полок.\n 
    m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую.\n 
    as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень.''')

    else:
        print('Вы ввели некорректную команду, повторите ввод.')
