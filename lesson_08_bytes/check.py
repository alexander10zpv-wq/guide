"""
Проверка задачи урока 8.
Запуск:  python check.py
"""

import sys
import traceback


def run_check(name, func):
    try:
        func()
        print(f"[OK]  {name}")
        return True
    except AssertionError as e:
        print(f"[FAIL] {name}: {e}")
    except Exception as e:
        print(f"[ERROR] {name}: {type(e).__name__}: {e}")
        traceback.print_exc()
    return False


def main():
    try:
        import task
    except Exception as e:
        print(f"Не удалось импортировать task.py: {type(e).__name__}: {e}")
        sys.exit(1)

    results = []

    def check_to_bytes():
        r = task.to_bytes("Hi")
        assert isinstance(r, bytes), f"должно быть bytes, а {type(r).__name__}"
        assert r == b"Hi"
        assert task.to_bytes("Привет") == "Привет".encode("utf-8")

    def check_from_bytes():
        assert task.from_bytes(b"Hi") == "Hi"
        assert task.from_bytes("Привет".encode("utf-8")) == "Привет"

    def check_replace_first_byte():
        r = task.replace_first_byte(b"hello", 72)  # 72 = 'H'
        assert isinstance(r, bytes), f"должно быть bytes, а {type(r).__name__}"
        assert r == b"Hello", f"ожидалось b'Hello', получили {r!r}"

    def check_bytes_length():
        assert task.bytes_length(b"hi") == 2
        assert task.bytes_length(b"") == 0
        # русские символы в utf-8 = 2 байта на букву
        assert task.bytes_length("Привет".encode("utf-8")) == 12

    def check_is_ascii():
        assert task.is_ascii(b"abc") is True
        assert task.is_ascii(b"") is True
        assert task.is_ascii("Привет".encode("utf-8")) is False
        assert task.is_ascii(bytes([200, 1, 2])) is False

    results.append(run_check("to_bytes", check_to_bytes))
    results.append(run_check("from_bytes", check_from_bytes))
    results.append(run_check("replace_first_byte", check_replace_first_byte))
    results.append(run_check("bytes_length", check_bytes_length))
    results.append(run_check("is_ascii", check_is_ascii))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
