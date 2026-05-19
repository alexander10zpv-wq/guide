# Урок 10. `Decimal` и `Fraction`

`float` подходит для приблизительных расчётов, но не для денег:

```python
print(0.1 + 0.2)   # 0.30000000000000004
```

Для точных вычислений в Python есть `Decimal` и `Fraction`.

## `Decimal` — точные десятичные числа

```python
from decimal import Decimal

price = Decimal("19.99")
tax = Decimal("0.20")
total = price + price * tax
print(total)   # 23.9880
```

### Важно: передавай строку, а не `float`!

```python
Decimal("0.1") + Decimal("0.2")   # Decimal('0.3')  правильно
Decimal(0.1) + Decimal(0.2)       # уже искажено!
```

### Когда использовать

- Деньги, бухгалтерия, платежи.
- Любые точные финансовые расчёты.
- Когда важно округление по правилам.

### Округление

```python
from decimal import Decimal, ROUND_HALF_UP

x = Decimal("2.5555")
x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
# Decimal('2.56')
```

## `Fraction` — рациональные дроби

```python
from fractions import Fraction

x = Fraction(1, 3)
y = Fraction(1, 6)
print(x + y)   # 1/2
```

### Когда использовать

- Точная математика без потери точности.
- Задачи с дробями (физика, химия, учебные алгоритмы).

### Из десятичной строки

```python
Fraction("0.25")    # Fraction(1, 4)
Fraction(3, 4)      # 3/4
```

## Сравнение

| Тип       | Когда |
|-----------|-------|
| `int`     | Целые значения, копейки/центы |
| `float`   | Приблизительные расчёты, физика |
| `Decimal` | Деньги, бухгалтерия, точная десятичная арифметика |
| `Fraction`| Точные дроби, математические задачи |
