# PYTHON LABS
## LAB_01
### Задание 1

```py
name = str(input('Имя: '))
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![Задание 1](/images/lab01/01_greeting.py.png)

### Задание 2

```py
a = float(str(input('a: ')).replace(',', '.'))
b = float(str(input('b: ')).replace(',', '.'))
print(f'sum={format(a+b, '.2f')}; avg={format((a+b)/2, '.2f')}')
```

![Задание 2](/images/lab01/02_sum_avg.py.png)

### Задание 3

```py
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

```py
min = int(input('Минуты: '))
print(f'{(min // 60):02d}:{(min % 60):02d}')
```

![Задание 4](images/lab01/04_minutes_to_hhmm.py.png)

### Задание 5

```py
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

```py
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:

    if nums == []:
        raise ValueError('Список пустой') 
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
```

![Задание 1(min_max)](/images/lab02/01_arrays_min_max.png)

### Задание 1 (unique_sorted)

```py
def unique_sorted(nums: list[float | int]) -> list[float | int]:

    nums = list(set(nums))
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

                '''
                Сортировка пузырьком:
                Каждый проход бОльшего цикла "всплывает" самый большой элемент из
                неотсортированной части. С каждым проходом сокращаем диапазон, т.к.
                последние i элементов уже на своих местах. Сравниваем последние числа
                '''
                
    return nums
```

![Задание 1(unique_sorted)](/images/lab02/01_arrays_unique_sorted.png)

### Задание 1 (flatten)

```py
def flatten(mat: list[list | tuple]) -> list:
    
    new_mat = []
    for elements in mat:
            if isinstance(elements, tuple | list):
                '''Проверяет, список/кортеж ли элемент'''

                for element in elements:
                    new_mat.append(element)
                '''
                Если все элементы удовлетворяют условию, то проходимся по
                элементам внутри каждого из них и добавляем в "сплющенную" матрицу
                '''
                
            else:
                raise TypeError('Элемент не того типа данных')
            '''Если есть элемент, не являющийся списком/кортежем, выводит ошибку'''

    return new_mat
```
![Задание 1(flatten)](/images/lab02/01_arrays_flatten.png)

### Задание 2 (transpose)

```py
def transpose(mat: list[list[float | int]]) -> list[list]:

    if not mat:
        return []
        '''Проверка наличия элементов в матрице'''
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            raise ValueError('Матрица рваная')
            '''Проверка на одинаковую длину строк'''

    len_row = len(mat[0])
    len_col = len(mat)
    new_mat =[]

    for col_ind in range(len_row):
        new_row = []
        '''
        C каждым запуском цикла создаётся ряд, рядов столько,
        сколько столбцов в изначальной матрице
        '''
        for row_ind in range(len_col):
            new_row.append(mat[row_ind][col_ind])
            '''
            Элементов в ряд добавляется столько, сколько
            столбцов в изначальной матрице
            '''
        new_mat.append(new_row)
        '''Ряд добавляется в новую матрицу'''

    return new_mat
```
![Задание 2(transpose)](/images/lab02/02_matrix_transpose.png)

### Задание 2 (row_sums)

```py
def row_sums(mat: list[list[float | int]]) -> list[float]:
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            raise ValueError('Матрица рваная')
            '''Проверка на одинаковую длину строк'''

    sum_row = []

    for row in mat:
        sum_row.append(sum(row))

    return sum_row
```

![Задание 2(row_sums)](/images/lab02/02_matrix_row_sums.png)

### Задание 2 (col_sums)

```py
def col_sums(mat: list[list[float | int]]) -> list[float]:

    len_row = len(mat[0])
    len_col = len(mat)
    
    for num in range(len(mat) - 1):
        if len(mat[num]) != len(mat[num + 1]):
            raise ValueError('Матрица рваная')
            '''Проверка на одинаковую длину строк'''

    sum_col = []

    for col in range(len_row):
        summa = 0
        for row in range(len_col):
            summa += mat[row][col] #меняем индексы местами
        sum_col.append(summa)
    
    return sum_col
