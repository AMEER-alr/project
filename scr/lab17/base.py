from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List
import validate


class Patient(ABC):
    HOSPITAL_NAME: str = "Городская больница №1"
    MIN_AGE: int = 0
    MAX_AGE: int = 150
    _next_patient_id: int = 1000

    @classmethod
    def get_next_id(cls) -> int:
        return cls._next_patient_id

    @classmethod
    def set_next_id(cls, value: int) -> None:
        cls._next_patient_id = value

    def __init__(
        self,
        name: str,
        age: int,
        diagnosis: str,
        doctor_specialization: str,
        temperature: float = 36.6,
        systolic: int = 120,
        diastolic: int = 80,
        patient_id: Optional[str] = None
    ) -> None:
        self._validate_all(
            name,
            age,
            diagnosis,
            doctor_specialization,
            temperature,
            systolic,
            diastolic
        )

        self.__name: str = name.strip()
        self.__age: int = int(age)
        self.__diagnosis: str = diagnosis.strip()
        self.__doctor_specialization: str = doctor_specialization.strip().lower()
        self.__temperature: float = float(temperature)
        self.__systolic: int = int(systolic)
        self.__diastolic: int = int(diastolic)
        
        if patient_id is not None:
            self.__patient_id: str = patient_id
            id_num = int(patient_id[3:])
            if id_num >= Patient._next_patient_id:
                Patient._next_patient_id = id_num + 1
        else:
            self.__patient_id: str = self._generate_patient_id()
        
        self.__status: str = "активен"
        self.__admission_date: datetime = datetime.now()
        self.__discharge_date: Optional[datetime] = None
        self.__treatment_history: List[str] = []

        self._add_to_history(f"Поступление. Диагноз: {self.__diagnosis}")

    def _validate_all(
        self,
        name: str,
        age: int,
        diagnosis: str,
        doctor_specialization: str,
        temperature: float,
        systolic: int,
        diastolic: int
    ) -> None:
        name_valid, name_msg = validate.validate_name(name)
        if not name_valid:
            raise ValueError(f"Ошибка в имени: {name_msg}")

        age_valid, age_msg = validate.validate_age(age)
        if not age_valid:
            raise ValueError(f"Ошибка в возрасте: {age_msg}")

        diagnosis_valid, diagnosis_msg = validate.validate_diagnosis(diagnosis)
        if not diagnosis_valid:
            raise ValueError(f"Ошибка в диагнозе: {diagnosis_msg}")

        doctor_valid, doctor_msg = validate.validate_doctor_specialization(
            doctor_specialization
        )
        if not doctor_valid:
            raise ValueError(f"Ошибка в специализации врача: {doctor_msg}")

        temp_valid, temp_msg = validate.validate_temperature(temperature)
        if not temp_valid:
            raise ValueError(f"Ошибка в температуре: {temp_msg}")

        pressure_valid, pressure_msg = validate.validate_pressure(
            systolic,
            diastolic
        )
        if not pressure_valid:
            raise ValueError(f"Ошибка в давлении: {pressure_msg}")

    def _generate_patient_id(self) -> str:
        patient_id: str = f"PAT{Patient._next_patient_id}"
        Patient._next_patient_id += 1
        return patient_id

    def _add_to_history(self, event: str) -> None:
        timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__treatment_history.append(f"[{timestamp}] {event}")

    @property
    def patient_id(self) -> str:
        return self.__patient_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def diagnosis(self) -> str:
        return self.__diagnosis

    @property
    def doctor_specialization(self) -> str:
        return self.__doctor_specialization

    @property
    def temperature(self) -> float:
        return self.__temperature

    @property
    def systolic(self) -> int:
        return self.__systolic

    @property
    def diastolic(self) -> int:
        return self.__diastolic

    @property
    def status(self) -> str:
        return self.__status

    @property
    def admission_date(self) -> datetime:
        return self.__admission_date

    @property
    def discharge_date(self) -> Optional[datetime]:
        return self.__discharge_date

    @property
    def days_in_hospital(self):
        if self.__status == "выписан" and self.__discharge_date:
            return (self.__discharge_date - self.__admission_date).days
        elif self.__status == "умер":
            return "Пациент умер"
        else:
            return (datetime.now() - self.__admission_date).days

    @property
    def treatment_history(self) -> List[str]:
        return self.__treatment_history.copy()

    @name.setter
    def name(self, new_name: str) -> None:
        valid, msg = validate.validate_name(new_name)
        if not valid:
            raise ValueError(f"Ошибка в имени: {msg}")

        old_name = self.__name
        self.__name = new_name.strip()
        self._add_to_history(f"Имя изменено с '{old_name}' на '{self.__name}'")

    @age.setter
    def age(self, new_age: int) -> None:
        valid, msg = validate.validate_age(new_age)
        if not valid:
            raise ValueError(f"Ошибка в возрасте: {msg}")

        old_age = self.__age
        self.__age = int(new_age)
        self._add_to_history(f"Возраст изменен с {old_age} на {self.__age}")

    @diagnosis.setter
    def diagnosis(self, new_diagnosis: str) -> None:
        valid, msg = validate.validate_diagnosis(new_diagnosis)
        if not valid:
            raise ValueError(f"Ошибка в диагнозе: {msg}")

        status_valid, status_msg = validate.validate_status_for_operation(
            self.__status,
            "изменить диагноз"
        )
        if not status_valid:
            raise ValueError(status_msg)

        old_diagnosis = self.__diagnosis
        self.__diagnosis = new_diagnosis.strip()
        self._add_to_history(
            f"Диагноз изменен с '{old_diagnosis}' на '{self.__diagnosis}'"
        )

    @doctor_specialization.setter
    def doctor_specialization(self, new_specialization: str) -> None:
        valid, msg = validate.validate_doctor_specialization(new_specialization)
        if not valid:
            raise ValueError(f"Ошибка в специализации: {msg}")

        old_spec = self.__doctor_specialization
        self.__doctor_specialization = new_specialization.strip().lower()
        self._add_to_history(
            f"Специализация врача изменена с '{old_spec}' на '{self.__doctor_specialization}'"
        )

    @temperature.setter
    def temperature(self, new_temperature: float) -> None:
        valid, msg = validate.validate_temperature(new_temperature)
        if not valid:
            raise ValueError(f"Ошибка в температуре: {msg}")

        old_temp = self.__temperature
        self.__temperature = float(new_temperature)

        if self.__temperature >= 39:
            self._update_status("критическое состояние")
        elif self.__temperature >= 38:
            self._update_status("на лечении")

        self._add_to_history(
            f"Температура изменена с {old_temp}°C на {self.__temperature}°C"
        )

    def update_vitals(
        self,
        temperature: Optional[float] = None,
        systolic: Optional[int] = None,
        diastolic: Optional[int] = None
    ) -> None:
        status_valid, status_msg = validate.validate_status_for_operation(
            self.__status,
            "обновить показатели"
        )
        if not status_valid:
            raise ValueError(status_msg)

        changes: List[str] = []

        if temperature is not None:
            valid, msg = validate.validate_temperature(temperature)
            if not valid:
                raise ValueError(f"Ошибка в температуре: {msg}")
            old_temp = self.__temperature
            self.__temperature = float(temperature)
            changes.append(f"температура: {old_temp}°C → {self.__temperature}°C")

        if systolic is not None or diastolic is not None:
            new_systolic = systolic if systolic is not None else self.__systolic
            new_diastolic = diastolic if diastolic is not None else self.__diastolic

            valid, msg = validate.validate_pressure(new_systolic, new_diastolic)
            if not valid:
                raise ValueError(f"Ошибка в давлении: {msg}")

            if systolic is not None:
                old_systolic = self.__systolic
                self.__systolic = int(systolic)
                changes.append(
                    f"систолическое: {old_systolic} → {self.__systolic}"
                )

            if diastolic is not None:
                old_diastolic = self.__diastolic
                self.__diastolic = int(diastolic)
                changes.append(
                    f"диастолическое: {old_diastolic} → {self.__diastolic}"
                )

        if temperature is not None:
            if self.__temperature >= 39:
                self._update_status("критическое состояние")
            elif self.__temperature >= 38:
                self._update_status("на лечении")

        if changes:
            self._add_to_history(f"Обновлены показатели: {', '.join(changes)}")

    def _update_status(self, new_status: str) -> None:
        if new_status != self.__status:
            old_status = self.__status
            self.__status = new_status
            self._add_to_history(f"Статус изменен: {old_status} → {new_status}")

    def admit_to_hospital(self) -> None:
        if self.__status == "выписан":
            raise ValueError("Нельзя госпитализировать выписанного пациента")

        if self.__status == "умер":
            raise ValueError("Нельзя госпитализировать умершего пациента")

        self._update_status("на лечении")
        self._add_to_history("Пациент госпитализирован")

    def discharge(self) -> None:
        if self.__status == "выписан":
            raise ValueError("Пациент уже выписан")

        if self.__status == "умер":
            raise ValueError("Нельзя выписать умершего пациента")

        needs_hospital, msg = validate.validate_hospitalization(
            self.__age,
            self.__diagnosis
        )
        if needs_hospital:
            raise ValueError(f"Нельзя выписать: {msg}")

        self.__discharge_date = datetime.now()
        self._update_status("выписан")
        self._add_to_history(
            f"Пациент выписан. Дней в больнице: {self.days_in_hospital}"
        )

    def mark_as_deceased(self) -> None:
        if self.__status == "умер":
            raise ValueError("Пациент уже отмечен как умерший")

        self.__discharge_date = datetime.now()
        self._update_status("умер")
        self._add_to_history(
            f"Пациент умер. Дней в больнице: {self.days_in_hospital}"
        )

    def transfer_to_doctor(self, new_specialization: str) -> None:
        status_valid, status_msg = validate.validate_status_for_operation(
            self.__status,
            "перевести к другому врачу"
        )
        if not status_valid:
            raise ValueError(status_msg)

        valid, msg = validate.validate_doctor_specialization(new_specialization)
        if not valid:
            raise ValueError(f"Ошибка в специализации: {msg}")

        old_spec = self.__doctor_specialization
        self.__doctor_specialization = new_specialization.strip().lower()
        self._add_to_history(
            f"Переведен к врачу: {old_spec} → {self.__doctor_specialization}"
        )

    def add_treatment_note(self, note: str) -> None:
        status_valid, status_msg = validate.validate_status_for_operation(
            self.__status,
            "добавить заметку"
        )
        if not status_valid:
            raise ValueError(status_msg)

        if not isinstance(note, str) or not note.strip():
            raise ValueError("Заметка не может быть пустой")

        self._add_to_history(f"Заметка: {note.strip()}")

    @abstractmethod
    def calculate_cost(self) -> float:
        pass

    @abstractmethod
    def process(self) -> str:
        pass

    @abstractmethod
    def get_patient_type(self) -> str:
        pass

    def get_summary(self) -> str:
        return (
            f"{self.patient_id} | {self.name} | {self.age} | "
            f"{self.diagnosis} | {self.status}"
        )

    def __str__(self) -> str:
        status_emoji: dict = {
            "активен": "✅",
            "на лечении": "🏥",
            "критическое состояние": "🚨",
            "выписан": "📋",
            "умер": "⚰️"
        }.get(self.__status, "❓")

        pressure_status: str = "норма"
        if self.__systolic > 140 or self.__diastolic > 90:
            pressure_status = "повышенное"
        elif self.__systolic < 90 or self.__diastolic < 60:
            pressure_status = "пониженное"

        temp_status: str = "норма"
        if self.__temperature >= 38:
            temp_status = "лихорадка"
        elif self.__temperature <= 35:
            temp_status = "гипотермия"

        return f"""
╔════════════════════════════════════════════════════════════╗
║                     КАРТА ПАЦИЕНТА #{self.__patient_id}
╠════════════════════════════════════════════════════════════╣
║ Больница: {self.HOSPITAL_NAME}
║ {status_emoji} Статус: {self.__status.upper()}
║
║ Личные данные:
║   👤 Имя: {self.__name}
║   🎂 Возраст: {self.__age} лет
║   📅 Поступление: {self.__admission_date.strftime('%d.%m.%Y')}
║   ⏱️ Дней в больнице: {self.days_in_hospital}
║
║ Медицинские данные:
║   🏥 Диагноз: {self.__diagnosis}
║   👨‍⚕️ Врач: {self.__doctor_specialization.capitalize()}
║   🌡️ Температура: {self.__temperature:.1f}°C ({temp_status})
║   ❤️ Давление: {self.__systolic}/{self.__diastolic} ({pressure_status})
║
║ История лечения: {min(3, len(self.__treatment_history))} из {len(self.__treatment_history)} записей
╚════════════════════════════════════════════════════════════╝"""

    def __repr__(self) -> str:
        return (
            f"Patient(name='{self.__name}', age={self.__age}, "
            f"diagnosis='{self.__diagnosis}', "
            f"doctor='{self.__doctor_specialization}', "
            f"temp={self.__temperature:.1f}, "
            f"pressure={self.__systolic}/{self.__diastolic}, "
            f"status='{self.__status}')"
        )

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Patient):
            return False
        return self.__patient_id == other.__patient_id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Patient):
            return NotImplemented
        return self.__age < other.__age

    def __len__(self) -> int:
        return len(self.__treatment_history)