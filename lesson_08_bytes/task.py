"""
Урок 8. Бинарные типы.
Заполни места, помеченные //TODO.
"""


def to_bytes(text):
    """Закодировать строку в bytes через UTF-8."""
    # //TODO 1
    return None


def from_bytes(data):
    """Раскодировать bytes -> str через UTF-8."""
    # //TODO 2
    return None


def replace_first_byte(data, new_byte):
    """Вернуть новый bytes с заменённым первым байтом."""
    # //TODO 3
    return None


def bytes_length(data):
    """Вернуть длину bytes в байтах."""
    # //TODO 4
    return None


def is_ascii(data):
    """Вернуть True, если все байты в data < 128."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print("to_bytes('Hi') =", to_bytes("Hi"))
    print("from_bytes(b'Hi') =", from_bytes(b"Hi"))
    print("replace_first_byte(b'hello', 72) =", replace_first_byte(b"hello", 72))
    print("bytes_length(b'hi') =", bytes_length(b"hi"))
    print("is_ascii(b'abc') =", is_ascii(b"abc"))
