import sys
import os

current_dir = os.path.dirname(__file__)
parent_dir = os.path.dirname(current_dir)
lib_path = os.path.join(parent_dir, 'lib')
sys.path.insert(0, lib_path)

from text import normalize, tokenize, count_freq, top_n

print("1. normalize('Привет\\nМир\\t') =", repr(normalize("Привет\nМир\t")))
print("2. normalize('Ёжик, Ёлка', yo2e=True) =", repr(normalize("Ёжик, Ёлка", yo2e=True)))
print("3. normalize('hello\\n\\nworld') =", repr(normalize("hello\n\nworld")))
print("4. normalize('  двойные пробелы  ') =", repr(normalize("  двойные пробелы  ")))

print("5. tokenize('привет мир') =", tokenize("привет мир"))
print("6. tokenize('hello, world!!!') =", tokenize("hello, world!!!"))
print("7. tokenize('по-настоящему круто') =", tokenize("по-настоящему круто"))
print("8. tokenize('2025 год') =", tokenize("2025 год"))
print("9. tokenize('emoji ⚫ не слово') =", tokenize("emoji ⚫ не слово"))

tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print("10. Токены", tokens1, "-> частоты", freq1)
print("11. top_n(..., n=2) ->", top_n(freq1, n=2))

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
print("12. Токены", tokens2, "-> частоты", freq2)
print("13. top_n(..., n=2) ->", top_n(freq2, n=2))