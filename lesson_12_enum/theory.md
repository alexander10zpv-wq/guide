# Урок 12. Перечисления `Enum`

`Enum` — это набор именованных констант. Удобен для статусов, ролей, режимов.

```python
from enum import Enum

class Status(Enum):
    ACTIVE = "active"
    BLOCKED = "blocked"
    DELETED = "deleted"
```

## Использование

```python
status = Status.ACTIVE

print(status)         # Status.ACTIVE
print(status.name)    # 'ACTIVE'    (имя константы)
print(status.value)   # 'active'    (значение)

if status == Status.ACTIVE:
    print("ok")
```

## Создание из значения

```python
Status("active")      # Status.ACTIVE
Status("blocked")     # Status.BLOCKED
Status("unknown")     # ValueError!
```

## Перебор

```python
for s in Status:
    print(s.name, "=", s.value)
```

## Когда использовать `Enum`

- Фиксированный набор статусов / ролей / категорий.
- Режимы работы.
- Типы событий.

## Почему `Enum` лучше «магических строк»

Сравни:

```python
# плохо
if user.role == "admin":
    ...
if user.role == "Admin":     # опечатка — баг!
    ...

# хорошо
if user.role == Role.ADMIN:
    ...
```

- IDE подсказывает значения.
- Опечатка ловится сразу (`AttributeError`).
- Все возможные значения видны в одном месте.

## `IntEnum` и `StrEnum`

Если нужно, чтобы значение вело себя как `int` или `str`:

```python
from enum import IntEnum, StrEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 5
    HIGH = 10

Priority.HIGH > Priority.LOW   # True
```

`StrEnum` появился в Python 3.11.
