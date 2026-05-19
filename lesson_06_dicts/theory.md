# Урок 6. Словари `dict`

`dict` — структура **ключ → значение**.

```python
user = {
    "name": "Alex",
    "age": 25,
    "email": "alex@example.com",
}
```

## Когда использовать

- JSON-подобные данные, ответы API.
- Настройки, конфиги.
- Быстрый поиск по ключу.
- Кеши.

## Основные операции

```python
user["name"]              # "Alex"
user["is_admin"] = False  # добавить/изменить ключ
del user["age"]           # удалить ключ
"email" in user           # True
len(user)                 # количество ключей
```

### Безопасный доступ — `.get()`

```python
user.get("phone")             # None  (ключа нет — без ошибки)
user.get("phone", "не указан") # "не указан"  (с дефолтом)
```

Через `[]` отсутствующий ключ даёт `KeyError`.

### Перебор

```python
for key in user:                    # ключи
    print(key)

for key, value in user.items():     # ключи и значения
    print(key, "=", value)

for value in user.values():         # только значения
    print(value)
```

## Полезные методы

```python
user.keys()                # dict_keys(['name', 'age', ...])
user.values()              # dict_values(['Alex', 25, ...])
user.items()               # пары (ключ, значение)
user.update({"age": 26})   # обновить/добавить из другого dict
user.pop("age")            # удалить и вернуть значение
user.pop("x", None)        # с дефолтом, если ключа нет
```

## Dict comprehension

```python
squares = {x: x * x for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

## Когда лучше **не** использовать `dict`

Если структура объекта фиксирована и есть бизнес-логика — лучше `dataclass` (см. урок 15).

## Требования к ключам

Ключом могут быть только **hashable** (неизменяемые) значения: `int`, `str`, `tuple` из неизменяемых. Список ключом быть не может.