```

![Задание 2(col_sums)](/images/lab02/02_matrix_col_sums.png)

### Задание 3 (tuples)

```py
def format_record(rec: tuple[str, str, float]) -> str:

    fio = rec[0].title().split()
    if fio == [] or len(fio) == 1 or rec[1] == [] or rec[2] == []:
        raise ValueError("Пустые значения")
    '''ValueError, если пустые имя/группа/GPA'''

   if  not isinstance(rec[0], str) or not isinstance(rec[1], str) or not isinstance(rec[2], float) :
        if not isinstance(rec, tuple):
            raise TypeError('Некорректный тип данных')
    '''TypeError, если некорректный тип данных'''
    

    if len(fio) == 3:
        f_io = f"{fio[0]} {fio[1][0]}. {fio[2][0]}."
    else:
        f_io = f"{fio[0]} {fio[1][0]}."
    """В 1 элементе кортежа все 1 буквы становятся прописными,
       в f_io сохраняются фамилия и инициалы"""
    
    GPA = f'GPA {format(round(rec[2], 2), '.2f')}'
    '''Округление (round), 2 знака после запятой(format)'''

    return f'{f_io}, гр. {rec[1]}, {GPA}'

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```

![Задание 3 (tuples)](/images/lab02/02_tuples.png)



## LAB_03

### Задание 1 (normalize)

```py
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''
    Если casefold=True — привести к casefold (лучше, чем lower для Юникода).
    Если yo2e=True — заменить все ё/Ё на е/Е.
    Убрать невидимые управляющие символы (например, \t, \r) →
    заменить на пробелы, схлопнуть повторяющиеся пробелы в один.
    '''

    if casefold == True:
        text = text.casefold()    # строку в нижний регистр

    if yo2e == True:
        text = text.replace('ё', 'е')
    
    text = text.replace('\t', ' ').replace('\n', ' ').replace('\r', ' ')
    norm = ' '.join(text.split())
    '''
    Cплитом убираем все пробелы; получившийся список методом
    " ".join() снова превращаем в строку
    '''
    return norm

assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"
assert normalize("Hello\r\nWorld") == "hello world"
assert normalize("  двойные   пробелы  ") == "двойные пробелы"

```

![Задание 1 (normalize)](/images/lab03/01_text_normalize.png)

### Задание 1 (tokenize)

```py
import re  

def tokenize(text: str) -> list[str]:
    '''
    Разбить на «слова» по небуквенно-цифровым разделителям.
    В качестве слова считаем последовательности символов \w 
    (буквы/цифры/подчёркивание) плюс дефис внутри слова (например, по-настоящему).
    Числа (например, 2025) считаем словами.

    Множество слов — это все подстроки, удовлетворяющие шаблону
    \w+(?:-\w+)*
    (буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые
    любыми не-\w символами.
    '''
    key = r'\w+(?:-\w+)*'

    '''
    Регулярное выражение (находит все совпадения шаблону '\w+(?:-\w+)*')
    имеет структуру r'...':
    1) \w+ означает один или более символов типа букв, цифр, подчёркивание
    2) (?:...) - незахватывающая группа. То есть всё, что после дефиса,
       не будет запоминаться как отдельное слово, оно будет присоединенино к предыдущему нахождению.
    3) -\w+ - буквы и цифры после дефиса
    4) * означает любое количество подобных вхождений (0-бесконечность)
    '''
    
    # Находим все совпадения через findall. tokens - это список
    tokens = re.findall(key, text)
    
    return tokens

assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

```

![Задание 1 (tokenize)](/images/lab03/01_text_tokenize.png)

### Задание 1 (count_freq)

```py
def count_freq(tokens: list[str]) -> dict[str, int]:

    '''Подсчитать частоты, вернуть словарь слово → количество.'''

    freq = {} #создаём словарь, в который и будем вносить слова и частоты

    for key in tokens: #пробегаемся по каждому токену
        freq[key] = freq.get(key, 0) + 1
        '''get возвращает текущее значение, если ключ уже есть в словаре + 1
           или 0 + 1, если в словаре ключа еще нет в словаре. Он появляетя там в виде {key:1} '''

    return freq

freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
```

![Задание 1 (count_freq)](/images/lab03/01_text_count_freq.png)


### Задание 1 (top_n)

```py
def top_n(freq: dict[str, int], n: int = 2) -> list[tuple[str, int]]:

    '''Вернуть топ-N по убыванию частоты; при равенстве — по алфавиту слова.'''

    sorted_items = sorted(freq.items())
    sorted_items = sorted(sorted_items, key = lambda x : x[1], reverse = True)
    '''
    Сортируем словарь сначала по алфавиту, потом уже отсортированный словарь
    (теперь список кортежей) сортируем по частотам (reverse для того, чтобы сначала
    отображался самый большой).
    Что делает lambda x: мини-функция, которая возвращает элемент x[1] кортежа ('слово', частота)
    => он становится ключом. Первая сортировка работает и без ключа, так как по умолчанию
    функция sorted сортирует по 1 элементу (в нашем случаю - по ключу)
    '''

    return sorted_items[:n]
    '''Возвращаем первые n элементов срезом'''

freq = count_freq(["a","b","a","c","b","a"])
assert top_n(freq, 2) == [("a",3), ("b",2)]
```

![Задание 1 (top_n)](/images/lab03/01_text_top_n.png)

### Задание 2 (text_stats)

```py
import sys   #импортируем систему, чтобы применить ввод stdin и добавить путь к папке
sys.path.append('C:/Users/user/Desktop/python_labs/src')  #добавляем путь к папке, чтобы он нашел папку lib
from lib.text import normalize, tokenize, count_freq, top_n

def main():

    line = sys.stdin.read()   #Читает весь ввод до конца файла. Сtrl+Z+Enter для прерывания ввода
    
    norm_line = tokenize(normalize(line))   #без этого шага слова в верхнем и нижнем регистре будут считаться разными
    uniq_line = len(set(norm_line))   #set возвращает список уникальных элементов (без повтроений)
    freq = count_freq(norm_line)
    top5 = top_n(freq, 5)


    print('Всего слов:', len(norm_line))
    print('Уникальных слов:', uniq_line)
    print('Топ-5:')
    for i in top5:   #цикл для ввода в i=5 строк
        print( f'{i[0]}:{i[1]}') 

while True:  #опционально: для бесконечного вызова функции
    main()   #вызов функции
```
![Задание 2 (text_stats)](/images/lab03/02_text_stats.png)




