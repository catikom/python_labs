def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''
    Если casefold=True — привести к casefold (лучше, чем lower для Юникода).
    Если yo2e=True — заменить все ё/Ё на е/Е.
    Убрать невидимые управляющие символы (например, \t, \r) →
    заменить на пробелы, схлопнуть повторяющиеся пробелы в один.
    '''

    if casefold == True:
        text = text.casefold() #строку в нижний регистр

    if yo2e == True:
        text = text.replace('ё', 'е')
    
    text = text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    norm = ' '.join(text.split())
    return norm

assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\r\nWorld") == "hello world"
assert normalize("  двойные   пробелы  ") == "двойные пробелы"


import re

def tokenize(text: str) -> list[str]:
    '''
    Разбить на «слова» по небуквенно-цифровым разделителям.
    В качестве слова считаем последовательности символов \w (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
    Числа (например, 2025) считаем словами.
    '''
    '''
    Множество слов — это все подстроки, удовлетворяющие шаблону
    \w+(?:-\w+)*
    (буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые любыми не-\w символами.
    '''
    key = r'\w+(?:-\w+)*'
    
    # Находим все совпадения
    tokens = re.findall(key, text)
    
    return tokens

assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]



def count_freq(tokens: list[str]) -> dict[str, int]:

    '''Подсчитать частоты, вернуть словарь слово → количество.'''

    dict = {}

    for token in tokens: #пробегаемся по каждому токену
        dict[token] = dict.get(token, 0) + 1
        '''get возвращает текущее значение, если token уже есть в словаре + 1
           или 0 + 1, если в словаре token отсутсвует '''

    return dict

freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}



# print('["a","b","a","c","b","a"] ->', count_freq(["a","b","a","c","b","a"]))

def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:

    '''Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.'''
    
    sorted_items = sorted(freq.items(), key = lambda x : x[1])[::-1]
    sorted_items = sorted(freq.items(), key = lambda x : x[0])
    '''Сортируем словарь сначала по частотам ([::-1] для того, чтобы сначала отображался самый большой), потом по алфавиту'''

    return sorted_items[:n]
    '''Возвращаем первые n элементов'''

freq = count_freq(["a","b","a","c","b","a"])
assert top_n(freq, 2) == [("a",3), ("b",2)]