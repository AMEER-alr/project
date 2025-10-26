
## lab01

### ex01

```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![alt text](./images/lab01/image-1.png)





### ex02

```python
numbers = [float(input()),float(input())]
total = sum(numbers)
average = sum(numbers) / len(numbers)
print(total)
print(average)
```

![alt text](./images/lab01/image-2.png)





### ex03

```python
print("enter the price :")
price = float(input())
print("enter the discount % :")
discount = float(input())
print("enter the vat % :")
vat = float(input())
base = price * (1-discount/100)
vat_amount  = base * (vat/100)
total = base + vat_amount
print("the price after discount",f"{base:.2f}")
print("the vat ", f"{vat_amount:.2f}")
print("total", f"{total:.2f}")
```

![alt text](./images/lab01/image-3.png)





## ex04

```python
minutes = int(input())
hh = minutes // 60
mm = minutes % 60
if hh <= 24 :
    print(f"{hh:02d}",f"{mm:02d}",sep=":")
else :
    print("none")
```

![alt text](./images/lab01/image-4.png)





## ex05

```python
ФИО = input()
length1 = len(ФИО.replace(" ", ""))
def get_first_letters(name) :
    words = name.split()
    first_letters = [word[0] for word in words if word]
    return ''.join(first_letters)
print("Инициалы:",get_first_letters(ФИО))
print("Длина (символов):", length1)
```

![alt text](./images/lab01/image-5.png)





## ex06

```python
n = int(input())

on_campus = 0
online = 0

for _ in range(n):
    line = input().split()

    format_type = line[-1]
    
    if format_type == "True":
        on_campus += 1
    else :
        online += 1

print(on_campus, online)
```

 ![alt text](./images/lab01/image-6.png)




 ## lab02

 ## ex01

 ```python
 def min_max(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"{sequence} is not list or tuple")
    
    if len(sequence) == 0:
        raise ValueError("Sequence cannot be empty")
    
    min_val = sequence[0]
    max_val = sequence[0]
    
    for element in sequence:
        if element < min_val:
            min_val = element
        if element > max_val:
            max_val = element
    
    return (min_val, max_val)


def unique_sorted(sequence):
    if not isinstance(sequence, (list, tuple)):
        raise TypeError(f"{sequence} is not list or tuple")
    unique_elements = set(sequence)
    return sorted(unique_elements)


def flatten(matrix):
    if not isinstance(matrix, (list, tuple)):
        raise TypeError(f"{matrix} is not list or tuple")
    
    result = []
    
    for row in matrix:
        if not isinstance(row, (list, tuple)):
            raise TypeError(f"{row} is not list or tuple")
        
        for element in row:
            result.append(element)
    
    return result


print("=== min_max ===")
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
try:
    print(min_max([]))
except ValueError as e:
    print("Error:", e)
print(min_max([1.5, 2, 2.0, -3.1]))

print("\n=== unique_sorted ===")
print(unique_sorted([3, 1, 2, 2, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print("\n=== flatten ===")
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], [3, 4, 5]]))
print(flatten([[1], [], [2, 3]]))
try:
    print(flatten([[1, 2], "ab"]))
except TypeError as e:
    print("Error:", e)
```

![alt text](./images/lab02/image-01-(2).png)





## ex02

```python
def transpose(mat):
    if not isinstance(mat, list):
        raise TypeError("Input must be a list")
    
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("All elements must be lists")
        if len(row) != row_length:
            raise ValueError("Jagged matrix is not allowed")
    
    transposed = []
    for col_index in range(len(mat[0])):
        new_row = []
        for row_index in range(len(mat)):
            new_row.append(mat[row_index][col_index])
        transposed.append(new_row)
    
    return transposed


def row_sums(mat):
    if not isinstance(mat, list):
        raise TypeError("Input must be a list")
    
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("All elements must be lists")
        if len(row) != row_length:
            raise ValueError("Jagged matrix is not allowed")
    
    sums = []
    for row in mat:
        row_sum = 0
        for element in row:
            row_sum += element
        sums.append(row_sum)
    
    return sums


