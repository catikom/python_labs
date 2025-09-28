# PYTHON LABS
## LAB_01
### Задание 1

```
name = str(input('Имя: '))
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![Задание 1](/images/lab01/01_greeting.py.png)

### Задание 2

```
a = float(str(input('a: ')).replace(',', '.'))
b = float(str(input('b: ')).replace(',', '.'))
print(f'sum={format(a+b, '.2f')}; avg={format((a+b)/2, '.2f')}')
```

![Задание 2](/images/lab01/02_sum_avg.py.png)

### Задание 3

```
price = int(input())
discount = int(input())
vat = int(input())
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f"База после скидки: {format(base, '.2f')} руб")
print(f"НДС:               {format(vat_amount, '.2f')} руб")
print(f"Итого к оплате:    {format(total, '.2f')} руб")
```

![Задание 3](/images/lab01/03_discount_vat.py.png)

### Задание 4

```
min = int(input('Минуты: '))
print(f'{(min // 60):02d}:{(min % 60):02d}')
```

![Задание 4](images/lab01/04_minutes_to_hhmm.py.png)

### Задание 5

```
fio = str(input('ФИО: '))
for i in range(len(fio)):
    fio = fio.replace(" ", "")
init = ''
for i in fio:
    if i.upper() == i:
        init += i
print(f'Инициалы: {init}.')
print('Длина (символов):', len(fio) + 2)
```

![Задание 5](/images/lab01/05_initials_and_len.py.png)

## LAB_02

### Задание 1 (min_max)

```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if nums == []:
        return ValueError('ValueError') 
    '''Возвращает ValueError, если список пустой'''
    
    mini = nums[0]
    for next in nums:
        if next < mini:
            mini = next 
    maxi = nums[0]
    for next in nums:
        if next > mini:
            maxi = next 

    return mini, maxi 
    '''В другом случае возвращает минимум и максимум из списка'''

print('[3, -1, 5, 5, 0] ->', min_max([3, -1, 5, 5, 0]))
print('[42] ->', min_max([42]))
print('[-5, -2, -9] ->', min_max([-5, -2, -9]))
print('[] ->', min_max([]))
print('[1.5, 2, 2.0, -3.1] ->', min_max([1.5, 2, 2.0, -3.1]))
```

![Задание 1(min_max)](/images/lab02/01_arrays_min_max.png)

### Задание 1 (unique_sorted)

```
def unique_sorted(nums: list[float | int]) -> list[float | int]:

    nums = list(set(nums))
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

                '''Сортировка пузырьком'''
                
    return nums

print('[3, 1, 2, 1, 3] ->', unique_sorted([3, 1, 2, 1, 3]))
print('[] ->', unique_sorted([]))
print('[-1, -1, 0, 2, 2] ->', unique_sorted([-1, -1, 0, 2, 2]))
print('[1.0, 1, 2.5, 2.5, 0] ->', unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```

![Задание 1(unique_sorted)](/images/lab02/01_arrays_unique_sorted.png)

### Задание 1 (flatten)

```
def flatten(mat: list[list | tuple]) -> list:
    
    new_mat = []
    for elements in mat:
            if isinstance(elements, tuple | list):
                '''Проверяет, список.кортеж ли элемент'''

                for element in elements:
                    new_mat.append(element)
                '''Если все элементы удовлетворяют условию, то проходимся по элементам внутри каждого из них'''
                
            else:
                return TypeError('TypeError')
            '''Если есть элемент, не являющийся списком/кортежем, выводит ошибку'''

    return new_mat

print('[[1, 2], [3, 4]] ->', flatten([[1, 2], [3, 4]]))
print('([1, 2], (3, 4, 5)) ->', flatten(([1, 2], (3, 4, 5))))
print('[[1], [], [2, 3]] ->', flatten([[1], [], [2, 3]]))
print('[[1, 2], "ab"] ->', flatten([[1, 2], "ab"]))
```
![Задание 1(flatten)](/images/lab02/01_arrays_flatten.png)