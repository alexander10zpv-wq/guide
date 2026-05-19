# Задача — мини-«интернет-магазин»

В этой контрольной ты соберёшь несколько связанных вещей: модели данных, статусы, цены, очередь обработки и сохранение в файл.

Открой [task.py](task.py) и выполни все `//TODO` сверху вниз. Ниже — список того, что должно получиться.

---

## 1. `Enum OrderStatus`
Поля: `NEW = "new"`, `PAID = "paid"`, `SHIPPED = "shipped"`, `CANCELLED = "cancelled"`.

## 2. `@dataclass Product`
Поля: `id: int`, `name: str`, `price: Decimal`, `category: str`.

## 3. `@dataclass Order`
Поля: `id: int`, `items: list[Product]`, `status: OrderStatus = OrderStatus.NEW`, `created_at: datetime` (по умолчанию — `datetime.now()` при создании; используй `field(default_factory=datetime.now)`).

Метод `total(self) -> Decimal` — сумма цен всех `items` (если пусто — `Decimal("0")`).

## 4. Функции

### `find_product(products: list[Product], product_id: int) -> Product | None`
Найти товар по `id` или вернуть `None`.

### `unique_categories(products: list[Product]) -> set[str]`
Множество уникальных категорий.

### `top_categories(products: list[Product], n: int) -> list[str]`
Список из `n` самых частых категорий (через `Counter.most_common`, только названия).

### `process_orders(orders: list[Order]) -> list[int]`
Через `deque`: положить туда все заказы, потом по очереди извлекать слева и возвращать список их `id` в порядке обработки.

### `mark_paid(order: Order) -> Order`
Вернуть **новый** `Order` со статусом `PAID` (исходный не менять). Используй `dataclasses.replace`.

### `format_total(amount: Decimal) -> str`
Округлить `amount` до 2 знаков (`ROUND_HALF_UP`) и вернуть строку вида `"123.45 $"`.

### `safe_get_name(product: Product | None) -> str`
Вернуть `product.name`, либо `"unknown"`, если `product is None`.

### `save_order_summary(path: Path, order: Order) -> None`
Записать в файл `path` строку:
```
Order #<id>, status=<статус как value>, total=<format_total(...)>
```
В кодировке UTF-8.

### `load_order_summary(path: Path) -> str`
Прочитать содержимое файла. Если файла нет — вернуть `""`.

### `encode_summary(text: str) -> bytes`
Закодировать строку в UTF-8.

---

## Как запускать и проверять

1. Открой терминал (`Ctrl + ~`).
2. Перейди в папку:
   ```powershell
   cd final_test
   ```
3. Запусти проверку:
   ```powershell
   python check.py
   ```

Если все 11 проверок пройдены — поздравляем, курс пройден!
