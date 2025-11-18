import sys  # импортируем систему, чтобы применить ввод stdin

sys.path.append("C:/Users/user/Desktop/python_labs/src")
from lib.text import normalize, tokenize, count_freq, top_n


def main():

    line = (
        sys.stdin.read()
    )  # Читает весь ввод до конца файла. Сtrl+Z+Enter для прерывания ввода

    norm_line = tokenize(
        normalize(line)
    )  # без этого шага слова в верхнем и нижнем регистре будут считаться разными
    uniq_line = len(
        set(norm_line)
    )  # set возвращает список уникальных элементов (без повтроений)
    freq = count_freq(norm_line)
    top5 = top_n(freq, 5)

    print("Всего слов:", len(norm_line))
    print("Уникальных слов:", uniq_line)
    print("Топ-5:")
    for i in top5:  # цикл для ввода в i=5 строк
        print(f"{i[0]}:{i[1]}")


while True:  # опционально: для бесконечного вызова
    main()  # вызов функции
