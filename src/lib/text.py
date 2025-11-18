def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if casefold == True:
        text = text.casefold()

    if yo2e == True:
        text = text.replace("ё", "е")

    text = text.replace("\t", " ").replace("\n", " ").replace("\r", " ")
    norm = " ".join(text.split())
    return norm


# print(normalize("ёжик, Ёлкa"))
import re


def tokenize(text: str) -> list[str]:

    key = r"\w+(?:-\w+)*"
    tokens = re.findall(key, text)

    return tokens


def count_freq(tokens: list[str]) -> dict[str, int]:

    freq = {}

    for token in tokens:
        freq[token] = freq.get(token, 0) + 1

    return freq


assert count_freq(["a", "b", "a", "c", "b", "a"]) == {"a": 3, "b": 2, "c": 1}


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    sorted_items = sorted(freq.items())
    sorted_items = sorted(sorted_items, key=lambda x: x[1], reverse=True)

    return sorted_items[:n]
