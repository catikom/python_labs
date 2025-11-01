from pathlib import Path
import json
import csv
import sys
sys.path.append('C:/Users/user/Desktop/python_labs/')

def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_path = Path(csv_path)

    if not csv_path.exists():
        raise FileNotFoundError('Файл не найден')
    
    if csv_path.suffix != '.csv':
            raise ValueError("Неверный тип файла")

    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        try:
            data_csv = csv.DictReader(csv_file)

        except data_csv.fieldnames is None:
            raise ValueError('Отсутствуют заголовки')
        
        if len(list(data_csv)) == 0:
             raise ValueError("Пустой файл")
        data_csv = list(data_csv)

    json_path = Path(json_path)

    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_csv, json_file, ensure_ascii=False, indent=2)

csv_to_json('data/samples/people.csv', 'data/out/people_from_csv.json')