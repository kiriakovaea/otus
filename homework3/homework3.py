import csv
import json
from typing import List


def read_csv_file(file_name: str):
    """ чтение csv и преобразование информации в список"""
    with open(file_name, 'r') as file_csv:
        reader = csv.reader(file_csv)
        # Извлекаем заголовок
        header = next(reader)
        # Итерируемся по данным делая из них словари
        data_list = []
        for row in reader:
            data_list.append(dict(zip(header, row)))
        return data_list


def read_json_file(file_name: str):
    """ чтение json из файла"""
    with open(file_name, 'r') as json_file:
        users = json.loads(json_file.read())
        return users


def write_json_file(file_name: str, json_data):
    """ запись json в итоговый файл """
    with open(file_name, 'w') as file:
        json.dump(json_data, file, indent=4,
                  ensure_ascii=False)


def get_users_info(users: List[dict]):
    valid_keys = ['name', 'gender', 'age', 'address']
    users_info_list = []
    for user in users:
        user_info = {}
        """оставляем только нужные ключи"""
        for key, value in user.items():
            if key in valid_keys:
                user_info[key] = value
            else:
                continue
        users_info_list.append(user_info)
    users_info_list = get_empty_books_for_users(users_info_list)
    return users_info_list


def get_books_info(books: List[dict]):
    books_list = []
    for book in books:
        """удаляем ключ Publisher и остальные ключи приводим к строчным буквам"""
        del (book['Publisher'])
        for key in list(book.keys()):
            book[key.lower()] = book.pop(key)
        books_list.append(book)
    return books_list


def get_empty_books_for_users(users: list):
    for user in users:
        user.update({'books': []})
    return users


def get_books_for_users():
    users = get_users_info(read_json_file('users.json'))
    books = get_books_info(read_csv_file('books.csv'))
    while len(books) > 0:
        """распределяем каждому юзеру по 1 книге пока не кончатся книги"""
        for user in users:
            if len(books) == 0:
                break
            user['books'].append(books[0])
            del (books[:1])
    return users


users_with_books = get_books_for_users()
write_json_file('result.json', users_with_books)