def col_sums(mat):
    if not isinstance(mat, list):
        raise TypeError("Input must be a list")
    
    if len(mat) == 0:
        return []
    
    row_length = len(mat[0])
    for row in mat:
        if not isinstance(row, list):
            raise TypeError("All elements must be lists")
        if len(row) != row_length:
            raise ValueError("Jagged matrix is not allowed")
    
    sums = []
    for col_index in range(len(mat[0])):
        col_sum = 0
        for row_index in range(len(mat)):
            col_sum += mat[row_index][col_index]
        sums.append(col_sum)
    
    return sums

print("=== transpose ===")
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
try:
    print(transpose([[1, 2], [3]]))
except ValueError as e:
    print("Error:", e)
    
print("\n=== row_sums ===")
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
try:
    print(row_sums([[1, 2], [3]]))
except ValueError as e:
    print("Error:", e)
    
print("\n=== col_sums ===")
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
try:
    print(col_sums([[1, 2], [3]]))
except ValueError as e:
    print("Error:", e)
```

![alt text](./images/lab02/image-02-(2).png)





## ex03

```python
def format_record(rec):
    if not isinstance(rec, tuple):
        raise TypeError("Input must be a tuple")
    
    if len(rec) != 3:
        raise ValueError("Tuple must have exactly 3 elements")
    
    ФИО, group, gpa = rec
    
    if not isinstance(ФИО, str):
        raise TypeError("ФИО must be a string")
    if not isinstance(group, str):
        raise TypeError("Group must be a string")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA must be a number")
    
    ФИО = ФИО.strip()
    if not ФИО:
        raise ValueError("ФИО cannot be empty")
    
    group = group.strip()
    if not group:
        raise ValueError("Group cannot be empty")
    
    if gpa < 0:
        raise ValueError("GPA cannot be negative")
    
    names = [name.strip() for name in ФИО.split() if name.strip()]
    
    if len(names) < 2:
        raise ValueError("ФИО must contain at least last name and first name")
    
    last_name = names[0]
    first_names = names[1:]
    
    initials = '.'.join(name[0].upper() for name in first_names) + '.'
    
    formatted_gpa = f"{gpa:.2f}"
    
    result = f"{last_name} {initials}, гр. {group}, GPA {formatted_gpa}"
    
    return result


print("=== format_record ===")
    
print(format_record(("Иванов Иван Иванович", "БИВТ-25", 4.6)))
    
print(format_record(("Петров Пётр", "IKB0-12", 5.0)))
    
print(format_record(("Петров Пётр Петрович", "IKB0-12", 5.0)))
    
print(format_record(("Сидорова анна аергеевна", "АВВ-01", 3.999)))
    
try:
    print(format_record(("", "БИВТ-25", 4.5)))
except ValueError as e:
    print("Error:", e)
    
try:
    print(format_record(("Иванов", "БИВТ-25", 4.5)))
except ValueError as e:
    print("Error:", e)
    
try:
    print(format_record(("Иванов Иван", "", 4.5)))
except ValueError as e:
    print("Error:", e)
    
try:
    print(format_record(("Иванов Иван", "БИВТ-25", -1.0)))
except ValueError as e:
    print("Error:", e)


```
![alt text](images/lab02/image-03-(2).png)




## lab04

## ex01
```python
from pathlib import Path
import csv
from typing import Union, Tuple, List


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    path = Path(path)
    
    with open(path, 'r', encoding=encoding) as file:
        content = file.read()
    
    return content


