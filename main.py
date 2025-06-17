import argparse

from tabulate import tabulate

from core import where_data, aggregate_data
from utils import read_csv, print_table


def parse_args():
    parser = argparse.ArgumentParser(description="Обработка CSV-файла: фильтрация и агрегация")
    parser.add_argument("--file", required=True, help="Путь к CSV-файлу")
    parser.add_argument("--where", help="Фильтр, формат: column=value или column>value или column<value")
    parser.add_argument("--aggregate", help="Агрегация, формат: column=avg/min/max")
    return parser.parse_args()


def main():
    args = parse_args()
    data = read_csv(args.file)

    if args.where:
        data = where_data(data, args.where)

    if args.aggregate:
        result = aggregate_data(data, args.aggregate)
        print(tabulate(result, headers="keys", tablefmt="grid"))
    else:
        print_table(data)


if __name__ == "__main__":
    main()