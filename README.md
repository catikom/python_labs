### Задание 1

`name = str(input('Имя: '))
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')`

![Задание 1](/images/01_greeting.py.png)

### Задание 2

`a = float(str(input('a: ')).replace(',', '.'))
b = float(str(input('b: ')).replace(',', '.'))
print(f'sum={format(a+b, '.2f')}; avg={format((a+b)/2, '.2f')}')`

![Задание 2](\images\02_sum_avg.py.png)

### Задание 3

`price = int(input())
discount = int(input())
vat = int(input())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f"База после скидки: {format(base, '.2f')} руб")
print(f"НДС:               {format(vat_amount, '.2f')} руб")
print(f"Итого к оплате:    {format(total, '.2f')} руб")`

![Задание 3](/images/03_discount_vat.py.png)

### Задание 4

`min = int(input('Минуты: '))
hh = min // 60
mm = min - 60 * hh
if mm < 10:
    mm = '0' + str(mm)
print(f'{hh}:{mm}')`

![Задание 4](/images/04_minutes_to_hhmm.py.png)

### Задание 5

`fio = str(input('ФИО: '))
for i in range(len(fio)):
    fio = fio.replace(" ", "")
init = ''
for i in fio:
    if i.upper() == i:
        init += i
print(f'Инициалы: {init}.')
print('Длина (символов):', len(fio) + 2)`

![Задание 5](/images/05_initials_and_len.py.png)