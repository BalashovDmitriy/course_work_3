from funcs import create_instances, print_result


def main():
    operations = create_instances()
    counter = 0
    for operation in reversed(operations):
        if counter < 5:
            if print_result(operation):
                counter += 1


if __name__ == '__main__':
    main()
