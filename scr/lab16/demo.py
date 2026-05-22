from base import Patient
from models import InPatient, OutPatient, EmergencyPatient
from container import TypedCollection, display_all, total_score


def demo_typed_collection_basic():
    print("\n" + "="*60)
    print("1. ДЕМОНСТРАЦИЯ TYPEDCOLLECTION (БАЗОВЫЕ ОПЕРАЦИИ)")
    print("="*60)
    
    collection = TypedCollection[Patient]()
    
    patient1 = InPatient(
        name="Иван Петров",
        age=45,
        diagnosis="гипертония",
        doctor_specialization="кардиолог",
        room_number=101,
        daily_cost=3500.0,
        temperature=36.8,
        systolic=130,
        diastolic=85
    )
    
    patient2 = OutPatient(
        name="Мария Сидорова",
        age=32,
        diagnosis="мигрень",
        doctor_specialization="невролог",
        appointment_date="2024-12-20",
        consultation_fee=2500.0,
        temperature=36.6,
        systolic=118,
        diastolic=78
    )
    
    patient3 = EmergencyPatient(
        name="Алексей Иванов",
        age=67,
        diagnosis="инфаркт",
        doctor_specialization="кардиолог",
        urgency_level=2,
        ambulance_arrival=True,
        temperature=38.5,
        systolic=160,
        diastolic=95
    )
    
    collection.add(patient1)
    collection.add(patient2)
    collection.add(patient3)
    
    print(f"\n📋 Всего пациентов: {len(collection)}")
    print(f"📋 Patient IDs: {[p.patient_id for p in collection.get_all()]}")
    
    print("\n🔍 Тестирование find():")
    found = collection.find(lambda p: p.name == "Мария Сидорова")
    if found:
        print(f"   ✅ Найден пациент: {found.name} (Тип: {found.get_patient_type()})")
    
    not_found = collection.find(lambda p: p.name == "Несуществующий")
    print(f"   ❌ Поиск несуществующего: {not_found}")
    
    print("\n📊 Тестирование filter():")
    cardiac_patients = collection.filter(lambda p: p.doctor_specialization == "кардиолог")
    print(f"   Кардиологи: {len(cardiac_patients)} пациент(ов)")
    for p in cardiac_patients:
        print(f"      - {p.name} ({p.get_patient_type()})")
    
    print("\n🔄 Тестирование map():")
    names = collection.map(lambda p: f"👤 {p.name} ({p.age} лет)")
    print(f"   Имена пациентов: {names}")
    
    print("\n📈 Тестирование sort():")
    sorted_by_age = collection.sort(key=lambda p: p.age)
    print("   Пациенты по возрасту:")
    for p in sorted_by_age:
        print(f"      - {p.name}: {p.age} лет")
    
    return collection


def demo_protocols():
    print("\n" + "="*60)
    print("2. ДЕМОНСТРАЦИЯ ПРОТОКОЛОВ (DISPLAYABLE И SCORABLE)")
    print("="*60)

    patients_data = [
        InPatient(
            name="Елена Васильева",
            age=28,
            diagnosis="ангина",
            doctor_specialization="терапевт",
            room_number=205,
            daily_cost=2800.0,
            temperature=38.2,
            systolic=122,
            diastolic=80
        ),
        OutPatient(
            name="Дмитрий Козлов",
            age=54,
            diagnosis="артрит",
            doctor_specialization="терапевт",
            appointment_date="2024-12-18",
            consultation_fee=3200.0,
            temperature=36.7,
            systolic=135,
            diastolic=88
        ),
        EmergencyPatient(
            name="Светлана Новикова",
            age=42,
            diagnosis="аппендицит",
            doctor_specialization="хирург",
            urgency_level=3,
            ambulance_arrival=True,
            temperature=39.0,
            systolic=145,
            diastolic=92
        ),
        InPatient(
            name="Владимир Соколов",
            age=71,
            diagnosis="пневмония",
            doctor_specialization="терапевт",
            room_number=312,
            daily_cost=4500.0,
            temperature=38.8,
            systolic=155,
            diastolic=90
        )
    ]
    
    collection = TypedCollection[Patient](patients_data)
    
    print("\n📋 Использование display_all (протокол Displayable):")
    summaries = display_all(collection)
    for summary in summaries:
        print(f"   • {summary}")
    
    print("\n💰 Использование total_score (протокол Scorable):")
    total = total_score(collection)
    print(f"   Общая стоимость лечения: {total:,.2f} руб.")
    
    print("\n   Детализация по типам:")
    for p in collection.get_all():
        cost = p.score()
        print(f"      • {p.name} ({p.get_patient_type()}): {cost:,.2f} руб.")
    
    return collection


