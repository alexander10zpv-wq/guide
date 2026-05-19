# Урок 13. Работа с путями — `pathlib.Path`

`Path` — современный объектно-ориентированный способ работать с путями к файлам и папкам. Работает одинаково на Windows / Linux / macOS.

```python
from pathlib import Path
```

## Создание пути

```python
p = Path("data/file.txt")
p = Path("data") / "file.txt"   # удобный оператор / для объединения
```

## Полезные атрибуты

```python
p = Path("/home/user/docs/report.pdf")

p.name          # 'report.pdf'
p.stem          # 'report'           (имя без расширения)
p.suffix        # '.pdf'             (расширение)
p.parent        # Path('/home/user/docs')
p.parts         # ('/', 'home', 'user', 'docs', 'report.pdf')
```

## Проверки

```python
p.exists()      # существует ли путь
p.is_file()     # это файл?
p.is_dir()      # это папка?
```

## Операции с файлами

```python
p = Path("hello.txt")

p.write_text("Привет", encoding="utf-8")
content = p.read_text(encoding="utf-8")

# для бинарных данных
p.write_bytes(b"...")
data = p.read_bytes()
```

## Папки и обход

```python
docs = Path("docs")
docs.mkdir(parents=True, exist_ok=True)   # создать (с родительскими)

for file in docs.iterdir():
    print(file)

for py_file in docs.glob("*.py"):
    print(py_file)

for any_py in docs.rglob("*.py"):   # рекурсивно
    print(any_py)
```

## Изменение имени / расширения

```python
p = Path("report.txt")
p.with_name("summary.txt")   # Path('summary.txt')
p.with_suffix(".md")         # Path('report.md')
```

## Зачем `Path` вместо строк

- Кроссплатформенно (`/` и `\` решаются автоматически).
- Удобный оператор `/` для соединения.
- Сразу много методов: `exists`, `read_text`, `iterdir`, ...
- Меньше места для опечаток.
