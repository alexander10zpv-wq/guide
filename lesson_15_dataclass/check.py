"""
Проверка задачи урока 15.
Запуск:  python check.py
"""

import sys
import traceback
from dataclasses import is_dataclass, fields, FrozenInstanceError


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
        assert is_dataclass(task.User), "User должен быть dataclass"
        names = {f.name for f in fields(task.User)}
        assert names == {"id", "name", "email", "is_admin"}, \
            f"ожидались поля id,name,email,is_admin; получили {names}"
        u = task.User(1, "Alex", "alex@example.com")
        assert u.is_admin is False, "по умолчанию is_admin должен быть False"

    def check_point_frozen():
        assert is_dataclass(task.Point), "Point должен быть dataclass"
        names = {f.name for f in fields(task.Point)}
        assert names == {"x", "y"}
        p = task.Point(1, 2)
        try:
            p.x = 99
            raise AssertionError("Point должен быть frozen, но изменение прошло")
        except FrozenInstanceError:
            pass

    def check_full_info():
        u = task.User(1, "Alex", "alex@example.com")
        info = u.full_info()
        assert info == "#1 Alex (alex@example.com)", f"получили {info!r}"

    def check_make_admin():
        u = task.User(1, "Alex", "alex@example.com")
        new_u = task.make_admin(u)
        assert new_u.is_admin is True, "новый user должен быть admin"
        assert u.is_admin is False, "исходный user не должен меняться"
        assert new_u is not u, "должен быть НОВЫЙ объект"
        assert new_u.name == "Alex"

    def check_distance():
        p1 = task.Point(0, 0)
        p2 = task.Point(3, 4)
        d = task.distance(p1, p2)
        assert abs(d - 5.0) < 1e-9, f"ожидалось 5.0, получили {d}"
        assert task.distance(task.Point(1, 1), task.Point(1, 1)) == 0

    results.append(run_check("User dataclass", check_user))
    results.append(run_check("Point frozen", check_point_frozen))
    results.append(run_check("full_info", check_full_info))
    results.append(run_check("make_admin", check_make_admin))
    results.append(run_check("distance", check_distance))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
