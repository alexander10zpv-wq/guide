"""
Урок 1. Числовые типы.
Заполни места, помеченные //TODO.
"""

# //TODO 1: Создай переменную age (int) со значением 25
age = None

# //TODO 2: Создай переменную price (float) со значением 19.99
price = None

# //TODO 3: Создай переменную z (complex), равную 3 + 4j
z = None


def rectangle_area(width, height):
    """Возвращает площадь прямоугольника."""
    # //TODO 4: Верни произведение width и height
    return None


def cents_to_dollars(cents):
    """
    Принимает целое число центов (например 1234)
    и возвращает строку вида "12.34".
    """
    # //TODO 5: Раздели cents на доллары и центы и собери строку
    # Подсказка: dollars = cents // 100, remaining_cents = cents % 100
    # Результат: f"{dollars}.{remaining_cents:02d}"
    return None


if __name__ == "__main__":
    print("age =", age)
    print("price =", price)
    print("z =", z)
    print("rectangle_area(3, 4) =", rectangle_area(3, 4))
    print("cents_to_dollars(1234) =", cents_to_dollars(1234))
