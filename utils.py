import csv
from tabulate import tabulate


def read_csv(file_path: str) -> list[dict]:
    with open(file_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def print_table(data: list[dict]) -> None:
    if data:
        print(tabulate(data, headers="keys", tablefmt="grid"))
    else:
        print("Нет данных для отображения.")