"""
Проверка задачи урока 2.
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

    def check_vars():
        assert task.is_admin is True, f"is_admin должен быть True, а равен {task.is_admin}"
        assert task.is_blocked is False, f"is_blocked должен быть False, а равен {task.is_blocked}"

    def check_can_login():
        assert task.can_login(True, False) is True, "активный незаблокированный -> True"
        assert task.can_login(True, True) is False, "активный, но заблокированный -> False"
        assert task.can_login(False, False) is False, "неактивный -> False"
        assert task.can_login(False, True) is False, "неактивный и заблокированный -> False"

    def check_is_adult():
        assert task.is_adult(18) is True, "18 -> True"
        assert task.is_adult(17) is False, "17 -> False"
        assert task.is_adult(0) is False, "0 -> False"
        assert task.is_adult(99) is True, "99 -> True"

    def check_is_empty_name():
        assert task.is_empty_name("") is True, "'' -> True"
        assert task.is_empty_name("   ") is True, "'   ' -> True"
        assert task.is_empty_name("Alex") is False, "'Alex' -> False"
        assert task.is_empty_name("  Alex  ") is False, "'  Alex  ' -> False"

    results.append(run_check("is_admin / is_blocked", check_vars))
    results.append(run_check("can_login", check_can_login))
    results.append(run_check("is_adult", check_is_adult))
    results.append(run_check("is_empty_name", check_is_empty_name))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
