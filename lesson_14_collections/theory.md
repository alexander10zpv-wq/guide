# Урок 14. Модуль `collections`: `deque`, `Counter`, `defaultdict`, `namedtuple`

Все эти типы лежат в модуле `collections`.

```python
from collections import deque, Counter, defaultdict, namedtuple
```

## `deque` — двусторонняя очередь

```python
queue = deque()
queue.append("task1")     # добавить справа
queue.append("task2")
queue.appendleft("task0") # добавить слева

first = queue.popleft()   # взять с начала
last = queue.pop()        # взять с конца
```

### Когда использовать

- Очереди задач, BFS-обходы.
- Когда нужны быстрые операции в начале **и** конце.

### Почему `deque` лучше `list` для очереди

- `list.pop(0)` — медленный, сдвигает все элементы.
- `deque.popleft()` — быстрый, O(1).

## `Counter` — подсчёт элементов

```python
words = ["cat", "dog", "cat", "bird", "cat"]
c = Counter(words)
print(c)              # Counter({'cat': 3, 'dog': 1, 'bird': 1})
print(c["cat"])       # 3
print(c["fish"])      # 0  (нет — но без ошибки!)

c.most_common(2)      # [('cat', 3), ('dog', 1)]
```

### Когда использовать

- Подсчёт частоты слов / событий / ошибок.
- Статистика, топ N.

## `defaultdict` — словарь со значением по умолчанию

Обычно при первом обращении к ключу нужно проверять, есть ли он:

```python
groups = {}
if "admins" not in groups:
    groups["admins"] = []
groups["admins"].append("Alex")
```

С `defaultdict` короче:

```python
groups = defaultdict(list)
groups["admins"].append("Alex")  # сам создаст пустой список
groups["admins"].append("Maria")
```

`defaultdict(int)` удобен для счётчиков:

```python
count = defaultdict(int)
for word in words:
    count[word] += 1
```

### Когда использовать

- Группировка данных.
- Счётчики.
- Словари списков / множеств.

## `namedtuple` — кортеж с именованными полями

```python
User = namedtuple("User", ["name", "age"])
u = User("Alex", 25)

print(u.name)   # 'Alex'
print(u.age)    # 25
print(u[0])     # 'Alex'  (всё ещё кортеж)
```

### Когда использовать

- Лёгкие неизменяемые структуры (точка, координата, RGB).
- Возврат нескольких именованных значений из функции.

Сегодня часто удобнее использовать [`dataclass`](../lesson_15_dataclass/theory.md), но `namedtuple` остаётся хорошим лёгким вариантом.
