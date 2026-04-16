from model import Patient
from datetime import datetime

def print_header(text):
    print("\n" + "="*70)
    print(f"    {text}")
    print("="*70)

def print_subheader(text):
    print(f"\n--- {text} ---")

def wait_for_user():
    input("\nНажмите Enter для продолжения...")

def main():

    print_header("ЛАБОРАТОРНАЯ РАБОТА №11")
    print_header("Класс Patient - демонстрация всех возможностей")
    print("Тема: Медицина (Больничная информационная система)")
    print(f"Дата выполнения: {datetime.now().strftime('%d.%m.%Y %H:%M')}")

    print_header("1. СОЗДАНИЕ КАРТ ПАЦИЕНТОВ")
    
    print_subheader("Создание пациента с параметрами по умолчанию")
    patient1 = Patient(
        name="Иван Петров",
        age=35,
        diagnosis="Острый бронхит",
        doctor_specialization="терапевт"
    )
    print(patient1)
    
    print_subheader("Создание пациента с полными параметрами")
    patient2 = Patient(
        name="Мария Иванова",
        age=28,
        diagnosis="Гипертоническая болезнь",
        doctor_specialization="кардиолог",
        temperature=37.8,
        systolic=150,
        diastolic=95
    )
    print(patient2)
    
    print_subheader("Создание пожилого пациента")
    patient3 = Patient(
        name="Петр Сидоров",
        age=75,
        diagnosis="Пневмония",
        doctor_specialization="терапевт",
        temperature=38.5,
        systolic=160,
        diastolic=90
    )
    print(patient3)
    
    wait_for_user()

    print_header("2. ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ (ОБРАБОТКА ОШИБОК)")
    
    test_cases = [
        ("пустое имя", "", 30, "ОРВИ", "терапевт"),
        ("имя из пробелов", "   ", 30, "ОРВИ", "терапевт"),
        ("слишком короткое имя", "А", 30, "ОРВИ", "терапевт"),
        ("имя с цифрами", "Иван123", 30, "ОРВИ", "терапевт"),
        ("имя со спецсимволами", "Иван@#$", 30, "ОРВИ", "терапевт"),
    ]
    
    for description, name, age, diagnosis, doctor in test_cases:
        print_subheader(f"Попытка создать пациента с {description}")
        try:
            p = Patient(name, age, diagnosis, doctor)
            print(f"СОЗДАН: {p.name}")
        except ValueError as e:
            print(f"ОШИБКА: {e}")
    
    print_subheader("Проверка возраста")
    try:
        p = Patient("Тест Тестов", -5, "ОРВИ", "терапевт")
    except ValueError as e:
        print(f"Отрицательный возраст: {e}")
    
    try:
        p = Patient("Тест Тестов", 200, "ОРВИ", "терапевт")
    except ValueError as e:
        print(f"Возраст > 150: {e}")
    
    print_subheader("Проверка температуры")
    try:
        p = Patient("Тест Тестов", 30, "ОРВИ", "терапевт", temperature=50)
    except ValueError as e:
        print(f"Температура 50°C: {e}")
    
    print_subheader("Проверка давления")
    try:
        p = Patient("Тест Тестов", 30, "ОРВИ", "терапевт", systolic=80, diastolic=100)
    except ValueError as e:
        print(f"Систолическое < диастолического: {e}")
    
    wait_for_user()

    print_header("3. ДЕМОНСТРАЦИЯ СВОЙСТВ (GETTERS/SETTERS)")
    
    demo_patient = Patient(
        name="Анна Смирнова",
        age=45,
        diagnosis="Сахарный диабет",
        doctor_specialization="эндокринолог",
        temperature=36.8,
        systolic=125,
        diastolic=82
    )
    
    print("Исходный пациент:")
    print(demo_patient)
    
    print_subheader("Изменение свойств через сеттеры")
    
    print("\nИзменяем имя на 'Анна Петровна Смирнова'")
    demo_patient.name = "Анна Петровна Смирнова"
    print(f"Новое имя: {demo_patient.name}")
    
    print("\nИзменяем возраст на 46 лет")
    demo_patient.age = 46
    print(f"Новый возраст: {demo_patient.age}")
    
    print("\nИзменяем диагноз на 'Сахарный диабет 2 типа'")
    demo_patient.diagnosis = "Сахарный диабет 2 типа"
    print(f"Новый диагноз: {demo_patient.diagnosis}")
    
    print("\nПробуем изменить patient_id напрямую")
    try:
        demo_patient.patient_id = "NEW123"
    except AttributeError as e:
        print(f"ОШИБКА: {e} - patient_id доступен только для чтения")
    
    wait_for_user()

    print_header("4. ДЕМОНСТРАЦИЯ МЕДИЦИНСКИХ ОПЕРАЦИЙ")
    
    treatment_patient = Patient(
        name="Сергей Козлов",
        age=52,
        diagnosis="Гипертония",
        doctor_specialization="кардиолог",
        temperature=36.8,
        systolic=145,
        diastolic=95
    )
    
    print("Начальное состояние:")
    print(treatment_patient)
    
    print_subheader("Обновление жизненных показателей")
    print("Обновляем температуру (37.2) и давление (135/85)")
    treatment_patient.update_vitals(temperature=37.2, systolic=135, diastolic=85)
    print("Показатели обновлены")
    print(f"Температура: {treatment_patient.temperature}°C")
    print(f"Давление: {treatment_patient.systolic}/{treatment_patient.diastolic}")
    
    print_subheader("Добавление заметок о лечении")
    treatment_patient.add_treatment_note("Назначен препарат Эналаприл 5мг 2 раза в день")
    treatment_patient.add_treatment_note("Рекомендована диета с ограничением соли")
    print(f"Добавлено 2 заметки. Всего записей: {len(treatment_patient)}")
    
    print_subheader("Попытка некорректной операции")
    try:
        treatment_patient.update_vitals(temperature=50)
    except ValueError as e:
        print(f"ОШИБКА: {e}")
    
    wait_for_user()

    print_header("5. ДЕМОНСТРАЦИЯ ИЗМЕНЕНИЯ СТАТУСОВ")
    
    status_patient = Patient(
        name="Ольга Новикова",
        age=34,
        diagnosis="Острый аппендицит",
        doctor_specialization="хирург",
        temperature=38.2
    )
    
    print(f"Исходный статус: {status_patient.status}")
    
    print_subheader("Госпитализация")
    status_patient.admit_to_hospital()
    print(f"Статус после госпитализации: {status_patient.status}")
    
    print_subheader("Операция с госпитализированным пациентом")
    status_patient.add_treatment_note("Проведена аппендэктомия")
    print("Заметка добавлена успешно")
    
    print_subheader("Выписка пациента")
    try:
        status_patient.discharge()
        print(f"Статус после выписки: {status_patient.status}")
        print(f"Дата выписки: {status_patient.discharge_date.strftime('%d.%m.%Y')}")
        print(f"Дней в больнице: {status_patient.days_in_hospital}")
    except ValueError as e:
        print(f"ОШИБКА: {e}")
    
    print_subheader("Попытка операции с выписанным пациентом")
    try:
        status_patient.add_treatment_note("Новая заметка")
    except ValueError as e:
        print(f"ОШИБКА: {e}")
    
    wait_for_user()

    print_header("6. ДЕМОНСТРАЦИЯ КРИТИЧЕСКИХ СЛУЧАЕВ")
    
    critical_patient = Patient(
        name="Николай Федоров",
        age=82,
        diagnosis="Инфаркт миокарда",
        doctor_specialization="кардиолог",
        temperature=39.5,
        systolic=180,
        diastolic=110
    )
    
    print("Пациент в критическом состоянии:")
    print(critical_patient)
    
    print_subheader("Попытка выписки критического пациента")
    try:
        critical_patient.discharge()
    except ValueError as e:
        print(f"ОШИБКА: {e}")
    
    print_subheader("Отметка о смерти пациента")
    critical_patient.mark_as_deceased()
    print(f"Статус: {critical_patient.status}")
    print(f"Дней в больнице: {critical_patient.days_in_hospital}")
    
    print_subheader("Попытка операции с умершим пациентом")
    try:
        critical_patient.update_vitals(temperature=36.6)
    except ValueError as e:
        print(f"ОШИБКА: {e}")
    
    wait_for_user()

    print_header("7. ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ")
    
    print_subheader("Метод __str__ (для пользователей)")
    magic_patient = Patient(
        name="Елена Васильева",
        age=29,
        diagnosis="ОРВИ",
        doctor_specialization="терапевт"
    )
    print(magic_patient)
    
    print_subheader("Метод __repr__ (для разработчиков)")
    print(repr(magic_patient))
    
    print_subheader("Метод __eq__ (сравнение пациентов)")
    p1 = Patient("Пациент Один", 40, "Диагноз 1", "терапевт")
    p2 = Patient("Пациент Два", 40, "Диагноз 2", "хирург")
    p3 = p1
    
    print(f"p1 == p2: {p1 == p2} (разные ID)")
    print(f"p1 == p3: {p1 == p3} (один и тот же объект)")
    
    print_subheader("Метод __lt__ (сравнение по возрасту)")
    young = Patient("Молодой", 25, "ОРВИ", "терапевт")
    old = Patient("Пожилой", 70, "Гипертония", "кардиолог")
    
    print(f"Молодой (25) < Пожилой (70): {young < old}")
    print(f"Пожилой (70) < Молодой (25): {old < young}")
    
    print_subheader("Сортировка пациентов по возрасту")
    patients = [
        Patient("Анна", 45, "Диагноз", "терапевт"),
        Patient("Борис", 30, "Диагноз", "хирург"),
        Patient("Виктор", 60, "Диагноз", "кардиолог")
    ]
    
    print("До сортировки:")
    for p in patients:
        print(f"  {p.name}: {p.age} лет")
    
    sorted_patients = sorted(patients)
    print("После сортировки (по возрасту):")
    for p in sorted_patients:
        print(f"  {p.name}: {p.age} лет")
    
    print_subheader("Метод __len__ (количество записей)")
    test_patient = Patient("Тест", 50, "Тест", "терапевт")
    test_patient.add_treatment_note("Запись 1")
    test_patient.add_treatment_note("Запись 2")
    test_patient.add_treatment_note("Запись 3")
    print(f"Количество записей в истории: {len(test_patient)}")
if __name__ == "__main__":
    main()