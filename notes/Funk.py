from datetime import datetime
import json
import file as i

    
def new_note():
    notebook = i.read()
    header = str(input('Заголовок - '))
    body = str(input('Заметка - '))
    date = datetime.now()
    id = str(date.second) + str(date.minute) + str(date.hour) + str(date.day) + str(date.month) + str(date.year)
    note = {
        'time':str(date.date()),
        'header':header,
        'body':body
    }
    notebook[id] = note
    i.write(notebook)

def search_date():
    notebook = i.read()
    d = str(input('Введите день (в формате 04 или 14)- '))
    m = str(input('введите месяц (в формате 02 или 11)-'))
    y = str(input('введите год (в формате 2023 - )'))
    date_search = y + '-' + m + '-' + d
    for note in notebook:
        if date_search == notebook[note]['time']:
            print('ID:', note)
            for key in notebook[note]:
                print(key + ':', notebook[note][key])
            print()

def delete():
    notebook = i.read()
    d = input('Введите id удаляемой записи - ')
    del notebook[d]
    i.write(notebook)

def p():
    notebook = i.read()
    p = str(input('Введите id записи которую вы хотите вывести на экран -'))
    for note in notebook:
        if p == note:
            print('ID:', note)
            for key in notebook[note]:
                print(key + ':', notebook[note][key])
            print()

def pr():
    notebook = i.read()
    for note in notebook:
            print('ID:', note)
            for key in notebook[note]:
                print(key + ':', notebook[note][key])
            print()

def editing():
    notebook = i.read()
    id_editing = str(input('Введите id записи которую вы хотите отредактировать -'))
    h = int(input('Вы хотитте изменить заголовок записи (1 - ДА, 2 - НЕТ) - '))
    if h == 1:
        text = input('Введите новый заголовок - ')
        notebook[id_editing]['header'] = text
    b = int(input('Вы хотитте изменить содержание записи (1 - ДА, 2 - НЕТ) - '))
    if b == 1:
        text = input('Введите новый текст - ')
        notebook[id_editing]['body'] = text
    date = datetime.now()
    notebook[id_editing]['editing'] = str(date.date())
    i.write(notebook)





comande = int(input('1 - Создание заметки; \n 2 - Вывод на экран всех заметок; \n 3 - Вывод на экран заметок по дате; \n 4 - Редактирование заметки; \n 5 - Вывод на экран заметки по id; \n 6 - Удалить заметку; \n Введите номер команды: '))
if comande == 1: new_note()
if comande == 2: pr()
if comande == 3: search_date()
if comande == 4: editing()
if comande == 5: p()
if comande == 6: delete()


