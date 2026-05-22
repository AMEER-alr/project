from base import Patient


class InPatient(Patient):
    def __init__(
        self,
        name: str,
        age: int,
        diagnosis: str,
        doctor_specialization: str,
        room_number: int,
        daily_cost: float,
        temperature: float = 36.6,
        systolic: int = 120,
        diastolic: int = 80
    ) -> None:
        super().__init__(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.room_number: int = room_number
        self.daily_cost: float = daily_cost
        self.add_treatment_note(f"Пациент размещён в палате {self.__room_number}")

        if self.temperature >= 39:
            self._update_status("критическое состояние")
        elif self.temperature >= 38:
            self._update_status("на лечении")

    @property
    def room_number(self) -> int:
        return self.__room_number

    @room_number.setter
    def room_number(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Номер палаты должен быть целым числом")
        if value <= 0:
            raise ValueError("Номер палаты должен быть положительным")
        self.__room_number: int = value

    @property
    def daily_cost(self) -> float:
        return self.__daily_cost

    @daily_cost.setter
    def daily_cost(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("Стоимость дня должна быть числом")
        if value <= 0:
            raise ValueError("Стоимость дня должна быть положительной")
        self.__daily_cost: float = float(value)

    def move_to_room(self, new_room: int) -> None:
        old_room: int = self.__room_number
        self.room_number = new_room
        self.add_treatment_note(
            f"Перевод в другую палату: {old_room} → {self.__room_number}"
        )

    def calculate_cost(self) -> float:
        days = self.days_in_hospital
        if isinstance(days, str):
            return 0.0
        days_for_payment: int = max(1, days)
        return days_for_payment * self.__daily_cost

    def process(self) -> str:
        return (
            f"Стационарный пациент {self.name} проходит лечение "
            f"в палате №{self.__room_number}"
        )

    def get_patient_type(self) -> str:
        return "InPatient"

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"\nТип пациента: СТАЦИОНАРНЫЙ"
            + f"\nПалата: {self.__room_number}"
            + f"\nСтоимость дня: {self.__daily_cost:.2f} руб."
            + f"\nПредварительная стоимость: {self.calculate_cost():.2f} руб."
        )

    def __repr__(self) -> str:
        return (
            f"InPatient(name='{self.name}', age={self.age}, "
            f"diagnosis='{self.diagnosis}', doctor='{self.doctor_specialization}', "
            f"room_number={self.__room_number}, daily_cost={self.__daily_cost})"
        )


class OutPatient(Patient):
    def __init__(
        self,
        name: str,
        age: int,
        diagnosis: str,
        doctor_specialization: str,
        appointment_date: str,
        consultation_fee: float,
        temperature: float = 36.6,
        systolic: int = 120,
        diastolic: int = 80
    ) -> None:
        super().__init__(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.appointment_date: str = appointment_date
        self.consultation_fee: float = consultation_fee
        self.add_treatment_note(
            f"Назначен амбулаторный приём на дату: {self.__appointment_date}"
        )

        if self.temperature >= 39:
            self._update_status("критическое состояние")
        elif self.temperature >= 38:
            self._update_status("на лечении")

    @property
    def appointment_date(self) -> str:
        return self.__appointment_date

    @appointment_date.setter
    def appointment_date(self, value: str) -> None:
        if not isinstance(value, str):
            raise ValueError("Дата приёма должна быть строкой")
        value = value.strip()
        if not value:
            raise ValueError("Дата приёма не может быть пустой")
        self.__appointment_date: str = value

    @property
    def consultation_fee(self) -> float:
        return self.__consultation_fee

    @consultation_fee.setter
    def consultation_fee(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise ValueError("Стоимость консультации должна быть числом")
        if value <= 0:
            raise ValueError("Стоимость консультации должна быть положительной")
        self.__consultation_fee: float = float(value)

    def reschedule_appointment(self, new_date: str) -> None:
        old_date: str = self.__appointment_date
        self.appointment_date = new_date
        self.add_treatment_note(
            f"Дата приёма изменена: {old_date} → {self.__appointment_date}"
        )

    def calculate_cost(self) -> float:
        return self.__consultation_fee

    def process(self) -> str:
        return (
            f"Амбулаторный пациент {self.name} записан на приём "
            f"на {self.__appointment_date}"
        )

    def get_patient_type(self) -> str:
        return "OutPatient"

    def __str__(self) -> str:
        return (
            super().__str__()
            + f"\nТип пациента: АМБУЛАТОРНЫЙ"
            + f"\nДата приёма: {self.__appointment_date}"
            + f"\nСтоимость консультации: {self.__consultation_fee:.2f} руб."
        )

    def __repr__(self) -> str:
        return (
            f"OutPatient(name='{self.name}', age={self.age}, "
            f"diagnosis='{self.diagnosis}', doctor='{self.doctor_specialization}', "
            f"appointment_date='{self.__appointment_date}', "
            f"consultation_fee={self.__consultation_fee})"
        )


class EmergencyPatient(Patient):
    def __init__(
        self,
        name: str,
        age: int,
        diagnosis: str,
        doctor_specialization: str,
        urgency_level: int,
        ambulance_arrival: bool,
        temperature: float = 36.6,
        systolic: int = 120,
        diastolic: int = 80
    ) -> None:
        super().__init__(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.urgency_level: int = urgency_level
        self.ambulance_arrival: bool = ambulance_arrival
        self.add_treatment_note(
            f"Экстренное поступление. Срочность: {self.__urgency_level}"
        )

        if self.temperature >= 39:
            self._update_status("критическое состояние")
        elif self.temperature >= 38:
            self._update_status("на лечении")

    @property
    def urgency_level(self) -> int:
        return self.__urgency_level

    @urgency_level.setter
    def urgency_level(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Уровень срочности должен быть целым числом")
        if value < 1 or value > 5:
            raise ValueError("Уровень срочности должен быть от 1 до 5")
        self.__urgency_level: int = value

    @property
    def ambulance_arrival(self) -> bool:
        return self.__ambulance_arrival

    @ambulance_arrival.setter
    def ambulance_arrival(self, value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError("Поле ambulance_arrival должно быть True или False")
        self.__ambulance_arrival: bool = value

    def increase_urgency(self) -> None:
        if self.__urgency_level > 1:
            old_level: int = self.__urgency_level
            self.__urgency_level -= 1
            self.add_treatment_note(
                f"Повышен уровень срочности: {old_level} → {self.__urgency_level}"
            )

    def calculate_cost(self) -> float:
        base_cost: float = 5000.0
        extra: float = (6 - self.__urgency_level) * 1500.0
        ambulance_fee: float = 2000.0 if self.__ambulance_arrival else 0.0
        return base_cost + extra + ambulance_fee

    def process(self) -> str:
        arrival_text: str = (
            "доставлен скорой помощью"
            if self.__ambulance_arrival else
            "прибыл самостоятельно"
        )
        return (
            f"Экстренный пациент {self.name} ({arrival_text}), "
            f"уровень срочности: {self.__urgency_level}"
        )

    def get_patient_type(self) -> str:
        return "EmergencyPatient"

    def __str__(self) -> str:
        ambulance_text: str = "Да" if self.__ambulance_arrival else "Нет"
        return (
            super().__str__()
            + f"\nТип пациента: ЭКСТРЕННЫЙ"
            + f"\nУровень срочности: {self.__urgency_level}"
            + f"\nДоставка скорой помощью: {ambulance_text}"
            + f"\nПредварительная стоимость: {self.calculate_cost():.2f} руб."
        )

    def __repr__(self) -> str:
        return (
            f"EmergencyPatient(name='{self.name}', age={self.age}, "
            f"diagnosis='{self.diagnosis}', doctor='{self.doctor_specialization}', "
            f"urgency_level={self.__urgency_level}, "
            f"ambulance_arrival={self.__ambulance_arrival})"
        )