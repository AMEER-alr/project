import csv
from pathlib import Path
from typing import List, Dict, Any
import json

from scr.lib.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        self.__ensure_storage_exists()
    
    def __ensure_storage_exists(self):
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])
    
    def __read_all(self) -> List[Dict[str, str]]:
        rows = []
        if self.path.exists() and self.path.stat().st_size > 0:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    cleaned_row = {key: value.strip() for key, value in row.items()}
                    rows.append(cleaned_row)
        return rows
    
    def __write_all(self, rows: List[Dict[str, str]]):
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["fio", "birthdate", "group", "gpa"])
            writer.writeheader()
            writer.writerows(rows)
    
    def list(self) -> List[Student]:
        rows = self.__read_all()
        students = []
        for row in rows:
            try:
                student = Student(
                    fio=row["fio"],
                    birthdate=row["birthdate"],
                    group=row["group"],
                    gpa=float(row["gpa"])
                )
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при создании Student: {row} - {e}")
        return students
    
    def add(self, student: Student):
        rows = self.__read_all()

        for row in rows:
            if row["fio"] == student.fio:
                raise ValueError(f"Студент '{student.fio}' уже существует")

        rows.append({
            "fio": student.fio,
            "birthdate": student.birthdate,
            "group": student.group,
            "gpa": str(student.gpa)
        })
        
        self.__write_all(rows)
    
    def find(self, substr: str) -> List[Student]:
        rows = self.__read_all()
        result = []
        
        for row in rows:
            if substr.lower() in row["fio"].lower():
                try:
                    student = Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"])
                    )
                    result.append(student)
                except (ValueError, KeyError) as e:
                    continue
        
        return result
    
    def remove(self, fio: str) -> bool:
        rows = self.__read_all()
        original_count = len(rows)
        
        new_rows = [row for row in rows if row["fio"] != fio]
        
        if len(new_rows) < original_count:
            self.__write_all(new_rows)
            return True
        return False
    
    def update(self, fio: str, **kwargs) -> bool:
        rows = self.__read_all()
        updated = False
        
        for row in rows:
            if row["fio"] == fio:
                for key, value in kwargs.items():
                    if key in row:
                        if key == "gpa":
                            row[key] = str(float(value))
                        else:
                            row[key] = str(value)
                updated = True
                break
        
        if updated:
            self.__write_all(rows)
        
        return updated
    
    def stats(self) -> Dict[str, Any]:
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "min_gpa": 0.0,
                "max_gpa": 0.0,
                "avg_gpa": 0.0,
                "groups": {},
                "top_5_students": []
            }

        gpas = [student.gpa for student in students]

        groups_dist = {}
        for student in students:
            group = student.group
            groups_dist[group] = groups_dist.get(group, 0) + 1

        sorted_students = sorted(students, key=lambda x: x.gpa, reverse=True)
        top_5 = sorted_students[:5]
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups_dist,
            "top_5_students": [
                {"fio": student.fio, "gpa": student.gpa}
                for student in top_5
            ]
        }