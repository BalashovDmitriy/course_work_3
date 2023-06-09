from src.funcs import create_instances, print_result, load_from_json

FILE = 'json/operations.json'


def main():
    database = load_from_json(FILE)
    operations = create_instances(database)
    counter = 0
    for operation in reversed(operations):
        if counter < 5:
            if print_result(operation):
                counter += 1


if __name__ == '__main__':
    main()
