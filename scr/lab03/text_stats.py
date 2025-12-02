import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "lib"))

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
    table_mode = os.environ.get("TEXT_STATS_TABLE") == "1"

    if any(arg in sys.argv for arg in ["--table", "-t"]):
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
