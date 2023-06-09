import pytest

from src.classes import Operation

id_ = 441945886
date_ = "30.5.2005"
state = "EXECUTED"
operation_amount = {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}
description = "Перевод организации"
to = "Счет 64686473678894779589"
from_ = "Maestro 1596837868705199"


@pytest.fixture
def test_operation():
    return Operation(id_, date_, state, operation_amount, description, to, from_)


@pytest.fixture()
def test_operation_2():
    return Operation(id_, date_, state, operation_amount, description, to)


@pytest.fixture()
def test_operation_3():
    return Operation(id_, date_, "CANCELLED", operation_amount, description, to)


@pytest.fixture
def database():
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
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182"
        }
    ]

@pytest.fixture()
def test_operations_for_create_instances():
    operation_1 = Operation(509552992, "19.4.2019", "EXECUTED",
                            {'amount': '81513.74', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            "Перевод с карты на карту", "МИР 2052809263194182", "Maestro 9171987821259925")
    operation_2 = Operation(414894334, "30.6.2019", "EXECUTED",
                            {'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                            "Перевод со счета на счет", "Счет 43475624104328495820", "Счет 59956820797131895975")
    return [operation_1, operation_2]