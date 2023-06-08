import json

import pytest

from src.classes import Operation
from src.funcs import database_sort_by_date, load_from_json, print_result, format_account, format_card


@pytest.fixture
def db():
    return [{
        "id": 414894334,
        "state": "EXECUTED",
        "date": "2019-06-30T15:11:53.136004",
        "operationAmount": {
            "amount": "95860.47",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 59956820797131895975",
        "to": "Счет 43475624104328495820"
    },
        {},
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {
                "amount": "81513.74",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            }
        }
    ]


def test_load_from_json():
    file = "json/operations.json"
    with open(file, encoding='utf-8') as f:
        operations = json.load(f)
    assert load_from_json("json/operations.json") == operations


def test_database_sort_by_date(db):
    assert database_sort_by_date(db) == [{'date': '2019-04-19T12:02:30.129240',
                                          'id': 509552992,
                                          'operationAmount': {'amount': '81513.74',
                                                              'currency': {'code': 'RUB', 'name': 'руб.'}},
                                          'state': 'EXECUTED'},
                                         {'date': '2019-06-30T15:11:53.136004',
                                          'description': 'Перевод со счета на счет',
                                          'from': 'Счет 59956820797131895975',
                                          'id': 414894334,
                                          'operationAmount': {'amount': '95860.47',
                                                              'currency': {'code': 'RUB', 'name': 'руб.'}},
                                          'state': 'EXECUTED',
                                          'to': 'Счет 43475624104328495820'}]


def test_create_instances():
    pass


def test_print_result(db):
    id_ = db[0]["id"]
    date_ = db[0]["date"]
    state = db[0]["state"]
    operation_amount = db[0]["operationAmount"]
    description = db[0]["description"]
    to = db[0]["to"]
    from_ = db[0]["from"]

    operation = Operation(id_, date_, state, operation_amount, description, to, from_)
    assert print_result(operation) is True
    operation.state = "CANCELLED"
    assert print_result(operation) is False


def test_format_account():
    assert format_account(["Счёт", "59956820797131895975"]) == "Счёт **5975"


def test_format_card():
    assert format_card(["Visa", "Classic", "1111222233334444"]) == "Visa Classic 1111 22** **** 4444"
    assert format_card(["Maestro", "5555666677778888"]) == "Maestro 5555 66** **** 8888"
