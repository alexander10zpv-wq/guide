"""
Проверка задачи урока 16.
Запуск:  python check.py

Проверяются и логика, и аннотации типов (через __annotations__ и get_type_hints).
"""

import sys
import traceback
import typing


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

    def check_add():
        hints = typing.get_type_hints(task.add)
        assert hints.get("a") is int and hints.get("b") is int and hints.get("return") is int, \
            f"add должна иметь аннотации int, int -> int; получили {hints}"
        assert task.add(1, 2) == 3
        assert task.add(-1, 1) == 0

    def check_find_first():
        hints = typing.get_type_hints(task.find_first)
        # допускаем list[int] или typing.List[int]; в hints это list[int]
        assert "items" in hints and "value" in hints and "return" in hints, \
            f"find_first нужны аннотации items, value, return; получили {hints}"
        assert hints["value"] is int
        # return должен быть Optional[int] = int | None
        ret = hints["return"]
        assert int in typing.get_args(ret) and type(None) in typing.get_args(ret), \
            f"return должен быть int | None, получили {ret}"
        assert task.find_first([1, 2, 3], 2) == 1
        assert task.find_first([1, 2, 3], 999) is None
        assert task.find_first([], 1) is None

    def check_get_name():
        hints = typing.get_type_hints(task.get_name)
        assert hints.get("return") is str, f"get_name -> str, получили {hints.get('return')}"
        assert task.get_name({"name": "Alex"}) == "Alex"

    def check_set_mode():
        hints = typing.get_type_hints(task.set_mode)
        assert hints.get("return") is str
        # тип mode должен быть Literal['read','write','append']
        mode_t = hints.get("mode")
        assert typing.get_origin(mode_t) is typing.Literal, \
            f"mode должен быть Literal[...], получили {mode_t}"
        assert set(typing.get_args(mode_t)) == {"read", "write", "append"}, \
            f"Literal должен содержать read/write/append; получили {typing.get_args(mode_t)}"
        assert task.set_mode("read") == "mode: read"
        assert task.set_mode("write") == "mode: write"

    def check_user_dict():
        # UserDict — это TypedDict; у него есть __annotations__
        assert hasattr(task, "UserDict"), "Должен быть UserDict"
        ann = getattr(task.UserDict, "__annotations__", {})
        assert ann.get("name") is str and ann.get("age") is int, \
            f"UserDict должен иметь name: str, age: int; получили {ann}"
        u = task.make_user("Alex", 25)
        assert u == {"name": "Alex", "age": 25}, f"получили {u}"
        hints = typing.get_type_hints(task.make_user)
        assert hints.get("name") is str and hints.get("age") is int

    results.append(run_check("add", check_add))
    results.append(run_check("find_first", check_find_first))
    results.append(run_check("get_name", check_get_name))
    results.append(run_check("set_mode", check_set_mode))
    results.append(run_check("UserDict / make_user", check_user_dict))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
