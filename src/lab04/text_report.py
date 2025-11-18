import sys

sys.path.append("C:/Users/user/Desktop/python_labs/src/")
from lib.text import normalize, tokenize, count_freq, top_n
from lib.io_txt_csv import read_text, write_csv


txt = read_text("data/input.txt", encoding="cp1251")
txt = tokenize(normalize(txt))
txt_counts = top_n(count_freq(txt))
print("Всего слов:", len(txt))
print("Уникальных слов:", len(set(txt)))
print("Топ-5:")
for i in txt_counts:
    print(f"{i[0]}:{i[1]}")

write_csv(txt_counts, "data/report.csv", ("word", "count"))
