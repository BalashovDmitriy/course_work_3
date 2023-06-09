import json

from src.classes import Operation
from src.funcs import database_sort_by_date, load_from_json, print_result, format_account, format_card, create_instances


def test_load_from_json():
    file = "json/operations.json"
    with open(file, encoding='utf-8') as f:
        operations = json.load(f)
    assert load_from_json("json/operations.json") == operations


def test_database_sort_by_date(database):
    assert database_sort_by_date(database) == [{'date': '2019-04-19T12:02:30.129240',
                                                'description': 'Перевод с карты на карту',
                                                'from': 'Maestro 9171987821259925',
                                                'id': 509552992,
                                                'operationAmount': {'amount': '81513.74',
                                                                    'currency': {'code': 'RUB', 'name': 'руб.'}},
                                                'state': 'EXECUTED',
                                                'to': 'МИР 2052809263194182'},

                                               {'date': '2019-06-30T15:11:53.136004',
                                                'description': 'Перевод со счета на счет',
                                                'from': 'Счет 59956820797131895975',
                                                'id': 414894334,
                                                'operationAmount': {'amount': '95860.47',
                                                                    'currency': {'code': 'RUB', 'name': 'руб.'}},
                                                'state': 'EXECUTED',
                                                'to': 'Счет 43475624104328495820'}]


def test_create_instances(database, test_operations_for_create_instances):
    assert create_instances(database) == test_operations_for_create_instances


def test_print_result(test_operation, test_operation_3):
    assert print_result(test_operation) is True
    assert print_result(test_operation_3) is False


def test_format_account():
    assert format_account(["Счёт", "59956820797131895975"]) == "Счёт **5975"


def test_format_card():
    assert format_card(["Visa", "Classic", "1111222233334444"]) == "Visa Classic 1111 22** **** 4444"
    assert format_card(["Maestro", "5555666677778888"]) == "Maestro 5555 66** **** 8888"
