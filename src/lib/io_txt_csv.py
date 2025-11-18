from pathlib import Path
import csv
from typing import Iterable, Sequence
from collections import Counter
from lib.text import normalize, tokenize


def ensure_parent_dir(path: Path | str) -> None:

    p = Path(path)
    parent_dir = p.parent

    """
    Создаём родительскую директорию если её нет
    parents=True - создаёт все промежуточные директории
    exist_ok=True - не вызывает ошибку если директория уже существует
    """

    parent_dir.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """
    Открыть файл на чтение в указанной кодировке и вернуть содержимое как одну строку.
    Обрабатывать ошибки: если файл не найден — поднимать FileNotFoundError (пусть падает),
    если кодировка не подходит — поднимать UnicodeDecodeError (пусть падает).
    """

    p = Path(path)  # Создаем путь к файлу - Path-объект

    if not p.exists():  # Явная проверка существования файла
        raise FileNotFoundError("Файл не найден")

    """
    UnicodeDecodeError поднимается автоматически.
    Для использования разых кодировок необходимо прописать в вызове функции параметр
    encoding=... . 
    Примеры:
    по умолчанию UTF-8: read_text("file.txt")
    другие: read_text("file.txt", encoding="cp1251")
            read_text("file.txt", encoding="koi8-r")
    """
    return p.read_text(encoding=encoding)


import csv
from typing import Iterable, Sequence


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    Создать/перезаписать CSV с разделителем ,.
    Если передан header, записать его первой строкой.
    Проверить, что каждая строка в rows имеет одинаковую длину (иначе ValueError).
    """

    p = Path(path)  # Создаем путь
    rows = list(rows)
    """
    Если на вход функции подавался не список, а другой итерируемый объект (например, кортеж)
    - превращаем его в список. Фиксирует данные на момент вызова функции созданием нового списка.
    """
    with p.open("w", newline="", encoding="utf-8") as f:
        """
        Через менеджер контекста (автозакрытие файла+устойчивость к ошибкам) открываем
        файл в режиме 'w' - чтения, кодировка UTF-8.
        newline="" позволяет избавиться от проблем при работе с файлом в разных ОС.
        Автоматическое преобразование перевода строк
        """
        w = csv.writer(f)  # Создание объекта writer для записи в csv формат
        if header is not None:
            w.writerow(header)  # Записываем заголовок, если такой существует

        if rows:  # Проверка не равную длину строк
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError("Строки имеют разную длину!")

        for r in rows:
            w.writerow(r)  # Записывает ряды построчно


"""Функция не возвращает ничего, она записывает данные в CSV файл."""


def frequencies_from_text(text: str) -> dict[str, int]:
    """
    Подсчитать частоты слов в тексте, используя normalize/tokenize из ЛР3.

    Аргументы:
        text: исходный текст.

    Возвращает:
        dict[str, int]: словарь слово -> частота.
    """

    tokens = tokenize(normalize(text))
    return Counter(tokens)  # dict-like


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """
    Отсортировать пары (слово, частота):
      - сначала по убыванию частоты,
      - затем по алфавиту.

    Аргументы:
        freq: словарь слово -> частота.

    Возвращает:
        list[tuple[str, int]]: отсортированный список.
    """

    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
