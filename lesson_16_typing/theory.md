# Урок 16. Аннотации типов — `typing`

Аннотации типов **не меняют выполнение** Python, но помогают IDE, линтерам и людям понимать код.

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

## Базовые аннотации

```python
age: int = 25
price: float = 19.99
name: str = "Alex"
is_admin: bool = False

users: list[str] = ["Alex", "Maria"]
point: tuple[int, int] = (1, 2)
user: dict[str, int] = {"age": 25}
ids: set[int] = {1, 2, 3}
```

> В современном Python (3.9+) используй встроенные `list`, `dict`, `set`, `tuple`. Старые `List`, `Dict`, `Set` из `typing` тоже работают, но они устарели.

## `Optional[T]` и `T | None`

«Значение `T` или `None`»:

```python
from typing import Optional

def find_user(uid: int) -> Optional[str]:
    return None

# современная запись (3.10+):
def find_user(uid: int) -> str | None:
    return None
```

## `Union[A, B]` и `A | B`

«Один из нескольких типов»:

```python
from typing import Union

def parse(value: Union[int, str]) -> int:
    ...

# современная запись:
def parse(value: int | str) -> int:
    ...
```

## `Any` — любой тип

```python
from typing import Any

def log(value: Any) -> None:
    print(value)
```

Не злоупотребляй — `Any` фактически отключает типизацию.

## `Literal` — фиксированные значения

```python
from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    ...
```

Линтер подскажет, если передадут `"wrong"`.

## `TypedDict` — структура словаря

```python
from typing import TypedDict

class UserDict(TypedDict):
    name: str
    age: int

user: UserDict = {"name": "Alex", "age": 25}
```

## `Protocol` — описание поведения (duck typing)

```python
from typing import Protocol

class HasName(Protocol):
    name: str

def print_name(obj: HasName) -> None:
    print(obj.name)
```

Подойдёт **любой** объект с атрибутом `name` — даже без наследования.

## `Generic` и `TypeVar` — универсальные типы

```python
from typing import Generic, TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, value: T):
        self.value = value
```

## Зачем оно нужно

- Документация прямо в сигнатуре.
- IDE подсказывает методы, поля, аргументы.
- Линтер (`mypy`, `pyright`) ловит ошибки до запуска.
- Легче поддерживать большой код.
