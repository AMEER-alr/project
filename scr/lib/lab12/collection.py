from model import Patient


class PatientCollection:
    def __init__(self):
        self._items = []

    def add(self, item):
        if not isinstance(item, Patient):
            raise TypeError("Можно добавлять только объекты Patient")

        for existing in self._items:
            if existing.patient_id == item.patient_id:
                raise ValueError("Пациент с таким ID уже существует")
            if existing.name == item.name:
                raise ValueError("Пациент с таким именем уже существует")

        self._items.append(item)

    def remove(self, item):
        if item not in self._items:
            raise ValueError("Пациент не найден")
        self._items.remove(item)

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        del self._items[index]

    def get_all(self):
        return self._items.copy()

    def find_by_name(self, name):
        return [p for p in self._items if p.name == name]

    def find_by_id(self, patient_id):
        for p in self._items:
            if p.patient_id == patient_id:
                return p
        return None

    def find_by_diagnosis(self, diagnosis):
        return [p for p in self._items if diagnosis.lower() in p.diagnosis.lower()]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self, key):
        self._items.sort(key=key)

    def sort_by_name(self):
        self._items.sort(key=lambda x: x.name)

    def sort_by_age(self):
        self._items.sort(key=lambda x: x.age)

    def sort_by_date(self):
        self._items.sort(key=lambda x: x.admission_date)

    def get_active(self):
        new = PatientCollection()
        for p in self._items:
            if p.status == "активен":
                new.add(p)
        return new

    def get_on_treatment(self):
        new = PatientCollection()
        for p in self._items:
            if p.status == "на лечении":
                new.add(p)
        return new

    def get_critical(self):
        new = PatientCollection()
        for p in self._items:
            if p.status == "критическое состояние":
                new.add(p)
        return new