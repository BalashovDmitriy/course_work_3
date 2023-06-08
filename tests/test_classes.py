from src.classes import Operation


def test_class_operation():
    id_ = 441945886
    date_ = "30.5.2005"
    state = "EXECUTED"
    operation_amount = {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}
    description = "Перевод организации"
    to = "Счет 64686473678894779589"
    from_ = "Maestro 1596837868705199"

    operation = Operation(id_, date_, state, operation_amount, description, to, from_)
    assert operation.id_ == id_
    assert operation.date_ == date_
    assert operation.state == state
    assert operation.operation_amount == operation_amount
    assert operation.description == description
    assert operation.from_ == from_
    assert operation.to == to

    operation_2 = Operation(id_, date_, state, operation_amount, description, to)
    assert operation_2.from_ is None
