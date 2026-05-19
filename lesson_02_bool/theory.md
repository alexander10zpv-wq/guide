# Урок 2. Логический тип `bool`

`bool` — это тип данных с двумя значениями: `True` и `False`.

```python
is_active = True
is_admin = False
```

## Когда использовать

- Флаги (`is_logged_in`, `has_access`).
- Условия и проверки.
- Статусы (включено/выключено).
- Проверки доступа.

```python
if is_active:
    print("Пользователь активен")
```

## Почему `bool` лучше строк `"yes"/"no"`

- Проще читать.
- Меньше ошибок (опечатка `"Yes"` vs `"yes"` ломает логику).
- Работает напрямую в `if`.

## Логические операторы

```python
a = True
b = False

print(a and b)  # False — оба должны быть True
print(a or b)   # True  — достаточно одного True
print(not a)    # False — инверсия
```

## Приведение к `bool`

Python автоматически приводит значения к `True`/`False`:

```python
bool(0)        # False
bool(1)        # True
bool("")       # False  (пустая строка)
bool("hello")  # True
bool([])       # False  (пустой список)
bool([1, 2])   # True
bool(None)     # False
```

Это используется в `if`:

```python
name = ""
if not name:
    print("Имя пустое")
```

## Важно

`bool` — это подкласс `int`: `True == 1`, `False == 0`. Но в коде проверяй именно тип:

```python
isinstance(True, int)   # True (!)
isinstance(True, bool)  # True
```
