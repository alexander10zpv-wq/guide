"""
Урок 3. Строки str.
Заполни места, помеченные //TODO.
"""


def normalize_email(email):
    """Привести email к нижнему регистру и убрать пробелы по краям."""
    # //TODO 1
    return email.strip().lower()
 

def greet(name):
    """Вернуть строку: 'Привет, <name>!'"""
    # //TODO 2
    return f"Привет, {name}!"


def count_words(text):
    """Вернуть число слов в строке."""
    # //TODO 3
    return len(text.split())


def is_palindrome(text):
    """Вернуть True, если text — палиндром (без учёта регистра и пробелов)."""
    # //TODO 4
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]


def mask_card(card_number):
    """
    Принимает строку из 16 цифр.
    Возвращает первые 4 + 8 '*' + последние 4.
    Пример: '1234123412341234' -> '1234********1234'
    """
    # //TODO 5
    return None


if __name__ == "__main__":
    print(normalize_email("  TEST@example.COM  "))
    print(greet("Alex"))
    print(count_words("hello   world  python"))
    print(is_palindrome("А роза упала на лапу Азора"))
    print(mask_card("1234567812345678"))
