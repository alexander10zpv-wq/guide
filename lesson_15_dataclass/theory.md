# Урок 15. `dataclass` — описание структур данных

`dataclass` — удобный способ описать класс-структуру (бизнес-объект, DTO, конфиг). Автоматически генерирует `__init__`, `__repr__`, `__eq__`.

```python
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str

user = User("Alex", 25, "alex@example.com")

print(user)         # User(name='Alex', age=25, email='alex@example.com')
print(user.name)    # 'Alex'
user.age = 26
```

## Когда использовать

- Бизнес-модели (`User`, `Order`, `Product`).
- DTO для передачи между слоями.
- Конфиги, структурированные данные.
- Замена для «больших» dict с фиксированной структурой.

## Чем `dataclass` лучше обычного `dict`

| `dict`                                 | `@dataclass`                           |
|----------------------------------------|----------------------------------------|
| `user["nam"]` — опечатка, `KeyError`   | `user.nam` — линтер поймает сразу      |
| Структура не задана                    | Поля и типы видно в определении        |
| Нет автодополнения                     | IDE подсказывает поля                  |
| Equality сравнивает содержимое         | Сравнение по полям из коробки          |

## Значения по умолчанию

```python
@dataclass
class Config:
    host: str = "localhost"
    port: int = 8080
    debug: bool = False
```

Поля **без значения** должны идти **до** полей **со значением** — как в обычной функции.

## Опции декоратора

```python
@dataclass(frozen=True)   # делает объект неизменяемым
class Point:
    x: int
    y: int

p = Point(1, 2)
p.x = 99    # FrozenInstanceError!
```

```python
@dataclass(order=True)    # добавляет сравнения <, >, <=, >=
class Score:
    value: int
```

## Методы можно добавлять обычным образом

```python
@dataclass
class User:
    name: str
    age: int

    def is_adult(self):
        return self.age >= 18
```

## Когда `dataclass` НЕ нужен

- Когда данные действительно динамические (например, ответ API с произвольными ключами) — используй `dict` или `TypedDict`.
- Когда нужна сложная инициализация с множеством логики — обычный `class`.
