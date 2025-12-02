import pytest
from scr.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("Привёт\vnWψv\t", "привет nwψv"),
            ("Ежик, Елка", "ежик, елка"),
            ("Hello\vr\vnworld", "hello r nworld"),
            ("   двойные   пробелы   ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("ТЕСТ123", "тест123"),
            ("Спец.символы!@#", "спец.символы!@#"),
        ],
    )
    def test_normalize_basic(self, source, expected):
        assert normalize(source) == expected


class TestTokenize:
    @pytest.mark.parametrize(
        "text, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello world test", ["hello", "world", "test"]),
            ("один, два. три!", ["один", "два", "три"]),
            ("", []),
            ("   ", []),
            ("много    пробелов", ["много", "пробелов"]),
        ],
    )
    def test_tokenize_basic(self, text, expected):
        assert tokenize(text) == expected


class TestCountFreq:
    def test_count_freq_basic(self):
        tokens = ["apple", "banana", "apple", "cherry", "banana", "apple"]
        result = count_freq(tokens)
        expected = {"apple": 3, "banana": 2, "cherry": 1}
        assert result == expected

    def test_count_freq_empty(self):
        assert count_freq([]) == {}

    def test_count_freq_single_word(self):
        assert count_freq(["test"]) == {"test": 1}


class TestTopN:
    def test_top_n_basic(self):
        freq = {"apple": 5, "banana": 3, "cherry": 7, "date": 2}
        result = top_n(freq, 2)
        expected = [("cherry", 7), ("apple", 5)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        freq = {"apple": 5, "banana": 5, "cherry": 3, "date": 5}
        result = top_n(freq, 3)
        expected = [("apple", 5), ("banana", 5), ("date", 5)]
        assert result == expected

    def test_top_n_more_than_available(self):
        freq = {"a": 1, "b": 2}
        result = top_n(freq, 5)
        expected = [("b", 2), ("a", 1)]
        assert result == expected

    def test_top_n_empty(self):
        assert top_n({}, 5) == []
