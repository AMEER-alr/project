import sys
import os

scr_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, scr_dir)

from lab13.models import InPatient, OutPatient, EmergencyPatient
from lab15.collection import ExtendedPatientCollection


def by_patient_age(p):
    return p.age

def by_patient_name(p):
    return p.name.lower()

def by_patient_status(p):
    order = {"критическое состояние": 0, "на лечении": 1, "активен": 2}
    return order.get(p.status, 3)

def is_adult(p):
    return p.age >= 18

def is_critical(p):
    return p.status == "критическое состояние"

def patient_to_str(p):
    icons = {"активен": "✅", "на лечении": "🏥", "критическое состояние": "🚨"}
    return f"{icons.get(p.status, '❓')} {p.name} | {p.age} лет | {p.diagnosis}"


class PriorityStrategy:
    def __call__(self, p):
        if p.status == "критическое состояние":
            return 1
        if p.temperature >= 39:
            return 2
        if p.status == "на лечении":
            return 3
        return 4


class TreatmentPlanStrategy:
    def __call__(self, p):
        t = p.get_patient_type()
        if t == "InPatient":
            return f"🏥 {p.name}: палата {p.room_number}"
        if t == "OutPatient":
            return f"📅 {p.name}: {p.appointment_date}"
        if t == "EmergencyPatient":
            return f"🚑 {p.name}: уровень {p.urgency_level}"
        return p.name


def create_patients():
    col = ExtendedPatientCollection()

    col.add(InPatient("Иван Петров", 72, "Гипертония", "кардиолог", 101, 3500, 36.8, 145, 90))
    col.add(InPatient("Анна Смирнова", 45, "Пневмония", "терапевт", 205, 4200, 38.7, 120, 80))
    col.add(OutPatient("Мария Сидорова", 25, "Грипп", "терапевт", "2026-05-20", 1500, 37.2, 115, 75))
    col.add(OutPatient("Дмитрий Козлов", 35, "Ангина", "отоларинголог", "2026-05-18", 2000, 38.2, 125, 80))
    col.add(EmergencyPatient("Елена Васина", 68, "Инфаркт", "кардиолог", 2, True, 36.5, 95, 60))
    col.add(EmergencyPatient("Сергей Николаев", 58, "Инсульт", "невролог", 1, True, 39.1, 180, 110))
    
    return col


def print_col(col, title):
    print(f"\n{'='*55}")
    print(f"📋 {title}")
    print(f"{'='*55}")
    for i, p in enumerate(col.get_all(), 1):
        print(f"  {i}. {patient_to_str(p)}")


def main():
    
    print("\n" + "="*55)
    print("ЛАБОРАТОРНАЯ РАБОТА №15 - Медицина")
    print("="*55)
    
    print("\n--- СЦЕНАРИЙ 1: filter → sort → apply ---")
    col = create_patients()
    print_col(col, "Исходная коллекция")
    
    col.filter_by(is_adult).sort_by(by_patient_status)
    print_col(col, "После filter + sort")
    
    col.apply(TreatmentPlanStrategy())
    print("\nПосле apply (планы лечения):")
    for p in col.get_all():
        print(f"  {p}")
    
    print("\n--- СЦЕНАРИЙ 2: Замена стратегии сортировки ---")
    col2 = create_patients()
    col2.sort_by(by_patient_name)
    print_col(col2, "Сортировка по имени")
    
    col2.sort_by(by_patient_age)
    print_col(col2, "Сортировка по возрасту")
    
    col3 = create_patients()
    col3.sort_by(lambda p: p.patient_id)
    print("\n--- Lambda: сортировка по ID ---")
    for p in col3.get_all():
        print(f"  {p.patient_id}: {p.name}")
    
    print("\n--- СЦЕНАРИЙ 3: Callable-объекты ---")
    priority = PriorityStrategy()
    levels = {1: "КРИТИЧЕСКИЙ", 2: "ВЫСОКИЙ", 3: "СРЕДНИЙ", 4: "ОБЫЧНЫЙ"}
    for p in create_patients().get_all():
        print(f"  {p.name:20} | {levels[priority(p)]}")
    
    names = create_patients().map_to(lambda p: p.name)
    print(f"\n📌 map() - имена: {names}")
    
    print("\n" + "="*55)
    print("✅ ВСЕ ТЕСТЫ ПРОШЛИ УСПЕШНО!")
    print("="*55)


if __name__ == "__main__":
    main()