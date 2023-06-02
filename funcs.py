import json
from classes import Operation

FILE = "operations.json"


def load_from_json(file):
    with open(file, encoding='utf-8') as f:
        operations = json.load(f)
    return operations


def create_instances():
    operations = load_from_json(FILE)
    instances = []
    print(operations)
    for operation in operations:
        if operation:
            print(operation)
            id_ = operation['id']
            date_ = operation['date']
            state = operation['state']
            operation_amount = operation['operationAmount']
            description = operation['description']
            from_ = operation.get('from')
            to = operation['to']
            instances.append(Operation(id_, date_, state, operation_amount, description, to, from_))
    return instances
