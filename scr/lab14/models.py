from base import Patient


class InPatient(Patient):
    def __init__(
        self,
        name,
        age,
        diagnosis,
        doctor_specialization,
        room_number,
        daily_cost,
        temperature=36.6,
        systolic=120,
        diastolic=80
    ):
        super().__init__(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.room_number = room_number
        self.daily_cost = daily_cost
        self.add_treatment_note(f"Пациент размещён в палате {self.room_number}")

        if self.temperature >= 39:
            self._update_status("критическое состояние")
        elif self.temperature >= 38:
            self._update_status("на лечении")

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, value):
        if not isinstance(value, int):
            raise ValueError("Номер палаты должен быть целым числом")
        if value <= 0:
            raise ValueError("Номер палаты должен быть положительным")
        self.__room_number = value

    @property
    def daily_cost(self):
        return self.__daily_cost

    @daily_cost.setter
    def daily_cost(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Стоимость дня должна быть числом")
        if value <= 0:
            raise ValueError("Стоимость дня должна быть положительной")
        self.__daily_cost = float(value)

    def move_to_room(self, new_room):
        old_room = self.__room_number
        self.room_number = new_room
        self.add_treatment_note(
            f"Перевод в другую палату: {old_room} → {self.__room_number}"
        )

    def calculate_cost(self):
        days = self.days_in_hospital
        if isinstance(days, str):
            return 0.0
        days_for_payment = max(1, days)
        return days_for_payment * self.__daily_cost

    def process(self):
        return (
            f"Стационарный пациент {self.name} проходит лечение "
            f"в палате №{self.__room_number}"
        )

    def get_patient_type(self):
        return "InPatient"

    def to_string(self) -> str:
        return f"[СТАЦИОНАР] {self.name} | Возраст: {self.age} | Палата: {self.__room_number} | Диагноз: {self.diagnosis} | Стоимость/день: {self.__daily_cost:.2f} руб."

    def compare_to(self, other) -> int:
        if not isinstance(other, InPatient):
            return super().compare_to(other)
        if self.room_number < other.room_number:
            return -1
        elif self.room_number > other.room_number:
            return 1
        else:
            return 0

    def get_medical_summary(self) -> str:
        return f"[Стационар] {self.name} | Палата {self.__room_number} | {self.diagnosis} | Стоимость: {self.calculate_cost():.2f} руб."

    def __str__(self):
        return (
            super().__str__()
            + f"\nТип пациента: СТАЦИОНАРНЫЙ"
            + f"\nПалата: {self.__room_number}"
            + f"\nСтоимость дня: {self.__daily_cost:.2f} руб."
            + f"\nПредварительная стоимость: {self.calculate_cost():.2f} руб."
        )

    def __repr__(self):
        return (
            f"InPatient(name='{self.name}', age={self.age}, "
            f"diagnosis='{self.diagnosis}', doctor='{self.doctor_specialization}', "
            f"room_number={self.__room_number}, daily_cost={self.__daily_cost})"
        )


class OutPatient(Patient):
    def __init__(
        self,
        name,
        age,
        diagnosis,
        doctor_specialization,
        appointment_date,
        consultation_fee,
        temperature=36.6,
        systolic=120,
        diastolic=80
    ):
        super().__init__(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.appointment_date = appointment_date
        self.consultation_fee = consultation_fee
        self.add_treatment_note(
            f"Назначен амбулаторный приём на дату: {self.appointment_date}"
        )

        if self.temperature >= 39:
            self._update_status("критическое состояние")
        elif self.temperature >= 38:
            self._update_status("на лечении")

    @property
    def appointment_date(self):
        return self.__appointment_date

    @appointment_date.setter
    def appointment_date(self, value):
        if not isinstance(value, str):
            raise ValueError("Дата приёма должна быть строкой")
        value = value.strip()
        if not value:
            raise ValueError("Дата приёма не может быть пустой")
        self.__appointment_date = value

    @property
    def consultation_fee(self):
        return self.__consultation_fee

    @consultation_fee.setter
    def consultation_fee(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Стоимость консультации должна быть числом")
        if value <= 0:
            raise ValueError("Стоимость консультации должна быть положительной")
        self.__consultation_fee = float(value)

    def reschedule_appointment(self, new_date):
        old_date = self.__appointment_date
        self.appointment_date = new_date
        self.add_treatment_note(
            f"Дата приёма изменена: {old_date} → {self.__appointment_date}"
        )

    def calculate_cost(self):
        return self.__consultation_fee

    def process(self):
        return (
            f"Амбулаторный пациент {self.name} записан на приём "
            f"на {self.__appointment_date}"
        )

    def get_patient_type(self):
        return "OutPatient"

    def to_string(self) -> str:
        return f"[АМБУЛАТОР] {self.name} | Возраст: {self.age} | Дата приёма: {self.__appointment_date} | Диагноз: {self.diagnosis} | Стоимость: {self.__consultation_fee:.2f} руб."

    def compare_to(self, other) -> int:
        if not isinstance(other, OutPatient):
            return super().compare_to(other)
        if self.appointment_date < other.appointment_date:
            return -1
        elif self.appointment_date > other.appointment_date:
            return 1
        else:
            return 0

    def get_medical_summary(self) -> str:
        return f"[Амбулатор] {self.name} | Приём {self.__appointment_date} | Стоимость: {self.__consultation_fee:.2f} руб."

    def __str__(self):
        return (
            super().__str__()
            + f"\nТип пациента: АМБУЛАТОРНЫЙ"
            + f"\nДата приёма: {self.__appointment_date}"
            + f"\nСтоимость консультации: {self.__consultation_fee:.2f} руб."
        )

    def __repr__(self):
        return (
            f"OutPatient(name='{self.name}', age={self.age}, "
            f"diagnosis='{self.diagnosis}', doctor='{self.doctor_specialization}', "
            f"appointment_date='{self.__appointment_date}', "
            f"consultation_fee={self.__consultation_fee})"
        )


class EmergencyPatient(Patient):
    def __init__(
        self,
        name,
        age,
        diagnosis,
        doctor_specialization,
        urgency_level,
        ambulance_arrival,
        temperature=36.6,
        systolic=120,
        diastolic=80
    ):
        super().__init__(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.urgency_level = urgency_level
        self.ambulance_arrival = ambulance_arrival
        self.add_treatment_note(
            f"Экстренное поступление. Срочность: {self.urgency_level}"
        )

        if self.temperature >= 39:
            self._update_status("критическое состояние")
        elif self.temperature >= 38:
            self._update_status("на лечении")

    @property
    def urgency_level(self):
        return self.__urgency_level

    @urgency_level.setter
    def urgency_level(self, value):
        if not isinstance(value, int):
            raise ValueError("Уровень срочности должен быть целым числом")
        if value < 1 or value > 5:
            raise ValueError("Уровень срочности должен быть от 1 до 5")
        self.__urgency_level = value

    @property
    def ambulance_arrival(self):
        return self.__ambulance_arrival

    @ambulance_arrival.setter
    def ambulance_arrival(self, value):
        if not isinstance(value, bool):
            raise ValueError("Поле ambulance_arrival должно быть True или False")
        self.__ambulance_arrival = value

    def increase_urgency(self):
        if self.__urgency_level > 1:
            old_level = self.__urgency_level
            self.__urgency_level -= 1
            self.add_treatment_note(
                f"Повышен уровень срочности: {old_level} → {self.__urgency_level}"
            )

    def calculate_cost(self):
        base_cost = 5000.0
        extra = (6 - self.__urgency_level) * 1500.0
        ambulance_fee = 2000.0 if self.__ambulance_arrival else 0.0
        return base_cost + extra + ambulance_fee

    def process(self):
        arrival_text = (
            "доставлен скорой помощью"
            if self.__ambulance_arrival else
            "прибыл самостоятельно"
        )
        return (
            f"Экстренный пациент {self.name} ({arrival_text}), "
            f"уровень срочности: {self.__urgency_level}"
        )

    def get_patient_type(self):
        return "EmergencyPatient"

    def to_string(self) -> str:
        ambulance_text = "скорая: да" if self.__ambulance_arrival else "скорая: нет"
        return f"[ЭКСТРЕННЫЙ] {self.name} | Возраст: {self.age} | Срочность: {self.__urgency_level} | {ambulance_text} | Диагноз: {self.diagnosis} | Стоимость: {self.calculate_cost():.2f} руб."

    def compare_to(self, other) -> int:
        if not isinstance(other, EmergencyPatient):
            return super().compare_to(other)
        if self.urgency_level < other.urgency_level:
            return -1
        elif self.urgency_level > other.urgency_level:
            return 1
        else:
            return 0

    def get_medical_summary(self) -> str:
        return f"[Экстренный] {self.name} | Срочность: {self.__urgency_level} | Скорая: {self.__ambulance_arrival} | Стоимость: {self.calculate_cost():.2f} руб."

    def __str__(self):
        ambulance_text = "Да" if self.__ambulance_arrival else "Нет"
        return (
            super().__str__()
            + f"\nТип пациента: ЭКСТРЕННЫЙ"
            + f"\nУровень срочности: {self.__urgency_level}"
            + f"\nДоставка скорой помощью: {ambulance_text}"
            + f"\nПредварительная стоимость: {self.calculate_cost():.2f} руб."
        )

    def __repr__(self):
        return (
            f"EmergencyPatient(name='{self.name}', age={self.age}, "
            f"diagnosis='{self.diagnosis}', doctor='{self.doctor_specialization}', "
            f"urgency_level={self.__urgency_level}, "
            f"ambulance_arrival={self.__ambulance_arrival})"
        )