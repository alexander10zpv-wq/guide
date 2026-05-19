"""
Урок 13. pathlib.Path.
Заполни места, помеченные //TODO.
"""

from pathlib import Path


def build_path(parent, name):
    """Вернуть Path = parent / name."""
    # //TODO 1
    return None


def get_extension(path):
    """Вернуть расширение файла (например '.txt')."""
    # //TODO 2
    return None


def change_extension(path, new_ext):
    """Заменить расширение и вернуть новый Path."""
    # //TODO 3
    return None


def write_and_read(path, text):
    """Записать text в файл (utf-8) и прочитать его обратно."""
    # //TODO 4
    return None


def safe_read(path):
    """Прочитать файл или вернуть '', если его нет."""
    # //TODO 5
    return None


if __name__ == "__main__":
    print(build_path("docs", "file.txt"))
    print(get_extension(Path("report.pdf")))
    print(change_extension(Path("a.txt"), ".md"))
