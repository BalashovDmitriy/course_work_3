def test_class_operation_init(test_operation, test_operation_2):
    assert test_operation.id_ == 441945886
    assert test_operation.date_ == "30.5.2005"
    assert test_operation.state == "EXECUTED"
    assert test_operation.operation_amount == {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}}
    assert test_operation.description == "Перевод организации"
    assert test_operation.from_ == "Maestro 1596837868705199"
    assert test_operation.to == "Счет 64686473678894779589"

    assert test_operation_2.from_ is None


def test_class_operation_repr(test_operation):
    assert test_operation.__repr__() == ('Operation(id = 441945886, date_ = 30.5.2005, state = EXECUTED, '
                                         "operation_amount = {'amount': '31957.58', 'currency': {'name': 'руб.', "
                                         "'code': 'RUB'}}, description = Перевод организации, from_ = Maestro "
                                         '1596837868705199, to = Счет 64686473678894779589')
