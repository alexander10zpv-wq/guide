"""
Проверка задачи урока 13.
Запуск:  python check.py
"""

import sys
import tempfile
import traceback
from pathlib import Path


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

    def check_build_path():
        r = task.build_path("docs", "file.txt")
        assert isinstance(r, Path), f"должно быть Path, а {type(r).__name__}"
        # сравним по частям, чтобы не зависеть от разделителя ОС
        assert r == Path("docs") / "file.txt"

    def check_get_extension():
        assert task.get_extension(Path("report.pdf")) == ".pdf"
        assert task.get_extension(Path("script.py")) == ".py"
        assert task.get_extension(Path("noext")) == ""

    def check_change_extension():
        r = task.change_extension(Path("a.txt"), ".md")
        assert isinstance(r, Path)
        assert r == Path("a.md"), f"получили {r}"

    def check_write_and_read():
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "test.txt"
            result = task.write_and_read(p, "Привет")
            assert result == "Привет", f"получили {result!r}"
            assert p.exists()

    def check_safe_read():
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "nope.txt"
            assert task.safe_read(missing) == ""
            existing = Path(tmp) / "exists.txt"
            existing.write_text("hello", encoding="utf-8")
            assert task.safe_read(existing) == "hello"

    results.append(run_check("build_path", check_build_path))
    results.append(run_check("get_extension", check_get_extension))
    results.append(run_check("change_extension", check_change_extension))
    results.append(run_check("write_and_read", check_write_and_read))
    results.append(run_check("safe_read", check_safe_read))

    print()
    if all(results):
        print("Все задачи выполнены верно!")
    else:
        passed = sum(results)
        print(f"Пройдено {passed} из {len(results)} проверок.")
        sys.exit(1)


if __name__ == "__main__":
    main()
