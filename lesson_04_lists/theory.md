# Урок 4. Списки `list`

`list` — изменяемый упорядоченный список элементов.

```python
users = ["Alex", "Maria", "John"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]   # элементы могут быть разных типов
```

## Когда использовать

- Когда элементов много и их состав меняется.
- Когда нужны индексы и порядок важен.
- Когда нужно сортировать, добавлять, удалять.

## Доступ и срезы

```python
users[0]        # 'Alex'
users[-1]       # 'John'  (последний)
users[0:2]      # ['Alex', 'Maria']  срез
len(users)      # 3
"Alex" in users # True
```

## Основные методы

```python
users.append("Ivan")        # добавить в конец
users.insert(0, "Boris")    # вставить по индексу
users.remove("Maria")       # удалить по значению (первое вхождение)
users.pop()                 # удалить и вернуть последний
users.pop(0)                # удалить и вернуть по индексу
users.sort()                # отсортировать на месте
sorted(users)               # вернуть новый отсортированный список
users.reverse()             # перевернуть
users.count("Alex")         # сколько раз встречается
users.index("Alex")         # индекс первого вхождения
users.extend(["A", "B"])    # добавить элементы из другого списка
```

## Перебор

```python
for user in users:
    print(user)

for i, user in enumerate(users):
    print(i, user)
```

## List comprehension (списковое включение)

Короткий способ построить список:

```python
squares = [x * x for x in range(5)]
# [0, 1, 4, 9, 16]

evens = [x for x in range(10) if x % 2 == 0]
# [0, 2, 4, 6, 8]
```

## Важно про изменяемость

Список изменяется по ссылке:

```python
a = [1, 2, 3]
b = a            # b ссылается на тот же список
b.append(4)
print(a)         # [1, 2, 3, 4]  изменился и a!

# чтобы получить копию:
c = a.copy()     # или c = list(a) или c = a[:]
```
