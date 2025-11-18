from pathlib import Path
import json
import csv
import sys

sys.path.append("C:/Users/user/Desktop/python_labs/")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError("Файл не найден")

    if csv_path.suffix != ".csv":
        raise ValueError("Неверный тип файла")

    with open(csv_path, "r", encoding="utf-8") as csv_file:
        data_csv = csv.DictReader(csv_file)

        # if data_csv.fieldnames is None:
        #     raise ValueError("Отсутствуют заголовки")

        data_csv = list(data_csv)
        if len(data_csv) == 0:
            raise ValueError("Пустой файл")

    json_path = Path(json_path)

    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(data_csv, json_file, ensure_ascii=False, indent=2)


csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_path = Path(json_path)  # Создаем путь к файлу - Path-объект

    if not json_path.exists():  # Явная проверка существования пути
        raise FileNotFoundError("Путь не найден")
    """
    Работаем с открытым JSON-файлом на чтение, загружаем его, паралелльно отлавливая ошибки.
    """
    with open(json_path, "r", encoding="utf-8") as json_file:
        try:
            data_json = json.load(json_file)

        except (
            json.JSONDecodeError
        ):  # Выходит, когда файл невозможно загрузить в формате JSON
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not data_json:  # Явная проверка существования данных
        raise ValueError("Пустой файл")

    if not isinstance(data_json, list):
        raise ValueError("Файл не JSON формата: не список словарей")

    if not all(isinstance(row, dict) for row in data_json):
        raise ValueError("Файл не JSON формата: в списке не словари")
    """
    Работаем с CSV-файлом, записывая в него данные из загруженного ранее JSON-файла.
    """

    csv_path = Path(csv_path)

    with open(csv_path, "w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(
            csv_file, fieldnames=data_json[0].keys()
        )  # Записывает список словарей, заголовок - ключи словарей
        writer.writeheader()
        writer.writerows(data_json)  # Записываем данные построчно


# json_to_csv('data/samples/people.json', 'data/out/people_from_json.csv')
