"""
Проверка задачи урока 6.
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

    def check_user():
        assert isinstance(task.user, dict), "user должен быть dict"
        assert task.user == {"name": "Alex", "age": 25, "email": "alex@example.com"}

    def check_get_field():
        d = {"a": 1, "b": 2}
        assert task.get_field(d, "a") == 1
        assert task.get_field(d, "missing") is None

    def check_set_field():
        d = {}
        result = task.set_field(d, "x", 10)
        assert result == {"x": 10}, f"ожидалось {{'x': 10}}, получили {result}"

    def check_merge_dicts():
        a = {"a": 1, "b": 2}
        b = {"b": 99, "c": 3}
        merged = task.merge_dicts(a, b)
        assert merged == {"a": 1, "b": 99, "c": 3}, f"получили {merged}"
        # исходные не должны меняться
        assert a == {"a": 1, "b": 2}, "исходный a не должен меняться!"
        assert b == {"b": 99, "c": 3}, "исходный b не должен меняться!"

    def check_count_chars():
        assert task.count_chars("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
        assert task.count_chars("") == {}
        assert task.count_chars("aaa") == {"a": 3}

    def check_invert_dict():
        assert task.invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
        assert task.invert_dict({}) == {}

    results.append(run_check("user", check_user))
    results.append(run_check("get_field", check_get_field))
    results.append(run_check("set_field", check_set_field))
    results.append(run_check("merge_dicts", check_merge_dicts))
    results.append(run_check("count_chars", check_count_chars))
    results.append(run_check("invert_dict", check_invert_dict))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
