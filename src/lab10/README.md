## LAB 10
### **Stack**

**Стек** — это абстрактный тип данных (АТД), представляющий собой коллекцию элементов, организованных по принципу **LIFO (Last In, First Out)** — «последним пришёл, первым вышел». Реализуется как список с ограниченным доступом.

### Основные операции
- **`push(x)`** — положить элемент на вершину стека.
- **`pop()`** — снять и вернуть верхний элемент.
- **`peek()`** — посмотреть верхний элемент, не убирая его.

### Сложность операций (время):
- `push` — O(1) (просто кладём сверху).
- `pop` — O(1) (просто снимаем сверху).
- `peek` — O(1) (просто смотрим).

### Где используется?
- Отмена действия
- История браузера
- Рекурсия и обход в глубину (DFS)

### Реализация
```py
from collections import deque
from typing import Any


class Stack:
    def __init__(self):  # Инициализация стека
        self._data = []

    def is_empty(self) -> bool:
        if len(self._data) == 0:
            return True

    def push(self, item) -> Any:  # Добавление элемента item на вершину стека
        self._data.append(item)

    def pop(self) -> Any:  # Извлечь последний элемент стека
        if self.is_empty():
            raise IndexError("Стек пустой, невозможно извлечь последний элемент")
        return self._data.pop()

    def peek(self) -> Any | None:  # Снять верхний элемент стека и вернуть его
        if self.is_empty():
            return None  # При пустом стеке просмотреть верхний элемент стека и вернуть его невозможно
        return self._data[-1]

    def __len__(self) -> int:
        return len(self._data)
```
![alt text](/images/lab10/stack.png)

### **Queue**

**Queue**— это абстрактный тип данных (АТД), представляющий собой упорядоченную коллекцию элементов, организованную по принципу **FIFO (First In, First Out)** — «первым пришёл, первым вышел».

### Основные операции
- **`enqueue(x)`** — добавить в конец.
- **`dequeue()`** — взять элемент из начала;
- **`peek()`** — посмотреть первый элемент, не удаляя.

### Сложность операций (время):
- `enqueue` — `O(1)`.
- `dequeue` — `O(1)`.
- `peek` — `O(1)`.

### Где используется?
- Очередь задач на печать.
- Очередь сообщений в мессенджере.
- Обход в ширину (BFS) в графах и деревьях.

### Реализация
```py
from collections import deque
from typing import Any


class Queue:
    def __init__(self):  # Инициализация очереди
        self._data = deque()

    def enqueue(self, item) -> None:  # Вставка в конец очереди
        self._data.append(item)

    def dequeue(self) -> Any:  # Взять элемент из начала очереди и вернуть его
        if self.is_empty():
            raise IndexError("Очередь пуста:невозможно извлечь первый элемент")
        return self._data.popleft()

    def peek(self) -> Any | None:  # Вернуть первый элемент без удаления
        if self.is_empty():
            raise None
        return self._data[0]

    def is_empty(self) -> bool:  # Проверка пустоты очереди
        if len(self._data) == 0:
            return True

    def __len__(self) -> int:
        return len(self._data)
```
![alt text](/images/lab10/queue.png)
---

### **Односвязный список**

**Двусвязный список** — это динамическая структура данных, состоящая из последовательности узлов (DoubleNode), где каждый узел содержит данные, ссылку на следующий узел и ссылку на предыдущий узел 

### Основные операции
- **`append(x)`** — добавить элемент в конец списка.
- **`prepend(x)`** — добавить элемент в начало списка.
- **`insert(i, x)`** —  вставить элемент по индексу.
- **`is_empty()`** — добавить элемент в начало списка.
- **`__len__()`** — проверить, пуст ли список.
- **`__iter__()`** —  получить итератор по элементам.

### Где иcпользуется?
- Реализация стеков и очередей.
- Динамическое управление памятью.
- Списки свободных блоков в файловых системах.

---

### **Двусвязный список**

**Двусвязный список** — это динамическая структура данных, состоящая из последовательности узлов (DNode), где каждый узел содержит данные, ссылку на следующий узел и ссылку на предыдущий узел.

### Где иcпользуется?
- Реализация LRU-кэша (Least Recently Used).
- История в браузерах (вперёд/назад).
- Редакторы текста с возможностью отмены.

## Реализация
```py
from typing import Any

class Node: # Узел
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self): # Инициализация пустого списка
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value): # Добавить элемент в конец списка
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else: # Для непустого списка
            self.tail.next = new_node # Устанавливаем указатель next последнего узла на новый элемент
            self.tail = new_node # Теперь new_node - последний узел
            """Итог - не О(n), а о(1)"""
            
        self._size += 1 # Обновляем длину

    def prepend(self, value):
        """Добавить элемент в начало списка, 1 операция"""
        new_node = Node(value, next=self.head)
        self.head = new_node
        
        self._size += 1 # Обновляем длину


    def insert(self, idx, value):
        """Вставка по индексу — неполная реализация, есть ошибки"""
        if idx < 0 or idx > self._size:
            raise IndexError("negative index is not supported")
        
        if idx == 0:
            self.prepend(value)
            return
        
        if idx == self._size:
            self.append(value)
            return
        
        current = self.head
        for _ in range(idx - 1):
            current = current.next # Доходим до эл-та, стоящего до необходимого

        new_node = Node(value, next=current.next) # Создаем необходимый узел. След. за ним - который сейчас на его месте
        current.next = new_node # Делаем ссылке на необходимый новый узел
        
        self._size += 1 # Обновляем длину


    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.value
            current = current.next


    def remove(self, value) -> None:
        current = self.head
        if current is None: # 1. Если список пустой
            return
        if current.value == value: # 2. Если удаляем голову
            self.head = current.next
            self._size -= 1

            # Если список стал пустым, обновляем tail
            if self.head is None:
                self.tail = None

        while current.next is not None: # 3. Если ищем в середине списка
            if current.next.value == value:
                current.next = current.next.next # Если нашли элемент, то меняем его на следующий
                self._size -= 1

                if current.next is None: # Если удалили последний элемет, меняем tail
                    self.tail = current
                return # Выкидывает из списка, когда условие выполнится
            
            current = current.next # Переходим к след. узлу

    def __iter__(self) -> None:
        current = self.head  # Начинаем с головы
        while current is not None:  # Пока не дойдём до конца
            yield current.value     # Возвращаем значение текущего узла
            current = current.next  # Переходим к следующему узлу

    def __len__(self) -> int:
        return self._size
    
    def is_empty(self) -> bool:
        """Проверка, пуст ли список - O(1)"""
        return self._size == 0

    def __repr__(self) -> str:
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    
if __name__ == "__main__":

   test = SinglyLinkedList()
   test.append(1)
   test.append(2)
   test.prepend(0)
   test.prepend('hello!')
   test.append(4)
   print(f'\nИмеющийся список:')
   print(test, '\n')
   print(f'Вставляем 3 на 4 место:')
   test.insert(4, 3)
   print(test, '\n')
   print(f'Удаляем 1 элемент:')
   test.remove('hello!')
   print(test, '\n')
   print(f'Количество элементов:')
   print(test.__len__(), '\n')

```
![alt text](/images/lab10/singlylinkedlist.png)

