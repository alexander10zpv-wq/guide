# Курс по типам данных в Python

Курс построен по материалу [python_data_types_full_guide.txt](python_data_types_full_guide.txt). Каждый урок — отдельная папка, в которой ты найдёшь:

| Файл         | Что внутри |
|--------------|------------|
| `theory.md`  | Краткая теория, которую нужно прочитать перед заданием |
| `task.md`    | Условие практической задачи |
| `task.py`    | Заготовка кода с метками `//TODO` — туда ты пишешь решение |
| `check.py`   | Скрипт-проверщик с базовой обработкой ошибок |

## Структура курса

1. [lesson_01_intro_and_numbers](lesson_01_intro_and_numbers/) — Что такое типы данных, `int`, `float`, `complex`
2. [lesson_02_bool](lesson_02_bool/) — Логический тип `bool`
3. [lesson_03_strings](lesson_03_strings/) — Строки `str`
4. [lesson_04_lists](lesson_04_lists/) — Списки `list`
5. [lesson_05_tuples_and_range](lesson_05_tuples_and_range/) — Кортежи `tuple` и `range`
6. [lesson_06_dicts](lesson_06_dicts/) — Словари `dict`
7. [lesson_07_sets](lesson_07_sets/) — Множества `set` и `frozenset`
8. [lesson_08_bytes](lesson_08_bytes/) — Бинарные типы `bytes`, `bytearray`, `memoryview`
9. [lesson_09_none](lesson_09_none/) — Тип `NoneType`
10. [lesson_10_decimal_fraction](lesson_10_decimal_fraction/) — `Decimal` и `Fraction`
11. [lesson_11_datetime](lesson_11_datetime/) — Даты и время
12. [lesson_12_enum](lesson_12_enum/) — Перечисления `Enum`
13. [lesson_13_pathlib](lesson_13_pathlib/) — Работа с путями `pathlib.Path`
14. [lesson_14_collections](lesson_14_collections/) — `deque`, `Counter`, `defaultdict`, `namedtuple`
15. [lesson_15_dataclass](lesson_15_dataclass/) — `dataclass`
16. [lesson_16_typing](lesson_16_typing/) — Аннотации типов `typing`
17. [lesson_17_choosing_types](lesson_17_choosing_types/) — Какой тип выбрать в разных ситуациях
18. [final_test](final_test/) — Контрольная работа по всему материалу

## Как работать с курсом

1. Открой папку нужного урока.
2. Прочитай `theory.md`.
3. Прочитай условие в `task.md`.
4. Открой `task.py` и заполни код в местах, помеченных `//TODO`.
5. Сохрани файл (`Ctrl+S`).
6. Запусти `check.py` (см. инструкцию ниже).
7. Если проверка прошла — переходи к следующему уроку. Если нет — читай сообщение об ошибке и исправляй.

## Как запускать код в VSCode

**Способ 1 — Через интерфейс:**
- Открой нужный `.py` файл.
- Нажми на треугольник ▶ в правом верхнем углу окна (кнопка «Run Python File»).

**Способ 2 — Через терминал VSCode (рекомендуется для `check.py`):**
- Открой терминал: `Ctrl + ~` (или меню `Terminal → New Terminal`).
- Перейди в папку урока:
  ```powershell
  cd lesson_01_intro_and_numbers
  ```
- Запусти проверку:
  ```powershell
  python check.py
  ```

**Способ 3 — Горячие клавиши:**
- Открой нужный файл и нажми `F5` (запуск с отладкой) или `Ctrl + F5` (без отладки).

> Если `python` не найден — установи [Python](https://www.python.org/downloads/) и расширение **Python** в VSCode (Microsoft).
