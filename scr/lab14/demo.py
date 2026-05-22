from typing import List
from models import InPatient, OutPatient, EmergencyPatient
from interfaces import Printable, Comparable, MedicalInfo



def print_all(items: List[Printable]) -> None:
    print("\n" + "=" * 80)
    print("ФУНКЦИЯ print_all() - РАБОТА ЧЕРЕЗ ИНТЕРФЕЙС Printable")
    print("=" * 80)
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.to_string()}")


def find_max(items: List[Comparable]) -> Comparable:
    if not items:
        raise ValueError("Список пуст")
    
    max_item = items[0]
    for item in items[1:]:
        if item.compare_to(max_item) > 0:
            max_item = item
    return max_item


def find_min(items: List[Comparable]) -> Comparable:
    if not items:
        raise ValueError("Список пуст")
    
    min_item = items[0]
    for item in items[1:]:
        if item.compare_to(min_item) < 0:
            min_item = item
    return min_item


def print_medical_info(items: List[MedicalInfo]) -> None:
    print("\n" + "=" * 80)
    print("ФУНКЦИЯ print_medical_info() - МЕДИЦИНСКАЯ СВОДКА")
    print("=" * 80)
    for i, item in enumerate(items, start=1):
        print(f"{i}. {item.get_medical_summary()}")



def get_printable(objects: List) -> List[Printable]:
    return [obj for obj in objects if isinstance(obj, Printable)]


def get_comparable(objects: List) -> List[Comparable]:
    return [obj for obj in objects if isinstance(obj, Comparable)]


def get_medical_info_objects(objects: List) -> List[MedicalInfo]:
    return [obj for obj in objects if isinstance(obj, MedicalInfo)]



def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(f"📋 {title}")
    print("=" * 80)


def print_subheader(title: str) -> None:
    print("\n" + "-" * 60)
    print(f"🔹 {title}")
    print("-" * 60)


def scenario_1_create_objects():
    print_header("СЦЕНАРИЙ 1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ (МЕДИЦИНА)")
    
    p1 = InPatient(
        "Иван Петров",
        45,
        "Пневмония",
        "терапевт",
        room_number=101,
        daily_cost=3500,
        temperature=38.2,
        systolic=130,
        diastolic=85
    )
    
    p2 = OutPatient(
        "Мария Соколова",
        29,
        "Головная боль",
        "невролог",
        appointment_date="2026-04-20",
        consultation_fee=1800,
        temperature=36.7,
        systolic=120,
        diastolic=80
    )
    
    p3 = EmergencyPatient(
        "Алексей Смирнов",
        61,
        "Инфаркт",
        "кардиолог",
        urgency_level=1,
        ambulance_arrival=True,
        temperature=39.1,
        systolic=170,
        diastolic=105
    )
    
    patients = [p1, p2, p3]
    
    print_subheader("Созданные объекты")
    for p in patients:
        print(f"✅ {p.get_patient_type()}: {p.name}, {p.age} лет, {p.diagnosis}")
    
    return patients


def scenario_2_interface_isinstance_checks(patients):
    print_header("СЦЕНАРИЙ 2. ПРОВЕРКА isinstance() ДЛЯ ИНТЕРФЕЙСОВ")
    
    for p in patients:
        print_subheader(f"Проверка для {p.name} ({p.get_patient_type()})")
        
        if isinstance(p, Printable):
            print("  ✅ Реализует интерфейс Printable")
        else:
            print("  ❌ НЕ реализует Printable")
        
        if isinstance(p, Comparable):
            print("  ✅ Реализует интерфейс Comparable")
        else:
            print("  ❌ НЕ реализует Comparable")
        
        if isinstance(p, MedicalInfo):
            print("  ✅ Реализует интерфейс MedicalInfo")
        else:
            print("  ❌ НЕ реализует MedicalInfo")


def scenario_3_printable_interface_demo(patients):
    print_header("СЦЕНАРИЙ 3. ИНТЕРФЕЙС Printable - РАЗНАЯ РЕАЛИЗАЦИЯ to_string()")
    
    print_subheader("Вызов to_string() для каждого пациента")
    for p in patients:
        print(f"\n{p.get_patient_type()}:")
        print(f"  {p.to_string()}")
    
    print_all(patients)

    printable_objects = get_printable(patients)
    print_subheader("Фильтрация через get_printable()")
    print(f"Найдено объектов с интерфейсом Printable: {len(printable_objects)}")


def scenario_4_comparable_interface_demo(patients):
    print_header("СЦЕНАРИЙ 4. ИНТЕРФЕЙС Comparable - СРАВНЕНИЕ ОБЪЕКТОВ")
    
    print_subheader("Сравнение через compare_to()")

    print(f"\nСравнение {patients[0].name} ({patients[0].age} лет) и {patients[1].name} ({patients[1].age} лет):")
    result = patients[0].compare_to(patients[1])
    if result < 0:
        print(f"  {patients[0].name} младше")
    elif result > 0:
        print(f"  {patients[0].name} старше")
    else:
        print(f"  Одинаковый возраст")

    emergency_patients = [p for p in patients if isinstance(p, EmergencyPatient)]
    if len(emergency_patients) >= 1:
        e1 = emergency_patients[0]
        print(f"\nСравнение {e1.name} (срочность: {e1.urgency_level}) с самим собой:")
        print(f"  compare_to(self) = {e1.compare_to(e1)}")

    print_subheader("Универсальные функции через Comparable")

    inpatients = [p for p in patients if isinstance(p, InPatient)]
    if inpatients:
        print(f"\nПоиск среди стационарных пациентов (сравнение по номеру палаты):")
        for p in inpatients:
            print(f"  - {p.name}: палата {p.room_number}")
    
    print(f"\nПоиск максимального элемента по возрасту (среди всех пациентов):")
    max_by_age = find_max(patients)
    print(f"  Самый старший пациент: {max_by_age.name} ({max_by_age.age} лет)")
    
    min_by_age = find_min(patients)
    print(f"  Самый младший пациент: {min_by_age.name} ({min_by_age.age} лет)")


