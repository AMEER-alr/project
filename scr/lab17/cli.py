from typing import List, Any
from app import MedicalApp
from exceptions import ValidationError, NotFoundError, DuplicateError

class ConsoleCLI:
    def __init__(self, app: MedicalApp) -> None:
        self.app: MedicalApp = app

    def _display_menu(self) -> None:
        print("\n" + "=" * 60)
        print("        MEDICAL PATIENT MANAGEMENT SYSTEM")
        print("=" * 60)
        print("1. Add InPatient (стационарный)")
        print("2. Add OutPatient (амбулаторный)")
        print("3. Add EmergencyPatient (экстренный)")
        print("4. Show all patients")
        print("5. Find by name")
        print("6. Find by diagnosis")
        print("7. Find by ID")
        print("8. Remove patient")
        print("9. Sort patients")
        print("10. Show patient count")
        print("0. Exit")
        print("=" * 60)

    def _get_int_input(self, prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Error: Please enter a valid number")

    def _get_positive_int(self, prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value > 0:
                    return value
                print("Error: Value must be positive")
            except ValueError:
                print("Error: Please enter a valid number")

    def _get_float_input(self, prompt: str) -> float:
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Please enter a valid number")

    def _get_bool_input(self, prompt: str) -> bool:
        while True:
            value = input(prompt).strip().lower()
            if value in ['y', 'yes', 'true', '1', 'да']:
                return True
            if value in ['n', 'no', 'false', '0', 'нет']:
                return False
            print("Please enter y/n")

    def _add_in_patient(self) -> None:
        print("\n--- ADD INPATIENT ---")
        try:
            name = input("Patient name: ").strip()
            if not name:
                raise ValidationError("Name cannot be empty")
            age = self._get_positive_int("Age: ")
            diagnosis = input("Diagnosis: ").strip()
            if not diagnosis:
                raise ValidationError("Diagnosis cannot be empty")
            doctor = input("Doctor specialization: ").strip()
            if not doctor:
                raise ValidationError("Doctor specialization cannot be empty")
            room = self._get_positive_int("Room number: ")
            cost = self._get_float_input("Daily cost: ")
            temp = self._get_float_input("Temperature (default 36.6): ") or 36.6
            patient = self.app.add_in_patient(
                name, age, diagnosis, doctor, room, cost, temp
            )
            print(f"\nPatient added successfully with ID: {patient.patient_id}")
        except ValidationError as e:
            print(f"Validation error: {e}")
        except DuplicateError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _add_out_patient(self) -> None:
        print("\n--- ADD OUTPATIENT ---")
        try:
            name = input("Patient name: ").strip()
            if not name:
                raise ValidationError("Name cannot be empty")
            age = self._get_positive_int("Age: ")
            diagnosis = input("Diagnosis: ").strip()
            if not diagnosis:
                raise ValidationError("Diagnosis cannot be empty")
            doctor = input("Doctor specialization: ").strip()
            if not doctor:
                raise ValidationError("Doctor specialization cannot be empty")
            date = input("Appointment date (YYYY-MM-DD): ").strip()
            fee = self._get_float_input("Consultation fee: ")
            temp = self._get_float_input("Temperature (default 36.6): ") or 36.6
            patient = self.app.add_out_patient(
                name, age, diagnosis, doctor, date, fee, temp
            )
            print(f"\nPatient added successfully with ID: {patient.patient_id}")
        except ValidationError as e:
            print(f"Validation error: {e}")
        except DuplicateError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _add_emergency_patient(self) -> None:
        print("\n--- ADD EMERGENCY PATIENT ---")
        try:
            name = input("Patient name: ").strip()
            if not name:
                raise ValidationError("Name cannot be empty")
            age = self._get_positive_int("Age: ")
            diagnosis = input("Diagnosis: ").strip()
            if not diagnosis:
                raise ValidationError("Diagnosis cannot be empty")
            doctor = input("Doctor specialization: ").strip()
            if not doctor:
                raise ValidationError("Doctor specialization cannot be empty")
            urgency = self._get_positive_int("Urgency level (1-5, 1=most urgent): ")
            if urgency < 1 or urgency > 5:
                raise ValidationError("Urgency level must be between 1 and 5")
            ambulance = self._get_bool_input("Ambulance arrival? (y/n): ")
            temp = self._get_float_input("Temperature (default 36.6): ") or 36.6
            patient = self.app.add_emergency_patient(
                name, age, diagnosis, doctor, urgency, ambulance, temp
            )
            print(f"\nPatient added successfully with ID: {patient.patient_id}")
        except ValidationError as e:
            print(f"Validation error: {e}")
        except DuplicateError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _show_all_patients(self) -> None:
        print("\n--- ALL PATIENTS ---")
        patients = self.app.get_all_patients()
        if not patients:
            print("No patients found")
            return
        print("\n" + "-" * 80)
        for patient in patients:
            print(patient.get_summary())
        print("-" * 80)

    def _find_by_name(self) -> None:
        print("\n--- FIND BY NAME ---")
        name = input("Enter patient name: ").strip()
        if not name:
            print("Name cannot be empty")
            return
        patients = self.app.find_by_name(name)
        self._display_search_results(patients)

    def _find_by_diagnosis(self) -> None:
        print("\n--- FIND BY DIAGNOSIS ---")
        diagnosis = input("Enter diagnosis: ").strip()
        if not diagnosis:
            print("Diagnosis cannot be empty")
            return
        patients = self.app.find_by_diagnosis(diagnosis)
        self._display_search_results(patients)

    def _find_by_id(self) -> None:
        print("\n--- FIND BY ID ---")
        patient_id = input("Enter patient ID (e.g., PAT1000): ").strip()
        if not patient_id:
            print("ID cannot be empty")
            return
        try:
            patient = self.app.find_by_id(patient_id)
            print("\n" + "-" * 80)
            print(patient)
            print("-" * 80)
        except NotFoundError as e:
            print(f"Error: {e}")

    def _display_search_results(self, patients: List[Any]) -> None:
        if not patients:
            print("No patients found")
            return
        print(f"\nFound {len(patients)} patient(s):")
        print("-" * 80)
        for patient in patients:
            print(patient.get_summary())
        print("-" * 80)

    def _remove_patient(self) -> None:
        print("\n--- REMOVE PATIENT ---")
        patient_id = input("Enter patient ID to remove: ").strip()
        if not patient_id:
            print("ID cannot be empty")
            return
        try:
            patient = self.app.find_by_id(patient_id)
            print(f"\nPatient to remove:")
            print(patient.get_summary())
            confirm = input("\nDelete this patient? (y/n): ").strip().lower()
            if confirm == 'y':
                self.app.remove_patient(patient_id, confirm=True)
                print("Patient removed successfully")
            else:
                print("Operation cancelled")
        except NotFoundError as e:
            print(f"Error: {e}")

    def _sort_patients(self) -> None:
        print("\n--- SORT PATIENTS ---")
        print("1. Sort by name")
        print("2. Sort by age")
        print("3. Sort by admission date")
        choice = self._get_int_input("Choose sorting option: ")
        try:
            if choice == 1:
                result = self.app.sort_by_name()
                print("\nSorted by name:")
            elif choice == 2:
                result = self.app.sort_by_age()
                print("\nSorted by age:")
            elif choice == 3:
                result = self.app.sort_by_date()
                print("\nSorted by admission date:")
            else:
                print("Invalid choice")
                return
            if not result:
                print("No patients to sort")
                return
            print("-" * 80)
            for patient in result:
                print(patient.get_summary())
            print("-" * 80)
        except Exception as e:
            print(f"Error during sorting: {e}")

    def _show_count(self) -> None:
        count = self.app.get_count()
        print(f"\nTotal patients: {count}")

    def run(self) -> int:
        while True:
            self._display_menu()
            choice = self._get_int_input("Your choice: ")
            if choice == 1:
                self._add_in_patient()
            elif choice == 2:
                self._add_out_patient()
            elif choice == 3:
                self._add_emergency_patient()
            elif choice == 4:
                self._show_all_patients()
            elif choice == 5:
                self._find_by_name()
            elif choice == 6:
                self._find_by_diagnosis()
            elif choice == 7:
                self._find_by_id()
            elif choice == 8:
                self._remove_patient()
            elif choice == 9:
                self._sort_patients()
            elif choice == 10:
                self._show_count()
            elif choice == 0:
                print("\nSaving data... Goodbye!")
                return 0
            else:
                print("Invalid choice. Please enter 0-10")