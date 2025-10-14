import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lib'))

from text1 import normalize, tokenize, count_freq, top_n, print_freq_table, TABLE_MODE

text1 = "Привет\nМир\t"
text2 = "Ёжик, Ёлка"
text3 = "hello\n\nworld"
text4 = "  двойные пробелы  "

print(f"normalize('Привет\\nМир\\t') = '{normalize(text1)}'")
print(f"normalize('Ёжик, Ёлка', yo2e=True) = '{normalize(text2, yo2e=True)}'")
print(f"normalize('hello\\n\\nworld') = '{normalize(text3)}'")
print(f"normalize('  двойные пробелы  ') = '{normalize(text4)}'")

print(f"tokenize('привет мир') = {tokenize('привет мир')}")
print(f"tokenize('hello, world!!!') = {tokenize('hello, world!!!')}")
print(f"tokenize('по-настоящему круто') = {tokenize('по-настоящему круто')}")
print(f"tokenize('2025 год') = {tokenize('2025 год')}")
print(f"tokenize('emoji ⚫ не слово') = {tokenize('emoji ⚫ не слово')}")

tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print(f"Токены {tokens1} -> частоты {freq1}")
print(f"top_n(..., n=2) -> {top_n(freq1, n=2)}")

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
print(f"Токены {tokens2} -> частоты {freq2}")
print(f"top_n(..., n=2) -> {top_n(freq2, n=2)}")

test_text = "Привет привет мир мир мир тест тест тест"
norm_text = normalize(test_text)
tokens_test = tokenize(norm_text)
freq_test = count_freq(tokens_test)

print("Table mode enabled:")
print_freq_table(freq_test, n=5, table_mode=True)

print("Table mode disabled:")
print_freq_table(freq_test, n=5, table_mode=False)