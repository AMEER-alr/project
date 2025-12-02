import pytest
import json
import csv
from pathlib import Path
from scr.lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    def test_json_to_csv_basic(self, tmp_path):
        scr = tmp_path / "test.json"
        dst = tmp_path / "test.csv"
        data = [
            {"name": "Alice", "age": 22},
            {"name": "Bob", "age": 25},
        ]
        scr.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        json_to_csv(str(scr), str(dst))
        with dst.open(encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        assert len(rows) == 2
        assert {"name", "age"} <= set(rows[0].keys())
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "22"
        assert rows[1]["name"] == "Bob"
        assert rows[1]["age"] == "25"

    def test_json_to_csv_empty_file(self, tmp_path):
        scr = tmp_path / "empty.json"
        dst = tmp_path / "empty.csv"
        scr.write_text("", encoding="utf-8")
        with pytest.raises(ValueError):
            json_to_csv(str(scr), str(dst))

    def test_json_to_csv_invalid_json(self, tmp_path):
        scr = tmp_path / "invalid.json"
        dst = tmp_path / "invalid.csv"
        scr.write_text("{invalid json}", encoding="utf-8")
        with pytest.raises(ValueError):
            json_to_csv(str(scr), str(dst))

    def test_json_to_csv_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")


class TestCsvToJson:
    def test_csv_to_json_basic(self, tmp_path):
        scr = tmp_path / "test.csv"
        dst = tmp_path / "test.json"
        csv_content = "name,age\nAlice,22\nBob,25\n"
        scr.write_text(csv_content, encoding="utf-8")
        csv_to_json(str(scr), str(dst))
        with dst.open(encoding="utf-8") as f:
            data = json.load(f)
        assert len(data) == 2
        assert data[0]["name"] == "Alice"
        assert int(data[0]["age"]) == 22
        assert data[1]["name"] == "Bob"
        assert int(data[1]["age"]) == 25

    def test_csv_to_json_empty_file(self, tmp_path):
        scr = tmp_path / "empty.csv"
        dst = tmp_path / "empty.json"
        scr.write_text("", encoding="utf-8")
        with pytest.raises(ValueError):
            csv_to_json(str(scr), str(dst))

    def test_csv_to_json_invalid_csv(self, tmp_path):
        scr = tmp_path / "invalid.csv"
        dst = tmp_path / "invalid.json"
        scr.write_text("invalid,csv,content\nline1\nline2", encoding="utf-8")
        try:
            csv_to_json(str(scr), str(dst))
        except ValueError:
            pass

    def test_csv_to_json_file_not_found(self):
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_to_json_roundtrip(self, tmp_path):
        scr_json = tmp_path / "original.json"
        intermediate_csv = tmp_path / "intermediate.csv"
        final_json = tmp_path / "final.json"
        original_data = [
            {"name": "Alice", "age": 22},
            {"name": "Bob", "age": 25},
        ]
        scr_json.write_text(
            json.dumps(original_data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        json_to_csv(str(scr_json), str(intermediate_csv))
        csv_to_json(str(intermediate_csv), str(final_json))
        with final_json.open(encoding="utf-8") as f:
            final_data = json.load(f)
        converted_data = []
        for item in final_data:
            converted_item = item.copy()
            if "age" in converted_item:
                converted_item["age"] = int(converted_item["age"])
            converted_data.append(converted_item)
        assert converted_data == original_data
