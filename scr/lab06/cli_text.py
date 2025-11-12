import argparse
import sys


def read_file_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def word_frequency_analysis(text, top_n=5):
    words = text.lower().split()
    word_count = {}
    
    for word in words:
        word = word.strip('.,!?;:"()[]{}')
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:top_n]

def cat_command(args):
    lines = read_file_lines(args.input)
    for i, line in enumerate(lines, 1):
        if args.n:
            print(f"{i:6d}  {line.rstrip()}")
        else:
            print(line.rstrip())

def stats_command(args):
    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            text = f.read()
        
        top_words = word_frequency_analysis(text, args.top)
        print(f"Top {args.top} most frequent words:")
        for i, (word, count) in enumerate(top_words, 1):
            print(f"{i}. '{word}': {count} occurrences")
            
    except FileNotFoundError:
        print(f"Error: File not found: {args.input}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="CLI Text Tools")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat_parser = subparsers.add_parser("cat", help="Display file content")
    cat_parser.add_argument("--input", required=True, help="Input file path")
    cat_parser.add_argument("-n", action="store_true", help="Number lines")
    cat_parser.set_defaults(func=cat_command)

    stats_parser = subparsers.add_parser("stats", help="Word frequency analysis")
    stats_parser.add_argument("--input", required=True, help="Input file path")
    stats_parser.add_argument("--top", type=int, default=5, help="Top N words")
    stats_parser.set_defaults(func=stats_command)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()