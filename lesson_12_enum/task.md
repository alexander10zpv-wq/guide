# Задача урока 12

Открой [task.py](task.py) и выполни все `//TODO`.

## Что нужно сделать

1. Создай `OrderStatus(Enum)` со значениями: `NEW = "new"`, `PAID = "paid"`, `SHIPPED = "shipped"`, `CANCELLED = "cancelled"`.
2. Реализуй `status_label(status)` — принимает `OrderStatus`. Вернуть значение (`.value`).
3. Реализуй `parse_status(text)` — принимает строку. Вернуть соответствующий `OrderStatus` или `None`, если значение неизвестно (без падения).
4. Реализуй `is_finalized(status)` — вернуть `True`, если статус `SHIPPED` или `CANCELLED`.
5. Реализуй `all_statuses()` — вернуть **список** всех значений `OrderStatus` в порядке объявления: `["new", "paid", "shipped", "cancelled"]`.

## Как запускать и проверять

1. Открой терминал (`Ctrl + ~`).
2. `cd lesson_12_enum`
3. `python check.py`
