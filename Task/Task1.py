'''
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной

******

Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных. (Добавить возможность копировать данных из одного файла в другой. Мы вводим номер строки, которую нужно перенести. См. заготовку elif command == 'c')

!Если получится!
Сделать волидацию имени
'''

import csv
from csv import DictReader, DictWriter
from os.path import exists
class LenNumberError: #будет позже изучаться, если тяжело можно неделать
    def __init__(self, txt):
        self.txt = txt

def get_info(): # функция получения данных о юзере
    first_name = 'Ivan'
    last_name = 'Ivanov'
    is_valid_number = False
    while not is_valid_number:
        try:
            phone_number = int(input("Введите номер: "))
            if len(str(phone_number)) != 11:
                raise LenNumberError("Невалидная длина")
            else:
                is_valid_number = True
        except ValueError:
            print("Невалидный номер")
            continue
        except LenNumberError as err:
            print(err)
            continue

    return [first_name, last_name, phone_number]

def create_file(file_name): # функция создания файла
    with open(file_name, 'w', encoding='utf-8') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()

def read_file(file_name): # функция чтения файла
    with open(file_name, 'r', encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)
    
def write_file(file_name): # функция записи файла
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['телефон'] == str(user_data[2]):
            print('Такой пользователь уже существует')
            return
    obj = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

def copy(copied_file_name, target_file_name): #функция копирования
    copied_file = read_file(copied_file_name)
    item = int(input('Введите номер строки: '))
    print(copied_file[item])
    row = [copied_file[item]['имя'], copied_file[item]['фамилия'], copied_file[item]['телефон']]
    with open(target_file_name, 'a+', encoding='utf-8', newline='') as target_file:
        f_writer = csv.writer(target_file)
        f_writer.writerow(row)

file_name = "phone.csv"

def main(): # главная управляющая функция 
    while True:
        command = input("Введите команду: ")
        if command == 'q': # Команда завершения работы цикла
            break
        elif command == 'w': # Команда записи
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r': # Команда чтения
            if not exists(file_name):
                print("Файл не создан. Создайте файл.")
                continue
            print(*read_file(file_name))
        elif command == 'c': # Команда копирования
            if not exists(file_name):
                print("Файл не создан. Создайте файл.")
                continue
            copied_file_name = input("Введите нименование копируемого файла: ")
            #copied_file_name = "phone2.csv"
            if not exists(copied_file_name):
                print("Файл не создан. Создайте файл.")
                continue
            copy(copied_file_name, file_name)
            
main()

