from models import InPatient, OutPatient, EmergencyPatient


def print_header(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def print_subheader(title):
    print("\n" + "-" * 60)
    print(title)
    print("-" * 60)


def show_collection(objects, title):
    print_header(title)
    for i, obj in enumerate(objects, start=1):
        print(f"\n[{i}] {obj.get_patient_type()}")
        print(obj)
        print(f"process() -> {obj.process()}")
        print(f"calculate_cost() -> {obj.calculate_cost():.2f} руб.")
        print(f"summary -> {obj.get_summary()}")


def get_only_inpatients(objects):
    return [obj for obj in objects if isinstance(obj, InPatient)]


def get_only_outpatients(objects):
    return [obj for obj in objects if isinstance(obj, OutPatient)]


def get_only_emergency(objects):
    return [obj for obj in objects if isinstance(obj, EmergencyPatient)]


def get_only_active(objects):
    return [obj for obj in objects if obj.status == "активен"]


def scenario_1_create_objects():
    print_header("СЦЕНАРИЙ 1. СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ")

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
    show_collection(patients, "Созданные объекты")
    return patients


def scenario_2_polymorphism_and_override(patients):
    print_header("СЦЕНАРИЙ 2. ПОЛИМОРФИЗМ И ПЕРЕОПРЕДЕЛЕНИЕ МЕТОДОВ")

    for patient in patients:
        print_subheader(f"Обработка: {patient.name}")
        print(f"Тип объекта: {patient.get_patient_type()}")
        print(f"process(): {patient.process()}")
        print(f"calculate_cost(): {patient.calculate_cost():.2f} руб.")


def scenario_3_isinstance_and_filter(patients):
    print_header("СЦЕНАРИЙ 3. ПРОВЕРКА ТИПОВ ЧЕРЕЗ isinstance() И ФИЛЬТРАЦИЯ")

    for patient in patients:
        print_subheader(f"Проверка типа для {patient.name}")

        if isinstance(patient, InPatient):
            print("Это объект класса InPatient")
        if isinstance(patient, OutPatient):
            print("Это объект класса OutPatient")
        if isinstance(patient, EmergencyPatient):
            print("Это объект класса EmergencyPatient")

    inpatients = get_only_inpatients(patients)
    outpatients = get_only_outpatients(patients)
    emergency_patients = get_only_emergency(patients)
    active_patients = get_only_active(patients)

    print_subheader("Только стационарные пациенты")
    for p in inpatients:
        print(f"{p.name} | палата {p.room_number}")

    print_subheader("Только амбулаторные пациенты")
    for p in outpatients:
        print(f"{p.name} | приём {p.appointment_date}")

    print_subheader("Только экстренные пациенты")
    for p in emergency_patients:
        print(f"{p.name} | срочность {p.urgency_level}")

    print_subheader("Только активные пациенты")
    for p in active_patients:
        print(f"{p.name} | статус: {p.status}")


def scenario_4_business_methods(patients):
    print_header("СЦЕНАРИЙ 4. ИСПОЛЬЗОВАНИЕ МЕТОДОВ БАЗОВОГО И ДОЧЕРНИХ КЛАССОВ")

    inpatient = patients[0]
    outpatient = patients[1]
    emergency = patients[2]

    print_subheader("Работа со стационарным пациентом")
    inpatient.move_to_room(205)
    inpatient.add_treatment_note("Назначена капельница")
    inpatient.admit_to_hospital()
    print(inpatient.process())
    print(f"Новая палата: {inpatient.room_number}")

    print_subheader("Работа с амбулаторным пациентом")
    outpatient.reschedule_appointment("2026-04-25")
    outpatient.add_treatment_note("Назначено повторное обследование")
    print(outpatient.process())
    print(f"Новая дата приёма: {outpatient.appointment_date}")

    print_subheader("Работа с экстренным пациентом")
    emergency.update_vitals(temperature=39.5, systolic=180, diastolic=110)
    emergency.add_treatment_note("Пациент направлен в реанимацию")
    print(emergency.process())
    print(f"Текущий уровень срочности: {emergency.urgency_level}")


def scenario_5_sorting_and_len(patients):
    print_header("СЦЕНАРИЙ 5. СОРТИРОВКА И ИСПОЛЬЗОВАНИЕ МЕТОДОВ БАЗОВОГО КЛАССА")

    sorted_patients = sorted(patients)

    print_subheader("Пациенты, отсортированные по возрасту (__lt__)")
    for p in sorted_patients:
        print(f"{p.name} | возраст: {p.age}")

    print_subheader("Количество записей в истории лечения (__len__)")
    for p in patients:
        print(f"{p.name}: {len(p)} записей")


def main():
    patients = scenario_1_create_objects()
    scenario_2_polymorphism_and_override(patients)
    scenario_3_isinstance_and_filter(patients)
    scenario_4_business_methods(patients)
    scenario_5_sorting_and_len(patients)


if __name__ == "__main__":
    main()