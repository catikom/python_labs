import pytest
import sys

sys.path.append("C:/Users/user/Desktop/python_labs/")
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    "source, expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлкa", "ежик, елкa"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
    ],
)
def test_normalize_basic(source, expected):
    assert normalize(source) == expected


@pytest.mark.parametrize(
    "source, expected",
    [
        ("привет, мир!", ["привет", "мир"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("    мноооооого ненужного!!", ["мноооооого", "ненужного"]),
        ("", []),
    ],
)
def test_tokenize_basic(source, expected):
    assert tokenize(source) == expected


@pytest.mark.parametrize(
    "tokens, expected",
    [
        (["a", "b", "a", "c", "b", "a"], {"a": 3, "b": 2, "c": 1}),
        ([], {}),
        (["test", "test", "test"], {"test": 3}),
        (["🌍", "🚀", "🌍"], {"🌍": 2, "🚀": 1}),
    ],
)
def test_count_freq_and_top_n(tokens, expected):
    assert count_freq(tokens) == expected


@pytest.mark.parametrize(
    "words, n, expected",
    [
        ({"b": 5, "a": 5, "c": 3, "d": 2}, 2, [("a", 5), ("b", 5)]),
        ({"x": 10}, 5, [("x", 10)]),
        ({}, 3, []),
        ({"a": 1, "b": 1}, 0, []),
    ],
)
def test_top_n_tie_breaker(words, n, expected):
    assert top_n(words, n) == expected
