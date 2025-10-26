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