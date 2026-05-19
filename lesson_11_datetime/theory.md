# Урок 11. Даты и время: `datetime`, `date`, `time`, `timedelta`

Все типы лежат в модуле `datetime`.

```python
from datetime import datetime, date, time, timedelta
```

## `datetime` — момент времени (дата + время)

```python
now = datetime.now()
print(now)   # 2026-05-19 14:30:00.123456

birthday = datetime(2000, 1, 15, 12, 0, 0)
```

## `date` — только дата (без времени)

```python
today = date.today()
my_date = date(2026, 5, 19)
```

## `time` — только время суток

```python
t = time(14, 30, 0)
```

## `timedelta` — промежуток времени

```python
delta = timedelta(days=7, hours=3)
tomorrow = datetime.now() + timedelta(days=1)
```

Можно вычитать даты и получать `timedelta`:

```python
d1 = date(2026, 5, 19)
d2 = date(2026, 5, 1)
diff = d1 - d2
print(diff.days)   # 18
```

## Форматирование

`strftime` — дата → строка (по шаблону):

```python
now.strftime("%Y-%m-%d %H:%M:%S")   # 2026-05-19 14:30:00
now.strftime("%d.%m.%Y")            # 19.05.2026
```

Основные коды:

| Код  | Значение            |
|------|---------------------|
| `%Y` | год (4 цифры)       |
| `%m` | месяц (01-12)       |
| `%d` | день (01-31)        |
| `%H` | часы (00-23)        |
| `%M` | минуты (00-59)      |
| `%S` | секунды (00-59)     |

## Парсинг строки

`strptime` — строка → дата:

```python
datetime.strptime("2026-05-19", "%Y-%m-%d")
# datetime(2026, 5, 19, 0, 0)
```

## Когда что использовать

- Даты, дедлайны, расписания — `date`.
- События, логи, метки времени — `datetime`.
- Промежутки, «через N дней» — `timedelta`.
