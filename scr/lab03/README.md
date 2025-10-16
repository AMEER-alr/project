## lib

## ex01
```python
import re
from collections import defaultdict
from typing import Dict, List, Tuple

def normalize(text: str, *, casefold: bool = True, yo_to_e: bool = True) -> str:
    if not text:
        return ""
    
    processed = text

    if casefold:
        processed = processed.casefold()

    if yo_to_e:
        processed = processed.replace('ё', 'е').replace('Ё', 'Е')

    control_pattern = r'[\t\r\n\v\f]'
    processed = re.sub(control_pattern, ' ', processed)

    processed = re.sub(r' +', ' ', processed).strip()
    
    return processed

def tokenize(text: str) -> List[str]:
    if not text:
        return []

    token_pattern = r'[a-zа-яё0-9_]+(?:-[a-zа-яё0-9_]+)*'
    
    matches = re.findall(token_pattern, text, flags=re.IGNORECASE)
    return matches

def count_freq(tokens: List[str]) -> Dict[str, int]:
    frequency_counter = defaultdict(int)
    
    for item in tokens:
        frequency_counter[item] += 1
            
    return dict(frequency_counter)

def top_n(frequency_data: Dict[str, int], limit: int = 5) -> List[Tuple[str, int]]:
    items_list = [(word, count) for word, count in frequency_data.items()]

    items_list.sort(key=lambda item: (-item[1], item[0]))
    
    return items_list[:limit]

if __name__ == "__main__":
    print(repr(normalize("ПрИвЕт\nМир\t")))
    print(repr(normalize("ёжик, Ёлка")))
    print(repr(normalize("Hello\r\nWorld")))
    print(repr(normalize("  двойные   пробелы  ")))
    print()

    print(tokenize("привет мир"))
    print(tokenize("hello,world!!!"))
    print(tokenize("по-настоящему круто"))
    print(tokenize("2025 год"))
    print(tokenize("emoji 😀 не слово"))
    print()
    
    frequency_data1 = count_freq(["a", "b", "a", "c", "b", "a"])
    print("Frequency 1:", frequency_data1)
    print("Top 2:", top_n(frequency_data1, 2))
    
    frequency_data2 = count_freq(["bb", "aa", "bb", "aa", "cc"])
    print("Frequency 2:", frequency_data2)
    print("Top 2:", top_n(frequency_data2, 2))
    

```
![alt text](/images/lab03/image-01-(3).png)



## lab03

## ex02
```python
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'lib'))

from text import normalize, tokenize, count_freq, top_n

def analyze_text(input_str: str, use_table: bool = False) -> str:
    if not input_str or input_str.isspace():
        return "No input text provided."

    clean_text = normalize(input_str)
    words = tokenize(clean_text)
    counts = count_freq(words)
    top_items = top_n(counts, 5)

    lines = []
    lines.append(f"Всего слов: {len(words)}")
    lines.append(f"Уникальных слов: {len(counts)}")
    lines.append("Топ-5:")
    
    if use_table:
        if top_items:
            col_width = max(len(item[0]) for item in top_items)
            col_width = max(col_width, 5)
            
            lines.append(f"| {'слово'.ljust(col_width)} | частота |")
            lines.append(f"|{'-' * (col_width + 2)}|---------|")

            for item, count in top_items:
                lines.append(f"| {item.ljust(col_width)} | {count:7} |")
        else:
            lines.append("| (нет данных) |         |")
    else:
        for item, count in top_items:
            lines.append(f"{item}:{count}")
    
    return "\n".join(lines)

def run_program():
    table_mode = os.environ.get('TEXT_STATS_TABLE') == '1'

    if any(arg in sys.argv for arg in ['--table', '-t']):
        table_mode = True

    if sys.stdin.isatty():
        print("press (Ctrl+Z then Enter):")
        print("to show the table write: --table or -t")
    
    try:
        user_input = sys.stdin.read().strip()
    except KeyboardInterrupt:
        print("\nВвод прерван.")
        return
    
    if not user_input:
        print("Ошибка: Не получен входной текст.")
        sys.exit(1)

    output = analyze_text(user_input, table_mode)
    print(output)

if __name__ == "__main__":
    run_program()


```
![alt text](/images/lab03/image-02-(3).png)