def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold == True:
        text = text.casefold() #строку в нижний регистр

    if yo2e == True:
        text = text.replace('ё', 'е')
    
    text = text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    norm = ' '.join(text.split())
    return norm


import re

def tokenize(text: str) -> list[str]:
    
    key = r'\w+(?:-\w+)*'
    tokens = re.findall(key, text)
    
    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:

    freq = {}

    for token in tokens: 
        freq[token] = dict.get(token, 0) + 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_items = sorted(freq.items())
    sorted_items = sorted(sorted_items, key = lambda x : x[1], reverse = True)

    return sorted_items[:n]
