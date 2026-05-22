from typing import List, Optional, Any
from collection import PatientCollection
from models import InPatient, OutPatient, EmergencyPatient
from exceptions import NotFoundError, DuplicateError
import storage

class MedicalApp:
    def __init__(self, data_file: str = "medical_data.json") -> None:
        self.data_file: str = data_file
        self.collection: PatientCollection = PatientCollection()
        self._load_data()

    def _load_data(self) -> None:
        try:
            records = storage.load(self.data_file)
            for record in records:
                try:
                    self.collection.add(record)
                except ValueError:
                    pass
        except Exception:
            pass

    def _save_data(self) -> None:
        records = self.collection.get_all()
        storage.save(records, self.data_file)

    def add_in_patient(
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
    ) -> InPatient:
        patient = InPatient(
            name, age, diagnosis, doctor_specialization,
            room_number, daily_cost, temperature, systolic, diastolic
        )
        try:
            self.collection.add(patient)
            self._save_data()
            return patient
        except ValueError as e:
            raise DuplicateError(f"Patient already exists: {e}")

    def add_out_patient(
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
    ) -> OutPatient:
        patient = OutPatient(
            name, age, diagnosis, doctor_specialization,
            appointment_date, consultation_fee, temperature, systolic, diastolic
        )
        try:
            self.collection.add(patient)
            self._save_data()
            return patient
        except ValueError as e:
            raise DuplicateError(f"Patient already exists: {e}")

    def add_emergency_patient(
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
    ) -> EmergencyPatient:
        patient = EmergencyPatient(
            name, age, diagnosis, doctor_specialization,
            urgency_level, ambulance_arrival, temperature, systolic, diastolic
        )
        try:
            self.collection.add(patient)
            self._save_data()
            return patient
        except ValueError as e:
            raise DuplicateError(f"Patient already exists: {e}")

    def remove_patient(self, patient_id: str, confirm: bool = True) -> bool:
        if not confirm:
            return False
        patient = self.collection.find_by_id(patient_id)
        if patient is None:
            raise NotFoundError(f"Patient with ID {patient_id} not found")
        self.collection.remove(patient)
        self._save_data()
        return True

    def get_all_patients(self) -> List[Any]:
        return self.collection.get_all()

    def find_by_name(self, name: str) -> List[Any]:
        return self.collection.find_by_name(name)

    def find_by_diagnosis(self, diagnosis: str) -> List[Any]:
        return self.collection.find_by_diagnosis(diagnosis)

    def find_by_id(self, patient_id: str) -> Optional[Any]:
        patient = self.collection.find_by_id(patient_id)
        if patient is None:
            raise NotFoundError(f"Patient with ID {patient_id} not found")
        return patient

    def sort_by_name(self) -> List[Any]:
        self.collection.sort_by_name()
        return self.collection.get_all()

    def sort_by_age(self) -> List[Any]:
        self.collection.sort_by_age()
        return self.collection.get_all()

    def sort_by_date(self) -> List[Any]:
        self.collection.sort_by_date()
        return self.collection.get_all()

    def get_count(self) -> int:
        return len(self.collection)

    def clear_all(self) -> None:
        for patient in self.collection.get_all():
            try:
                self.collection.remove(patient)
            except ValueError:
                pass
        self._save_data()