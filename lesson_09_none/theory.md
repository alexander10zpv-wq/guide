# Урок 9. Тип `NoneType` и значение `None`

`None` — специальное значение, которое означает **отсутствие значения**. Тип у него — `NoneType`.

```python
result = None
print(type(result))   # <class 'NoneType'>
```

## Когда использовать `None`

- Функция «ничего не вернула» (`return` без значения).
- Значение пока неизвестно или ещё не задано.
- Объект не найден.
- Необязательный параметр функции.

```python
def find_user(user_id):
    # ничего не нашли
    return None

user = find_user(42)
if user is None:
    print("Пользователь не найден")
```

## Сравнивать через `is None`, а не `== None`

Правильно:

```python
if user is None:
    pass

if user is not None:
    pass
```

Не рекомендуется:

```python
if user == None:   # работает, но плохой стиль
    pass
```

Причина: `is` проверяет, что это **тот самый** объект `None`. `==` может работать неожиданно у пользовательских классов с переопределённым `__eq__`.

## Функция без `return` возвращает `None`

```python
def log(msg):
    print(msg)

result = log("hi")
print(result)   # None
```

## `None` как значение по умолчанию

Удобно для необязательных параметров:

```python
def greet(name=None):
    if name is None:
        name = "guest"
    print(f"Hello, {name}")
```

## `None` ↔ `bool`

```python
bool(None)   # False
```

Поэтому `if not value:` сработает и для `None`, и для пустой строки/списка/нуля. Если важно различать «нет значения» и «пустая строка» — используй именно `is None`.
