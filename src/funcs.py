import json
from datetime import datetime
from src.classes import Operation
from operator import itemgetter


def load_from_json(file):
    """
    Загружает из файла список словарей
    :param file: файл с джейсоном
    :return: список словарей из файла
    """
    with open(file, encoding='utf-8') as f:
        operations = json.load(f)
    return operations


def database_sort_by_date(db):
    """
    Убирает пустой словарик из списка словарей и сортирует по ключу 'date'
    :param db: список словарей
    :return: новый отсортированный список словарей
    """
    database = []
    for item in db:
        if item:
            database.append(item)
    return sorted(database, key=itemgetter('date'))


def create_instances(database):
    """
    Создаёт и возвращает экземпляры класса Operation
    :return: экземпляры класса Operation
    """
    instances = []
    operations = database_sort_by_date(database)
    for operation in operations:
        id_ = operation['id']

        date_ = operation['date']
        the_date = datetime.fromisoformat(date_)
        new_date = f'{the_date.day}.{the_date.month}.{the_date.year}'

        state = operation['state']
        operation_amount = operation['operationAmount']
        description = operation['description']
        from_ = operation.get('from')
        to = operation['to']
        instances.append(Operation(id_, new_date, state, operation_amount, description, to, from_))
    return instances


def print_result(operation):
    """
    Печать результатов если поле state в экземпляре класса Operation == "EXECUTED"
    :param operation: экземпляр класса
    :return: True если поле экземпляра класса Operation == "EXECUTED"
             и False в ином случае
    """
    if operation.state == 'EXECUTED':
        print(f'{operation.date_} {operation.description}')

        if operation.from_:
            numbers = operation.from_.split()
            if len(numbers[-1]) == 16:
                print(format_card(numbers))
            elif len(numbers[-1]) == 20:
                print(format_account(numbers), end="")
            print(" -> ", end="")
            numbers = operation.to.split()
            if len(numbers[-1]) == 16:
                print(format_card(numbers))
            elif len(numbers[-1]) == 20:
                print(format_account(numbers), end="")
            print()
        else:
            print(f"Счёт **{operation.to[-4:]}")

        print(f'{operation.operation_amount["amount"]} {operation.operation_amount["currency"]["name"]}')
        print()
        return True
    return False


def format_account(nums):
    """
    Форматирование счёта в соответствие с ТЗ
    :param nums: список слов
    :return: отформатированная строка
    """
    return f'{nums[0]} **{nums[-1][-4:]}'


def format_card(nums):
    """
    Форматирование номера карты в соответствие с ТЗ
    :param nums: список слов
    :return: отформатированная строка
    """
    formatted_card = f'{nums[-1][:4]} {nums[-1][4:6]}** **** {nums[-1][-4:]}'
    the_list = []
    for element in nums:
        if element != nums[-1]:
            the_list.append(element)
    the_list.append(formatted_card)
    return " ".join(the_list)
