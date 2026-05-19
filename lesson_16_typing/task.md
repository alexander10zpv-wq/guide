# Задача урока 16

Открой [task.py](task.py) и выполни все `//TODO`.

> В этом уроке проверка смотрит и логику, и сами **аннотации типов** функций.

## Что нужно сделать

1. Реализуй `add(a: int, b: int) -> int` — вернуть сумму.
2. Реализуй `find_first(items: list[int], value: int) -> int | None` — индекс первого вхождения или `None`.
3. Реализуй `get_name(user: dict[str, str]) -> str` — вернуть значение по ключу `"name"`.
4. Реализуй `set_mode(mode: Literal["read", "write", "append"]) -> str` — вернуть строку `f"mode: {mode}"`.
5. Создай `TypedDict` `UserDict` с полями `name: str`, `age: int`. И функцию `make_user(name: str, age: int) -> UserDict`, возвращающую `dict` с этими полями.

## Как запускать и проверять

1. Открой терминал (`Ctrl + ~`).
2. `cd lesson_16_typing`
3. `python check.py`