def write_csv(rows: List[Union[tuple, list]], path: Union[str, Path], 
              header: Tuple[str, ...] = None) -> None:
    path = Path(path)
    ensure_parent_dir(path)
    
    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_length}")
    
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        
        if header is not None:
            writer.writerow(header)
        
        writer.writerows(rows)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    path = Path(path)
    parent_dir = path.parent
    parent_dir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    try:
        txt = read_text("data/lab04/input.txt")
        print(f"File content: '{txt}'")
        print(f"Content length: {len(txt)}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        write_csv([("word", "count"), ("test", "3")], "data/lab04/check.csv")
        print("check.csv created successfully")
    except Exception as e:
        print(f"Error: {e}")


```
![alt text](images/lab04/image-01-(4)(1).png)


![alt text](images/lab04/image-01-(4)(2).png)


![alt text](images/lab04/image-01-(4)(3).png)





## ex02
```python
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Tuple
from collections import Counter
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

try:
    from scr.lab04.io_txt_csv import read_text, write_csv
    from scr.lib.text import normalize, tokenize, count_freq
except ImportError as e:
    print(f"wrong while import: {e}")
    print("make sure that the file is exist scr/lib/text.py")
    sys.exit(1)


def top_n(frequency_data: Dict[str, int], limit: int = 5) -> List[Tuple[str, int]]:
    items_list = [(word, count) for word, count in frequency_data.items()]
    items_list.sort(key=lambda item: (-item[1], item[0]))
    return items_list[:limit]


def process_text(text: str) -> Dict[str, int]:
    normalized = normalize(text, casefold=True, yo_to_e=True)
    tokens = tokenize(normalized)
    return count_freq(tokens)


def print_summary(word_freq: Dict[str, int], total_words: int):
    unique_words = len(word_freq)
    top_words = top_n(word_freq, len(word_freq))
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ:")
    for word, count in top_words:
        print(f"{word}:{count}")


def print_pretty_table(word_freq: Dict[str, int]):
    top_words = top_n(word_freq, len(word_freq))

    max_word_len = max(len(word) for word in word_freq.keys())
    max_count_len = max(len(str(count)) for count in word_freq.values())
    
    word_width = max(max_word_len, len("Слово"))
    count_width = max(max_count_len, len("Частота"))

    print("\n" + "=" * (word_width + count_width + 5))
    print(f"{'Слово':<{word_width}} | {'Частота':>{count_width}}")
    print("=" * (word_width + count_width + 5))

    for word, count in top_words:
        print(f"{word:<{word_width}} | {count:>{count_width}}")
    
    print("=" * (word_width + count_width + 5))


def main_single(input_file: str, output_file: str, encoding: str = "utf-8"):
    try:
        text = read_text(input_file, encoding)
        word_freq = process_text(text)
        total_words = sum(word_freq.values())
        
        sorted_words = top_n(word_freq, len(word_freq))
        rows = [(word, str(count)) for word, count in sorted_words]
        write_csv(rows, output_file, header=("word", "count"))
        
        print_summary(word_freq, total_words)
        print_pretty_table(word_freq)
        
        print(f"\nОтчёт сохранён в: {output_file}")
        
    except FileNotFoundError:
        print(f"Ошибка: файл {input_file} не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: неверная кодировка файла. Попробуйте --encoding cp1251")
        sys.exit(1)


def main_multiple(input_files: List[str], per_file_output: str, total_output: str, encoding: str = "utf-8"):
    all_word_freq = {}
    per_file_data = []
    
    for input_file in input_files:
        try:
            text = read_text(input_file, encoding)
            word_freq = process_text(text)

            for word, count in word_freq.items():
                all_word_freq[word] = all_word_freq.get(word, 0) + count

            for word, count in word_freq.items():
                per_file_data.append((Path(input_file).name, word, str(count)))
            
        except FileNotFoundError:
            print(f"Ошибка: файл {input_file} не найден")
            sys.exit(1)
        except UnicodeDecodeError:
            print(f"Ошибка: неверная кодировка файла {input_file}. Попробуйте --encoding cp1251")
            sys.exit(1)

    per_file_data.sort(key=lambda x: (x[0], -int(x[2]), x[1]))
    write_csv(per_file_data, per_file_output, header=("file", "word", "count"))

    sorted_total = top_n(all_word_freq, len(all_word_freq))
    total_rows = [(word, str(count)) for word, count in sorted_total]
    write_csv(total_rows, total_output, header=("word", "count"))

    total_words = sum(all_word_freq.values())
    print_summary(all_word_freq, total_words)
    print_pretty_table(all_word_freq)
    
    print(f"\nОтчёт по файлам сохранён в: {per_file_output}")
    print(f"Сводный отчёт сохранён в: {total_output}")


def main():
    parser = argparse.ArgumentParser(description='Генерация отчёта по частоте слов')
    parser.add_argument('--in', dest='input_files', nargs='+', 
                       default=['data/lab04/input.txt'],
                       help='Входные файлы (по умолчанию: data/lab04/input.txt)')
    parser.add_argument('--out', dest='output_file',
                       default='data/lab04/report.csv',
                       help='Выходной файл (по умолчанию: data/lab04/report.csv)')
    parser.add_argument('--per-file', dest='per_file_output',
                       help='Отчёт по файлам (★)')
    parser.add_argument('--total', dest='total_output',
                       help='Сводный отчёт (★)')
    parser.add_argument('--encoding', default='utf-8',
                       help='Кодировка файлов (по умолчанию: utf-8)')
    
    args = parser.parse_args()

    if len(args.input_files) == 1 and not args.per_file_output and not args.total_output:
        main_single(args.input_files[0], args.output_file, args.encoding)
    else:
        if not args.per_file_output:
            args.per_file_output = 'data/lab04/report_per_file.csv'
        if not args.total_output:
            args.total_output = 'data/lab04/report_total.csv'
        main_multiple(args.input_files, args.per_file_output, args.total_output, args.encoding)


if __name__ == "__main__":
    main()


```
![alt text](images/lab04/image-02-(4)(1).png)

![alt text](images/lab04/image-02-(4)(2).png)

![alt text](images/lab04/image-02-(4)(3).png)

![alt text](images/lab04/image-02-(4)(4).png)

![alt text](images/lab04/image-02-(4)(5).png)

![alt text](images/lab04/image-02-(4)(6).png)

![alt text](images/lab04/image-02-(4)(7).png)

![alt text](images/lab04/image-02-(4)(8).png)

![alt text](images/lab04/image-02-(4)(9).png)





## lab05


## ex01
```python
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
try:
    from scr.lib.io_helpers import read_json, write_json, read_csv, write_csv
except ImportError:
    import os
    lib_path = Path(__file__).parent.parent / "lib"
    sys.path.append(str(lib_path))
    from io_helpers import read_json, write_json, read_csv, write_csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        data = read_json(json_path)

        if not isinstance(data, list):
            raise ValueError("JSON должен содержать список объектов")
        
        if len(data) == 0:
            raise ValueError("JSON файл пуст")

        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Все элементы JSON должны быть словарями")

        all_fields = set()
        for item in data:
            all_fields.update(item.keys())

        first_item_fields = list(data[0].keys())
        additional_fields = sorted(all_fields - set(first_item_fields))
        fieldnames = first_item_fields + additional_fields

        processed_data = []
        for item in data:
            row = {field: item.get(field, "") for field in fieldnames}
            processed_data.append(row)

        write_csv(processed_data, csv_path, fieldnames)
        
    except (FileNotFoundError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании JSON в CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        data = read_csv(csv_path)

        write_json(data, json_path)
        
    except (FileNotFoundError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании CSV в JSON: {e}")


if __name__ == "__main__":
    try:
        print("=== Тестирование JSON ↔ CSV ===")

        current_dir = Path(__file__).parent
        samples_dir = current_dir / "../../data/samples"
        out_dir = current_dir / "../../data/out"

        out_dir.mkdir(parents=True, exist_ok=True)

        print("1. Конвертация JSON to CSV...")
        json_to_csv(
            str(samples_dir / "people.json"),
            str(out_dir / "people_from_json.csv")
        )
        print("✓ Успешно преобразован JSON в CSV")

        print("2. Конвертация CSV to JSON...")
        csv_to_json(
            str(samples_dir / "people.csv"),
            str(out_dir / "people_from_csv.json")
        )
        print("✓ Успешно преобразован CSV в JSON")
        
        print("✓ Все операции завершены успешно!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")


```
![alt text](images/lab05/image-01-(5)(1).png)

![alt text](images/lab05/image-01-(5)(2).png)

![alt text](images/lab05/image-01-(5)(3).png)

![alt text](images/lab05/image-01-(5)(4).png)

![alt text](images/lab05/image-01-(5)(5).png)





## ex02
```python
import csv
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from pathlib import Path


def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    try:
        csv_path_obj = Path(csv_path)
        if not csv_path_obj.exists():
            raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

        xlsx_dir = Path(xlsx_path).parent
        xlsx_dir.mkdir(parents=True, exist_ok=True)

        wb = Workbook()
        ws = wb.active
        ws.title = "Sheet1"

        with open(csv_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                ws.append(row)

        if ws.max_row == 0:
            raise ValueError("CSV файл пуст")

        for col in range(1, ws.max_column + 1):
            max_length = 0
            column_letter = get_column_letter(col)
            
            for row in range(1, ws.max_row + 1):
                cell_value = ws.cell(row=row, column=col).value
                if cell_value:
                    max_length = max(max_length, len(str(cell_value)))

            adjusted_width = max(max_length + 2, 8)
            ws.column_dimensions[column_letter].width = adjusted_width

        wb.save(xlsx_path)
        print(f"✓ Успешно создан XLSX файл: {xlsx_path}")
        
    except FileNotFoundError as e:
        raise e
    except ValueError as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании CSV в XLSX: {e}")


if __name__ == "__main__":
    try:
        print("=== Тестирование CSV to XLSX ===")

        current_dir = Path(__file__).parent
        samples_dir = current_dir / "../../data/samples"
        out_dir = current_dir / "../../data/out"

        out_dir.mkdir(parents=True, exist_ok=True)

        print("1. Конвертация people.csv...")
        csv_to_xlsx(
            str(samples_dir / "people.csv"),
            str(out_dir / "people.xlsx")
        )

        cities_csv = samples_dir / "cities.csv"
        if cities_csv.exists():
            print("2. Конвертация cities.csv...")
            csv_to_xlsx(
                str(cities_csv),
                str(out_dir / "cities.xlsx")
            )
        else:
            print("2. cities.csv не найден, пропускаем")
            
        print("✓ Все операции завершены успешно!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")


```
![alt text](images/lab05/image-02-(5)(1).png)

![alt text](images/lab05/image-02-(5)(2).png)

![alt text](images/lab05/image-02-(5)(3).png)

![alt text](images/lab05/image-02-(5)(4).png)

![alt text](images/lab05/image-02-(5)(5).png)


## lib
```python
import json
import csv
from pathlib import Path
from typing import Union, List, Dict, Any


def read_json(file_path: Union[str, Path]) -> Any:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON файл не найден: {file_path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        if data is None:
            raise ValueError(f"JSON файл пуст: {file_path}")
            
        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Неверный формат JSON в файле: {file_path}")


def write_json(data: Any, file_path: Union[str, Path], indent: int = 2) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def read_csv(file_path: Union[str, Path]) -> List[Dict[str, str]]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {file_path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = list(reader)
            
        if not data:
            raise ValueError(f"CSV файл пуст: {file_path}")
            
        return data
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV {file_path}: {e}")


def write_csv(data: List[Dict[str, Any]], file_path: Union[str, Path], fieldnames: list = None) -> None:
    if not data:
        raise ValueError("Данные пусты")
    
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    if fieldnames is None:
        fieldnames = list(data[0].keys())
    
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def ensure_directory(dir_path: Union[str, Path]) -> Path:
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def validate_file_exists(file_path: Union[str, Path]) -> bool:
    path = Path(file_path)
    return path.exists() and path.stat().st_size > 0