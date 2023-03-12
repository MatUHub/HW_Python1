import json
import datetime
data = {}

def save():
    with open("data.json", "w", encoding="utf-8") as dat:
        json.dump(data, dat)
        print("Данные сохранены!")

def add():
    header = input("Введите название заметки: ")
    context = input("Введите текст заметки: ")
    data[header] = dateTime(), context

    print("Заметка создана")

def dateTime() :
    time = datetime.datetime.today().strftime("%Y/%m/%d-%H.%M.%S")
    return time

def showAll():
    for a in data:
     print(a)
     print(data[a][0])

def showNote():
    header = input("Введите название заметки: ")
    count = 0
    for a in data:
        if a == header:
            print(data[header][0])
            count = 1
    if count == 0:
        print("Такой заметки нет в базе данных!")

def delete():
    print("Удаление заметки!")
    header = input("Введите название заметки: ")
    try:
      del data[header]
      print("Заметка удалена")
    except:
       print("Такой заметки нет в записной книжке!")

def edit():
    header = input("Введите название заметки: ")
    count = 0
    for a in data:
        if a == header:
            text = input("Введите новое содержание заметки: ")
            data[header][1] = text
            data[header][0] = dateTime()
            print("Заметка изменена!")
            count = 1
    if count == 0:
        print("Такой заметки нет в базе данных!")

try:
    with open("data.json", "r") as dat:
        data = json.load(dat)
except:
    data = {}

while True:
    command = input("Введите команду: ")
    if command == "add":
        add()

    elif command == "show":
        showAll()

    elif command == "showNote":
        showNote()

    elif command == "del":
        delete()

    elif command == "save":
        save()

    elif command == "edit":
        edit()

    elif command == "quite":
        save()
        exit()

    elif command == "help":
        print("show - показать название всех заметок,\nshowNote - показать содержание заметки,\nadd - добавить заметку,\ndel - удалить заметку,\nsave - созранить изменения,\nedit - изменить заметку,\nquite - выход из программы")

    else:
        print("команда не распознана, для вывода списка команд введите help")
