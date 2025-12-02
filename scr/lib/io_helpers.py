import json
import csv
from pathlib import Path
from typing import Union, List, Dict, Any


def read_json(file_path: Union[str, Path]) -> Any:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"JSON файл не найден: {file_path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if data is None:
            raise ValueError(f"JSON файл пуст: {file_path}")

        return data
    except json.JSONDecodeError as e:
        raise ValueError(f"Неверный формат JSON в файле: {file_path}")


def write_json(data: Any, file_path: Union[str, Path], indent: int = 2) -> None:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


def read_csv(file_path: Union[str, Path]) -> List[Dict[str, str]]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV файл не найден: {file_path}")

    try:
        with open(path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = list(reader)

        if not data:
            raise ValueError(f"CSV файл пуст: {file_path}")

        return data
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV {file_path}: {e}")


def write_csv(
    data: List[Dict[str, Any]], file_path: Union[str, Path], fieldnames: list = None
) -> None:
    if not data:
        raise ValueError("Данные пусты")

    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if fieldnames is None:
        fieldnames = list(data[0].keys())

    with open(path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def ensure_directory(dir_path: Union[str, Path]) -> Path:
    path = Path(dir_path)
    path.mkdir(parents=True, exist_ok=True)
    return path


def validate_file_exists(file_path: Union[str, Path]) -> bool:
    path = Path(file_path)
    return path.exists() and path.stat().st_size > 0
