import json
from datetime import datetime
from classes import Operation
from operator import itemgetter

FILE = "operations.json"


def load_from_json(file):
    with open(file, encoding='utf-8') as f:
        operations = json.load(f)
    return operations


def database_sort_by_date(db):
    database = []
    for item in db:
        if item:
            database.append(item)
    return sorted(database, key=itemgetter('date'))


def create_instances():
    database = load_from_json(FILE)
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
    if operation.state == 'EXECUTED':
        print(f'{operation.date_} {operation.description}')
        if operation.from_:
            numbers = operation.from_.split()
            if len(numbers[-1]) == 16:
                format_card(numbers[-1])
            elif len(numbers[-1]) == 20:
                format_account(numbers[-1])
        else:
            print(f"Счёт **{operation.to[-4:]}")
        print(f'{operation.operation_amount["amount"]} {operation.operation_amount["currency"]["name"]}')
        print()
        return True
    return False

def format_account(nums):
    pass

def format_card(nums):
    pass