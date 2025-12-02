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
        processed = processed.replace("ё", "е").replace("Ё", "Е")

    control_pattern = r"[\t\r\n\v\f]"
    processed = re.sub(control_pattern, " ", processed)

    processed = re.sub(r" +", " ", processed).strip()

    return processed


def tokenize(text: str) -> List[str]:
    if not text:
        return []

    token_pattern = r"[a-zа-яё0-9_]+(?:-[a-zа-яё0-9_]+)*"

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
