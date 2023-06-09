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