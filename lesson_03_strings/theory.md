# Урок 3. Строки `str`

`str` — это текстовый тип данных.

```python
name = "Alex"
email = "test@example.com"
message = "Привет"
```

Python использует Unicode — строки работают с русским, английским, эмодзи:

```python
text = "Привет, мир 👋"
```

## Когда использовать

- Имена, email, URL.
- Сообщения, JSON-ключи, логи.
- Любые текстовые данные.

## Строки **неизменяемые**

Метод не меняет строку, а возвращает новую:

```python
text = "hello"
new_text = text.upper()

print(text)      # hello
print(new_text)  # HELLO
```

## Создание строк

```python
single = 'одинарные кавычки'
double = "двойные кавычки"
multi = """многострочная
строка"""
fstring = f"Привет, {name}!"  # подставит значение переменной
```

## Полезные методы

```python
s = "  Hello, World!  "

s.strip()           # "Hello, World!"  — убирает пробелы
s.lower()           # "  hello, world!  "
s.upper()           # "  HELLO, WORLD!  "
s.replace("l", "L") # "  HeLLo, WorLd!  "
s.split(",")        # ['  Hello', ' World!  ']
",".join(["a", "b"])# "a,b"
s.startswith("  H") # True
s.endswith("!  ")   # True
len(s)              # 17
"World" in s        # True
```

## Индексы и срезы

Как в списках — индексация с `0`, поддерживает срезы:

```python
text = "Python"
text[0]     # 'P'
text[-1]    # 'n'  (последний символ)
text[0:3]   # 'Pyt'
text[::-1]  # 'nohtyP'  (переворот строки)
```

## Форматирование (f-strings)

```python
name = "Alex"
age = 25
print(f"{name} - {age} лет")            # Alex - 25 лет
print(f"{3.14159:.2f}")                  # 3.14
print(f"{42:05d}")                       # 00042 (5 цифр с ведущими нулями)
```
