## LAB_05

### Задание A (json_to_csv)
```py
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
    
    if not json_path.exists():   # Явная проверка существования пути
        raise FileExistsError('Путь не найден')
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
    Работаем с CSV-файлом, записывая в него данные из загруженного ранее JSON-файла.
    '''

    csv_path = Path(csv_path)

    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=data_json[0].keys()) # Записывает список словарей, заголовок - ключи словарей
        writer.writeheader()
        writer.writerows(data_json) # Записываем данные построчно
```
![json_to_csv](/images/lab05/01_json_csv.png)

### Задание A (csv_to_json)

```py
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
    '''
    Работаем с открытым CSV-файлом, пробуем читать как список словарей и отлавливаем ошибки.
    '''
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        try:
            data_csv = csv.DictReader(csv_file)

        except data_csv.fieldnames is None:
            raise ValueError('Отсутствуют заголовки')
        
        if len(list(data_csv)) == 0:
             raise ValueError("Пустой файл")
        data_csv = list(data_csv) # Создаёт список данных, сохраняем считанные данные

    json_path = Path(json_path)
    '''
    Работаем с JSON-файлом, загружая в него данные из CSV_файла.
    '''
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(json.dump(data_csv, json_file, ensure_ascii=False, indent=2))
        '''
        data_csv - что записываем
        json_file -  куда записываем
        ensure_ascii=False - корректная работа с кириллицей
        indent=2 - красивый вывод
        '''
```
![csv_to_json](/images/lab05/01_csv_json.png)

### Задание B (csv_to_xlsx)
```py
from pathlib import Path
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter # Утилита openpyxl для получения буквы столбца таблицы

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """
    Конвертирует CSV в XLSX.
    Использовать openpyxl ИЛИ xlsxwriter.
    Первая строка CSV — заголовок.
    Лист называется "Sheet1".
    Колонки — автоширина по длине текста (не менее 8 символов).
    """

    csv_path = Path(csv_path)
    xlsx_path = Path(xlsx_path)

    if not csv_path.exists():  # Явная проверка существования файла
        raise FileNotFoundError('Файл не найден')
    
    if not xlsx_path.exists():  # Явная проверка существования файла
        raise FileNotFoundError('Файл не найден')
    
    if csv_path.suffix != '.csv':
            raise ValueError("Неверный тип файла")
    '''
    Работаем с CSV-файлом, читаем из него информацию и проверяем на наличие ошибок. Если они есть - они всплывают.
    '''
    with open(csv_path, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)
        csv_file = list(reader) # Сохраняем считанные данные в список
        if len(csv_file) == 0:
             raise ValueError("Пустой файл")
        
        if not reader.fieldnames:
             raise ValueError('Файл не содержит заголовков')
        
        wb = Workbook()      # Создаем рабочую книгу
        ws = wb.active       # Создаём в ней новый лист
        ws.title = "Sheet1"  # Называем его

        ws.append(reader.fieldnames)  # Добавляем заголовок
        for row in csv_file:
            ws.append([row[field] for field in reader.fieldnames])  # В каждую строку таблицы добавляем соответствующую ей информацию
        
        for column in ws.columns:   # Равняем всё по ширине, 8 - минимум
            max_length = 8
            column_letter = get_column_letter(column[0].column)
            for cell in column:
                max_length = max(len(str(cell.value)), max_length)

            ws.column_dimensions[column_letter].width = max_length
            

    wb.save(xlsx_path)  # Сохраняем все изменения в указанном пути
```
![csv_to_xlsx](/images/lab05/02_csv_to_xlsx.png)