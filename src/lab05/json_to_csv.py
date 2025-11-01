from pathlib import Path
import json
import csv
import sys
sys.path.append('C:/Users/user/Desktop/python_labs/')

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_path = Path(json_path)   # Создаем путь к файлу - Path-объект
    
    # if not json_path.exists():   # Явная проверка существования файла
    #     raise FileExistsError('Файл не найден')
    '''
    Работаем с открытым JSON-файлом на чтение, загружаем его, паралелльно отлавливая ошибки.
    '''
    with open(json_path, 'r', encoding='utf-8') as json_file:
        try:
            data_json = json.load(json_file)

        except json.JSONDecodeError:   # Выходит, когда файл невозможно загрузить в формате JSON
            raise ValueError("Пустой JSON или неподдерживаемая структура")
        
        except not data_json:  # Явная проверка существования файла
            raise FileNotFoundError("Файл не найден")
        
        except not isinstance(data_json, list):
            raise ValueError('Файл не JSON формата: не список словарей')
        
        except not all(isinstance(row, dict) for row in data_json):
            raise ValueError('Файл не JSON формата: в списке не словари')
    '''
    Работаем с файлом формата .csv, записывая в него данные из загруженного ранее JSON-файла.
    '''

    csv_path = Path(csv_path)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_json[0].keys())
        writer.writeheader()
        writer.writerows(data_json)
        

json_to_csv('data/samples/people.json', "data/out/people_from_json.csv")