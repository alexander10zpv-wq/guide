"""
Проверка задачи урока 3.
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

    def check_normalize_email():
        assert task.normalize_email("  TEST@example.COM  ") == "test@example.com"
        assert task.normalize_email("a@b.ru") == "a@b.ru"
        assert task.normalize_email("\tFoo@Bar.com\n") == "foo@bar.com"

    def check_greet():
        assert task.greet("Alex") == "Привет, Alex!"
        assert task.greet("Маша") == "Привет, Маша!"

    def check_count_words():
        assert task.count_words("hello world") == 2
        assert task.count_words("   hello   world  python  ") == 3
        assert task.count_words("") == 0
        assert task.count_words("one") == 1

    def check_is_palindrome():
        assert task.is_palindrome("level") is True
        assert task.is_palindrome("Level") is True
        assert task.is_palindrome("А роза упала на лапу Азора") is True
        assert task.is_palindrome("hello") is False
        assert task.is_palindrome("") is True

    def check_mask_card():
        assert task.mask_card("1234567812345678") == "1234********5678"
        assert task.mask_card("0000111122223333") == "0000********3333"

    results.append(run_check("normalize_email", check_normalize_email))
    results.append(run_check("greet", check_greet))
    results.append(run_check("count_words", check_count_words))
    results.append(run_check("is_palindrome", check_is_palindrome))
    results.append(run_check("mask_card", check_mask_card))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
