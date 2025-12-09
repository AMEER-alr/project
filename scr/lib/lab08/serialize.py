import json
from .models import Student
from typing import List

def students_to_json(students: List[Student], path: str) -> None:
    data = [s.to_dict() for s in students]
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные успешно сохранены в {path}")

def students_from_json(path: str) -> List[Student]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        students = []
        for item in data:
            try:
                student = Student.from_dict(item)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при создании студента из данных: {item}")
                print(f"Ошибка: {e}")
        
        print(f"Загружено {len(students)} студентов из {path}")
        return students
    
    except FileNotFoundError:
        print(f"Файл {path} не найден!")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка чтения JSON из файла {path}")
        return []