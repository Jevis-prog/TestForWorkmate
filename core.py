def where_data(data: list[dict], condition: str) -> list[dict]:
    """
    Фильтрует данные по условию: column=value, column>value, column<value
    Поддерживает числовые и строковые значения
    """
    if ">" in condition:
        column, value = condition.split(">", 1)
        operator = ">"
    elif "<" in condition:
        column, value = condition.split("<", 1)
        operator = "<"
    elif "=" in condition:
        column, value = condition.split("=", 1)
        operator = "="
    else:
        raise ValueError(f"Неверный формат фильтра: {condition}")

    column = column.strip()
    value = value.strip()

    def try_parse(val: str):
        try:
            return float(val) if "." in val else int(val)
        except ValueError:
            return val

    target_value = try_parse(value)

    def match(row: dict) -> float | int:
        row_value = try_parse(row[column])
        if isinstance(row_value, (int, float)) and isinstance(target_value, (int, float)):
            if operator == ">":
                return row_value > target_value
            elif operator == "<":
                return row_value < target_value
            elif operator == "=":
                return row_value == target_value
        else:
            if operator == "=":
                return str(row_value) == str(target_value)
            else:
                raise ValueError(f"Нельзя сравнивать строки с операцией '{operator}'")

    return [row for row in data if match(row)]

def aggregate_data(data: list[dict], aggregation: str) -> list[dict]:
    """
    Выполняет агрегацию: column=avg/min/max
    Возвращает результат в виде списка словарей для tabulate.
    """
    try:
        column, operator = aggregation.split("=", 1)
        column = column.strip()
        operator = operator.strip().lower()
    except ValueError:
        raise ValueError(f"Неверный формат агрегации. {aggregation}")

    # Преобразуем все значения колонки в числа
    try:
        values = [float(row[column]) for row in data]
    except KeyError:
        raise ValueError(f"Колонка '{column}' не найдена")
    except ValueError:
        raise ValueError(f"Колонка '{column}' содержит нечисловые значения")

    if not values:
        return [{operator: "Нет данных"}]

    if operator == "avg":
        result = sum(values) / len(values)
    elif operator == "min":
        result = min(values)
    elif operator == "max":
        result = max(values)
    else:
        raise ValueError(f"Неподдерживаемая операция агрегации: {operator}")

    return [{operator: round(result, 2)}]