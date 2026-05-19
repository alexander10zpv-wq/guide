# Урок 8. Бинарные типы: `bytes`, `bytearray`, `memoryview`

## `bytes` — неизменяемая последовательность байтов

```python
data = b"hello"
print(data)        # b'hello'
print(data[0])     # 104  (код буквы 'h')
```

## Когда использовать

- Чтение/запись файлов в бинарном режиме.
- Сетевые протоколы, HTTP.
- Шифрование, хеширование.
- Изображения, аудио, бинарные форматы.

```python
with open("file.bin", "rb") as f:
    data = f.read()  # bytes
```

## str ↔ bytes

```python
s = "Привет"
b = s.encode("utf-8")   # str -> bytes
print(b)                # b'\xd0\x9f\xd1\x80...'

back = b.decode("utf-8")  # bytes -> str
print(back)               # 'Привет'
```

UTF-8 — кодировка по умолчанию для текста.

## `bytearray` — изменяемая версия `bytes`

```python
data = bytearray(b"hello")
data[0] = 72        # меняем первый байт ('H' = 72)
print(data)         # bytearray(b'Hello')
```

Когда использовать:

- Когда бинарные данные нужно менять «на месте».
- Буферы, парсеры, обработка файлов без копирования.

## `memoryview` — представление без копирования

```python
data = bytearray(b"abcdef")
view = memoryview(data)
print(view[1:3])       # <memory at ...>
print(bytes(view[1:3])) # b'bc'
```

Когда использовать: оптимизация больших бинарных данных. В обычной разработке встречается редко.

## Литералы

```python
b"hello"          # ascii
b"\x48\x69"       # шестнадцатеричные коды (= b"Hi")
bytes([72, 105])  # из списка целых -> b"Hi"
```
