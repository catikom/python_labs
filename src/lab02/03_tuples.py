def format_record(rec: tuple[str, str, float]) -> str:

    fio = rec[0].title().split()
    if fio == [] or len(fio) == 1 or rec[1] == [] or rec[2] == []:
        return ValueError("ValueError")
    """ValueError, если пустые имя/группа/GPA"""

    if (
        not isinstance(rec[0], str)
        or not isinstance(rec[1], str)
        or not isinstance(rec[2], float)
    ):
        if not isinstance(rec, tuple):
            return TypeError("TypeError")
    """TypeError, если некорректный тип данных"""

    if len(fio) == 3:
        f_io = f"{fio[0]} {fio[1][0]}. {fio[2][0]}."
    else:
        f_io = f"{fio[0]} {fio[1][0]}."
    """В 1 элементе кортежа все 1 буквы становятся прописными,
       в f_io сохраняются фамилия и инициалы"""

    GPA = f"GPA {format(round(rec[2], 2), '.2f')}"
    """Округление, 2 знака после запятой """

    return f"{f_io}, гр. {rec[1]}, {GPA}"


print(format_record(["Иванов", "BIVT-25", 4.6]))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
