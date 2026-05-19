# Задача урока 15

Открой [task.py](task.py) и выполни все `//TODO`.

## Что нужно сделать

1. Создай `@dataclass User` с полями: `id: int`, `name: str`, `email: str`, `is_admin: bool = False`.
2. Создай `@dataclass(frozen=True) Point` с полями `x: int`, `y: int`.
3. Реализуй метод `User.full_info()` — вернуть строку вида `"#1 Alex (alex@example.com)"`.
4. Реализуй функцию `make_admin(user)` — принимает `User`, возвращает **нового** `User` с `is_admin=True` (исходный не менять). Используй `dataclasses.replace`.
5. Реализуй функцию `distance(p1, p2)` — расстояние между двумя `Point` (евклидово, `((x1-x2)**2 + (y1-y2)**2) ** 0.5`).

## Как запускать и проверять

1. Открой терминал (`Ctrl + ~`).
2. `cd lesson_15_dataclass`
3. `python check.py`