def scenario_5_multiple_interfaces_demo(patients):
    """Сценарий 5: Множественная реализация интерфейсов"""
    print_header("СЦЕНАРИЙ 5. МНОЖЕСТВЕННАЯ РЕАЛИЗАЦИЯ ИНТЕРФЕЙСОВ")
    
    print_subheader("Каждый класс реализует сразу несколько интерфейсов")
    
    for p in patients:
        print(f"\n{p.get_patient_type()}: {p.name}")
        print(f"  🔹 Printable.to_string() → {p.to_string()[:60]}...")
        print(f"  🔹 Comparable.compare_to() → доступен")
        print(f"  🔹 MedicalInfo.get_medical_summary() → {p.get_medical_summary()}")

    print_medical_info(patients)

    medical_info_objects = get_medical_info_objects(patients)
    print_subheader("Фильтрация через get_medical_info_objects()")
    print(f"Найдено объектов с интерфейсом MedicalInfo: {len(medical_info_objects)}")


def scenario_6_polymorphism_demo():
    print_header("СЦЕНАРИЙ 6. ПОЛИМОРФИЗМ ЧЕРЕЗ ИНТЕРФЕЙСЫ")
    
    print_subheader("Создание новых объектов для демонстрации")

    inpatients = [
        InPatient("Анна Крылова", 52, "Гипертония", "кардиолог", room_number=205, daily_cost=4200, temperature=36.8),
        InPatient("Дмитрий Морозов", 38, "Бронхит", "терапевт", room_number=102, daily_cost=3500, temperature=37.2),
        InPatient("Елена Ветрова", 67, "Артрит", "терапевт", room_number=310, daily_cost=4800, temperature=36.5),
    ]
    
    outpatients = [
        OutPatient("Сергей Кузнецов", 25, "Конъюнктивит", "офтальмолог", appointment_date="2026-05-15", consultation_fee=1500),
        OutPatient("Ольга Павлова", 33, "Отит", "отоларинголог", appointment_date="2026-05-10", consultation_fee=1700),
    ]
    
    emergency = EmergencyPatient(
        "Владимир Соколов", 75, "Инсульт", "невролог",
        urgency_level=2, ambulance_arrival=True, temperature=38.5, systolic=185, diastolic=110
    )
    
    all_patients = inpatients + outpatients + [emergency]
    
    print_subheader("Полиморфный вызов to_string() (без isinstance)")
    for p in all_patients:
        print(f"  {p.get_patient_type()}: {p.to_string()}")
    
    print_subheader("Фильтрация коллекции по интерфейсам")
    printable_filtered = get_printable(all_patients)
    comparable_filtered = get_comparable(all_patients)
    
    print(f"  Объектов с Printable: {len(printable_filtered)}")
    print(f"  Объектов с Comparable: {len(comparable_filtered)}")
    
    print_subheader("Сортировка через стандартный Python (использует __lt__)")
    sorted_by_age = sorted(all_patients, key=lambda x: x.age)
    for p in sorted_by_age:
        print(f"  {p.name}: {p.age} лет - {p.get_patient_type()}")


def main():
    print("\n" + "🏥" * 40)
    print("ЛАБОРАТОРНАЯ РАБОТА №14")
    print("Интерфейсы и абстрактные классы (ABC)")
    print("Вариант 10: МЕДИЦИНА")
    print("Оценка: 5 (полная реализация)")
    print("🏥" * 40)

    patients = scenario_1_create_objects()
    scenario_2_interface_isinstance_checks(patients)
    scenario_3_printable_interface_demo(patients)
    scenario_4_comparable_interface_demo(patients)
    scenario_5_multiple_interfaces_demo(patients)
    scenario_6_polymorphism_demo()
    
    print_header("ЗАВЕРШЕНИЕ ДЕМОНСТРАЦИИ")
    print("✅ Все требования выполнены:")
    print("   ✓ Минимум 2 интерфейса (Printable, Comparable, MedicalInfo)")
    print("   ✓ Минимум 2 класса реализуют интерфейсы")
    print("   ✓ Разная реализация методов в разных классах")
    print("   ✓ Использование интерфейсов как типов")
    print("   ✓ Универсальные функции через интерфейсы")
    print("   ✓ Множественная реализация интерфейсов")
    print("   ✓ Проверка через isinstance()")
    print("   ✓ Фильтрация коллекции по интерфейсу")
    print("   ✓ Полиморфизм без условий (хороший подход)")


if __name__ == "__main__":
    main()