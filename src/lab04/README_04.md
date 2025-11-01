## LAB_04

### Задание A (read_text)


```py
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    '''
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает),
    если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).
    '''

    p = Path(path)   # Создаем путь к файлу - Path-объект
    
    if not p.exists():   # Явная проверка существования файла
        raise FileNotFoundError('Файл не найден')

    '''
    UnicodeDecodeError поднимается автоматически.
    Для использования разых кодировок необходимо прописать в вызове функции параметр
    encoding=... . 
    Примеры:
    по умолчанию UTF-8: read_text("file.txt")
    другие: read_text("file.txt", encoding="cp1251")
            read_text("file.txt", encoding="koi8-r")
    '''
    return p.read_text(encoding=encoding)

```
```py
import csv
from pathlib import Path
from typing import Iterable, Sequence

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:

    '''
    Создать/перезаписать CSV с разделителем ,.
    Если передан header, записать его первой строкой.
    Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
    '''

    p = Path(path)   # Создаем путь
    rows = list(rows)
    '''
    Если на вход функции подавался не список, а другой итерируемый объект (например, кортеж)
    - превращаем его в список. Фиксирует данные на момент вызова функции созданием нового списка.
    '''
    with p.open('w', newline='', encoding = 'utf-8') as f:
        '''
        Через менеджер контекста (автозакрытие файла+устойчивость к ошибкам) открываем
        файл в режиме 'w' - чтения, кодировка UTF-8. 
        newline="" позволяет избавиться от проблем при работе с файлом в разных ОС.
        Автоматическое преобразование перевода строк
        '''
        w = csv.writer(f)   # Создание объекта writer для записи в csv формат
        if header is not None:
            w.writerow(header)   # Записываем заголовок, если такой существует
        
        if rows:    # Проверка не равную длину строк
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError("Строки имеют разную длину!")

        for r in rows:
            w.writerow(r)   # Записывает ряды построчно

'''Функция не возвращает ничего, она записывает данные в CSV файл.'''
```
```py
from pathlib import Path

def ensure_parent_dir(path: Path | str) -> None:

    p = Path(path)
    parent_dir = p.parent
    
    '''
    Создаём родительскую директорию если её нет
    parents=True - создаёт все промежуточные директории
    exist_ok=True - не вызывает ошибку если директория уже существует
    '''
    
    parent_dir.mkdir(parents=True, exist_ok=True)
```
![Задание A](/images/lab04/01_io_txt_csv.png)

### Задание B

```py
import sys   
sys.path.append('C:/Users/user/Desktop/python_labs/src')
from lib.text import normalize, tokenize, count_freq, top_n
from lib.io_txt_csv import read_text, write_csv, write_text


txt = read_text('data/input.txt')
txt = tokenize(normalize(txt))
txt_counts = top_n(count_freq(txt))
print('Всего слов:', len(txt))
print('Уникальных слов:', len(set(txt)))
print('Топ-5:')
for i in txt_counts:  
    print( f'{i[0]}:{i[1]}') 

write_csv(txt_counts, 'data/report.csv', ("word","count"))
```

![Задание B](/images/lab04/02_text_report.png)
