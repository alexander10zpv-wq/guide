"""
Проверка задачи урока 17.
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


EXPECTED = {
    "answer_money": "Decimal",
    "answer_user_id": "int",
    "answer_coordinates": "tuple",
    "answer_unique_tags": "set",
    "answer_order_status": "Enum",
    "answer_business_user": "dataclass",
    "answer_word_frequency": "Counter",
    "answer_task_queue": "deque",
    "answer_event_timestamp": "datetime",
    "answer_missing_value": "None",
}


def main():
    try:
        import task
    except Exception as e:
        print(f"Не удалось импортировать task.py: {type(e).__name__}: {e}")
        sys.exit(1)

    results = []

    for var_name, expected in EXPECTED.items():
        def make_check(var_name=var_name, expected=expected):
            def _check():
                actual = getattr(task, var_name, None)
                assert isinstance(actual, str) and actual != "", \
                    f"{var_name} должен быть непустой строкой"
                assert actual == expected, \
                    f"{var_name}: ожидалось {expected!r}, получили {actual!r}"
            return _check
        results.append(run_check(var_name, make_check()))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
