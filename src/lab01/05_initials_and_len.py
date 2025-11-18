fio = str(input("ФИО: "))
for i in range(len(fio)):
    fio = fio.replace(" ", "")
init = ""
for i in fio:
    if i.upper() == i:
        init += i
print(f"Инициалы: {init}.")
print("Длина (символов):", len(fio) + 2)
