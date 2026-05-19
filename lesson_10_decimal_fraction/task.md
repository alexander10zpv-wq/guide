# Задача урока 10

Открой [task.py](task.py) и выполни все `//TODO`.

## Что нужно сделать

1. Реализуй `add_money(a, b)` — принимает строки вида `"19.99"`. Возвращает `Decimal`-сумму. Подсказка: преобразуй обе строки в `Decimal` и сложи.
2. Реализуй `apply_tax(price, tax_rate)` — оба аргумента — строки. Вернуть `Decimal` = `price + price * tax_rate`, округлённое до 2 знаков (`ROUND_HALF_UP`).
3. Реализуй `add_fractions(a_num, a_den, b_num, b_den)` — вернуть `Fraction` = сумма двух дробей.
4. Реализуй `is_exact_third(x)` — принимает `Fraction`. Вернуть `True`, если значение равно `1/3`.
5. Реализуй `cents_total(prices)` — принимает список строк `["1.99", "2.50", ...]`. Вернуть `Decimal`-сумму всех значений.

## Как запускать и проверять

1. Открой терминал (`Ctrl + ~`).
2. `cd lesson_10_decimal_fraction`
3. `python check.py`
