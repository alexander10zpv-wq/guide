"""
Урок 2. Логический тип bool.
Заполни места, помеченные //TODO.
"""

# //TODO 1: Создай переменные
is_admin = None
is_blocked = None


def can_login(is_active, is_blocked):
    """Вернуть True, если пользователь активен и НЕ заблокирован."""
    # //TODO 2
    return None


def is_adult(age):
    """Вернуть True, если age >= 18."""
    # //TODO 3
    return None


def is_empty_name(name):
    """Вернуть True, если name пустая или только пробелы."""
    # //TODO 4
    return None


if __name__ == "__main__":
    print("is_admin =", is_admin)
    print("is_blocked =", is_blocked)
    print("can_login(True, False) =", can_login(True, False))
    print("is_adult(20) =", is_adult(20))
    print("is_empty_name('   ') =", is_empty_name("   "))