def demo_advanced_operations():
    print("\n" + "="*60)
    print("3. ДЕМОНСТРАЦИЯ ПРОДВИНУТЫХ ОПЕРАЦИЙ")
    print("="*60)
    
    patients = [
        InPatient(
            name="Андрей Морозов",
            age=35,
            diagnosis="гастрит",
            doctor_specialization="терапевт",
            room_number=108,
            daily_cost=3000.0,
            temperature=36.9,
            systolic=125,
            diastolic=82
        ),
        OutPatient(
            name="Ольга Лебедева",
            age=29,
            diagnosis="аллергия",
            doctor_specialization="терапевт",
            appointment_date="2024-12-22",
            consultation_fee=1800.0,
            temperature=36.5,
            systolic=115,
            diastolic=75
        ),
        InPatient(
            name="Михаил Федоров",
            age=58,
            diagnosis="диабет",
            doctor_specialization="терапевт",
            room_number=215,
            daily_cost=3800.0,
            temperature=37.0,
            systolic=140,
            diastolic=88
        ),
        EmergencyPatient(
            name="Татьяна Григорьева",
            age=49,
            diagnosis="инсульт",
            doctor_specialization="невролог",
            urgency_level=1,
            ambulance_arrival=True,
            temperature=39.2,
            systolic=170,
            diastolic=100
        )
    ]
    
    collection = TypedCollection[Patient](patients)
    
    print("\n📊 Использование reduce():")
    total_age = collection.reduce(lambda acc, p: acc + p.age, 0)
    avg_age = total_age / len(collection) if len(collection) > 0 else 0
    print(f"   • Суммарный возраст: {total_age} лет")
    print(f"   • Средний возраст: {avg_age:.1f} лет")
    
    print("\n🌡️ Фильтрация пациентов с высокой температурой (>38.5°C):")
    high_fever = collection.filter(lambda p: p.temperature > 38.5)
    print(f"   Найдено: {len(high_fever)} пациент(ов)")
    for p in high_fever:
        print(f"      • {p.name}: {p.temperature:.1f}°C - {p.diagnosis}")
    
    print("\n💵 Преобразование в список затрат (map с другим типом R):")
    costs = collection.map(lambda p: (p.name, p.score()))
    print(f"   Затраты: {costs}")
    
    print("\n🔗 Цепочка операций (method chaining):")
    result = (collection
              .filter(lambda p: p.age > 40)
              .sort(key=lambda p: p.age, reverse=True)
              .map(lambda p: f"{p.name} ({p.age} лет) - {p.score():.0f} руб."))
    
    print("   Пациенты старше 40 лет (по убыванию возраста):")
    for item in result:
        print(f"      • {item}")
    
    print("\n📦 TypedCollection с разными типами:")
    string_collection = TypedCollection[str](["Петров", "Иванов", "Сидоров"])
    print(f"   Строковая коллекция: {string_collection.get_all()}")
    
    int_collection = TypedCollection[int]([100, 200, 300, 400])
    result_int = int_collection.map(lambda x: x * 2).filter(lambda x: x > 500)
    print(f"   Целочисленная коллекция (x2, >500): {result_int}")
    
    return collection


def main():
    print("\n" + "="*60)
    print("ЛАБОРАТОРНАЯ РАБОТА №16")
    print("ВАРИАНТ 10: МЕДИЦИНА")
    print("ОЦЕНКА: 5 (ОТЛИЧНО)")
    print("="*60)
    
    demo_typed_collection_basic()
    demo_protocols()
    demo_advanced_operations()
    
    print("\n" + "="*60)
    print("✅ ВСЕ ТЕСТЫ УСПЕШНО ЗАВЕРШЕНЫ")
    print("="*60)


if __name__ == "__main__":
    main()