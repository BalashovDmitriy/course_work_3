from funcs import create_instances


def main():
    operations = create_instances()
    for operation in operations:
        print(operation)


if __name__ == '__main__':
    main()
