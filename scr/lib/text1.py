import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not text:
        return ""
    
    if yo2e:
        text = text.replace('Ё', 'Е').replace('ё', 'е')
    
    if casefold:
        text = text.casefold()
    
    text = re.sub(r'[\x00-\x1f\x7f-\x9f]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    
    return text.strip()

def tokenize(text: str) -> list[str]:
    if not text:
        return []
    
    pattern = r'[\w\-]+'
    tokens = re.findall(pattern, text)
    
    return [token for token in tokens if token]

def count_freq(tokens: list[str]) -> dict[str, int]:
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not freq:
        return []
    
    items = list(freq.items())
    sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]

def print_freq_table(freq: dict[str, int], n: int = 10, table_mode: bool = False):
    if not freq:
        return
    
    top_items = top_n(freq, n)
    
    if not table_mode:
        for word, count in top_items:
            print(f"{word}: {count}")
        return
    
    if not top_items:
        return
    
    max_word_length = max(len(word) for word, _ in top_items)
    word_column_width = max(max_word_length, 6)
    
    print(f"| {'слово':<{word_column_width}} | {'частота':<8} |")
    print(f"|{'-' * (word_column_width + 2)}|{'-' * 10}|")
    
    for word, count in top_items:
        print(f"| {word:<{word_column_width}} | {count:<8} |")

TABLE_MODE = False