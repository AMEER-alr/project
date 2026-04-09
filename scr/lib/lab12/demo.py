from model import Patient
from collection import PatientCollection


def print_title(text):
    print(f"\n=== {text} ===")


def main():
    print_title("SCENARIO 1: Создание и добавление")

    p1 = Patient("Иван Петров", 35, "Бронхит", "терапевт")
    p2 = Patient("Мария Иванова", 28, "Гипертония", "кардиолог")
    p3 = Patient("Петр Сидоров", 75, "Пневмония", "терапевт")
    p4 = Patient("Анна Смирнова", 45, "Диабет", "эндокринолог")

    collection = PatientCollection()

    collection.add(p1)
    collection.add(p2)
    collection.add(p3)
    collection.add(p4)

    for p in collection:
        print(p.name, p.age)

    print_title("SCENARIO 2: Поиск и доступ")

    print("Поиск по имени:")
    for p in collection.find_by_name("Иван Петров"):
        print(p.name)

    print("Поиск по ID:")
    found = collection.find_by_id(p2.patient_id)
    print(found.name if found else "Не найден")

    print("Поиск по диагнозу:")
    for p in collection.find_by_diagnosis("пнев"):
        print(p.name, "-", p.diagnosis)

    print("Длина коллекции:", len(collection))
    print("Первый элемент:", collection[0].name)

    print_title("SCENARIO 3: Фильтрация")

    p2.admit_to_hospital()
    p3.temperature = 39.2

    treated = collection.get_on_treatment()
    critical = collection.get_critical()
    active = collection.get_active()

    print("На лечении:")
    for p in treated:
        print(p.name)

    print("Критическое состояние:")
    for p in critical:
        print(p.name)

    print("Активные:")
    for p in active:
        print(p.name)

    print_title("SCENARIO 4: Сортировка")

    print("Сортировка по возрасту:")
    collection.sort_by_age()
    for p in collection:
        print(p.name, p.age)

    print("\nСортировка по имени:")
    collection.sort_by_name()
    for p in collection:
        print(p.name)

    print_title("SCENARIO 5: Удаление")

    temp_collection = PatientCollection()
    temp_collection.add(p1)
    temp_collection.add(p2)
    temp_collection.add(p3)
    temp_collection.add(p4)

    print("До удаления:")
    for p in temp_collection:
        print(p.name)

    temp_collection.remove(p1)
    print("\nПосле remove(p1):")
    for p in temp_collection:
        print(p.name)

    temp_collection.remove_at(0)
    print("\nПосле remove_at(0):")
    for p in temp_collection:
        print(p.name)

    print_title("SCENARIO 6: Ошибки")

    try:
        collection.add(p2)
    except Exception as e:
        print("Duplicate ошибка:", e)

    try:
        collection.add("не пациент")
    except Exception as e:
        print("Type ошибка:", e)

    try:
        collection.remove_at(100)
    except Exception as e:
        print("Index ошибка:", e)


if __name__ == "__main__":
    main()