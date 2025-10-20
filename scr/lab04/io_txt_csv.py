from pathlib import Path
import csv
from typing import Union, Tuple, List


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:
    path = Path(path)
    
    with open(path, 'r', encoding=encoding) as file:
        content = file.read()
    
    return content


def write_csv(rows: List[Union[tuple, list]], path: Union[str, Path], 
              header: Tuple[str, ...] = None) -> None:
    path = Path(path)
    ensure_parent_dir(path)
    
    if rows:
        first_length = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_length:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_length}")
    
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',')
        
        if header is not None:
            writer.writerow(header)
        
        writer.writerows(rows)


def ensure_parent_dir(path: Union[str, Path]) -> None:
    path = Path(path)
    parent_dir = path.parent
    parent_dir.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    try:
        txt = read_text("data/lab04/input.txt")
        print(f"File content: '{txt}'")
        print(f"Content length: {len(txt)}")
    except Exception as e:
        print(f"Error: {e}")

    try:
        write_csv([("word", "count"), ("test", "3")], "data/lab04/check.csv")
        print("check.csv created successfully")
    except Exception as e:
        print(f"Error: {e}")