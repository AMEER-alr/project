import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))
try:
    from scr.lib.io_helpers import read_json, write_json, read_csv, write_csv
except ImportError:
    import os
    lib_path = Path(__file__).parent.parent / "lib"
    sys.path.append(str(lib_path))
    from io_helpers import read_json, write_json, read_csv, write_csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        data = read_json(json_path)

        if not isinstance(data, list):
            raise ValueError("JSON должен содержать список объектов")
        
        if len(data) == 0:
            raise ValueError("JSON файл пуст")

        for item in data:
            if not isinstance(item, dict):
                raise ValueError("Все элементы JSON должны быть словарями")

        all_fields = set()
        for item in data:
            all_fields.update(item.keys())

        first_item_fields = list(data[0].keys())
        additional_fields = sorted(all_fields - set(first_item_fields))
        fieldnames = first_item_fields + additional_fields

        processed_data = []
        for item in data:
            row = {field: item.get(field, "") for field in fieldnames}
            processed_data.append(row)

        write_csv(processed_data, csv_path, fieldnames)
        
    except (FileNotFoundError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании JSON в CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        data = read_csv(csv_path)

        write_json(data, json_path)
        
    except (FileNotFoundError, ValueError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Ошибка при преобразовании CSV в JSON: {e}")


if __name__ == "__main__":
    try:
        print("=== Тестирование JSON ↔ CSV ===")

        current_dir = Path(__file__).parent
        samples_dir = current_dir / "../../data/samples"
        out_dir = current_dir / "../../data/out"

        out_dir.mkdir(parents=True, exist_ok=True)

        print("1. Конвертация JSON to CSV...")
        json_to_csv(
            str(samples_dir / "people.json"),
            str(out_dir / "people_from_json.csv")
        )
        print("✓ Успешно преобразован JSON в CSV")

        print("2. Конвертация CSV to JSON...")
        csv_to_json(
            str(samples_dir / "people.csv"),
            str(out_dir / "people_from_csv.json")
        )
        print("✓ Успешно преобразован CSV в JSON")
        
        print("✓ Все операции завершены успешно!")
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")