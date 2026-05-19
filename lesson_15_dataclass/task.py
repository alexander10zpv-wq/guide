"""
Урок 15. dataclass.
Заполни места, помеченные //TODO.
"""

from dataclasses import dataclass, replace


# //TODO 1: создай dataclass User c полями id, name, email, is_admin=False
@dataclass
class User:
    pass

    # //TODO 3: метод full_info(self) возвращает "#<id> <name> (<email>)"
    def full_info(self):
        return None


# //TODO 2: создай frozen dataclass Point с полями x, y
@dataclass
class Point:
    pass


def make_admin(user):
    """Вернуть НОВОГО User с is_admin=True."""
    # //TODO 4
    return None


def distance(p1, p2):
    """Евклидово расстояние между двумя Point."""
    # //TODO 5
    return None


if __name__ == "__main__":
    u = User(1, "Alex", "alex@example.com")
    print(u)
    print(u.full_info())
    print(make_admin(u))

    p1 = Point(0, 0)
    p2 = Point(3, 4)
    print(distance(p1, p2))
