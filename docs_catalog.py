import os

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(data_base, document_number):
    flag = False
    for record in data_base:
        if record['number'] == document_number:
            flag = True
            return record['name']
    if flag == False:
        return 'Человека с таким номером документа нет в нашей базе!'


def shelf(dirs, document_number):
    flag = False
    for key, val in dirs.items():
        if document_number in val:
            flag = True
            return key
    if flag == False:
        return 'Документа с таким номером нет на наших полках!'


def lists(data_base):
    lists_records = []
    for record in data_base:
        lists_records.append([record['type'], record['number'], record['name']])
    return lists_records


def add(data_base, directories):
    add_type = str(input('Введите тип документа: '))
    add_number = str(input('Введите номер документа: '))
    add_name = str(input('Введите имя, фамилию владельца документа: '))
    add_number_shelf = str(input('Введите номер полки: '))
    new_record = {'type': add_type, 'number': add_number, 'name': add_name}
    if add_number_shelf not in directories.keys():
        return 'Данной полки в нашем архиве не существует.\nПопробуйте снова!'
    else:
        data_base.append(new_record)
    for key, val in directories.items():
        if key == add_number_shelf:
            val.append(data_base[-1]['number'])
    if new_record in data_base:
        return True


def work_programm():
    exit = False
    while exit == False:
        print('Для выхода из программы введите \"e\"')
        input_command = str(input('Введите команду: '))
        if input_command == 'p':
            document_number = str(input('Введите номер искомого документа: '))
            print(people(documents, document_number))
        elif input_command == 's':
            document_number = str(input('Введите номер искомого документа: '))
            print(shelf(directories, document_number))
        elif input_command == 'l':
            for rec in lists(documents):
                print(f'{rec}')
        elif input_command == 'a':
            print(add(documents, directories))
        elif input_command == 'e':
            exit = True
            os.system('clear')
        else:
            os.system('clear')
            print('Такой команды не существует (=')


work_programm()