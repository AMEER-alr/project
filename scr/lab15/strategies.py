def by_patient_age(patient):
    return patient.age


def by_patient_name(patient):
    return patient.name.lower()


def by_patient_id(patient):
    return patient.patient_id


def by_patient_status(patient):
    status_priority = {
        "критическое состояние": 0,
        "на лечении": 1,
        "активен": 2,
        "выписан": 3,
        "умер": 4
    }
    return status_priority.get(patient.status, 5)


def by_temperature(patient):
    return patient.temperature


def by_admission_date(patient):
    return patient.admission_date


def by_days_in_hospital(patient):
    days = patient.days_in_hospital
    if isinstance(days, str):
        return -1
    return days


def by_multiple_attrs(patient):
    status_priority = {
        "критическое состояние": 0,
        "на лечении": 1,
        "активен": 2,
        "выписан": 3,
        "умер": 4
    }
    return (status_priority.get(patient.status, 5), -patient.age)


def is_adult(patient):
    return patient.age >= 18


def is_child(patient):
    return patient.age < 18


def is_critical(patient):
    return patient.status == "критическое состояние"


def is_on_treatment(patient):
    return patient.status == "на лечении"


def is_active(patient):
    return patient.status in ["активен", "на лечении", "критическое состояние"]


def has_fever(patient):
    return patient.temperature >= 38.0


def has_high_pressure(patient):
    return patient.systolic > 140 or patient.diastolic > 90


def by_patient_type_filter(patient_type):
    def filter_fn(patient):
        return patient.get_patient_type() == patient_type
    return filter_fn


def by_diagnosis_filter(diagnosis_substring):
    def filter_fn(patient):
        return diagnosis_substring.lower() in patient.diagnosis.lower()
    return filter_fn


def by_age_range_filter(min_age, max_age):
    def filter_fn(patient):
        return min_age <= patient.age <= max_age
    return filter_fn


def by_doctor_specialization_filter(specialization):
    def filter_fn(patient):
        return patient.doctor_specialization == specialization.lower()
    return filter_fn


def patient_to_short_string(patient):
    status_icon = {
        "активен": "✅",
        "на лечении": "🏥",
        "критическое состояние": "🚨",
        "выписан": "📋",
        "умер": "⚰️"
    }.get(patient.status, "❓")
    return f"{status_icon} {patient.patient_id} | {patient.name} | {patient.age} лет | {patient.diagnosis[:20]}"


def patient_to_string(patient):
    return (f"{patient.patient_id} | {patient.name} | {patient.age} лет | "
            f"{patient.diagnosis} | {patient.doctor_specialization} | "
            f"Т:{patient.temperature:.1f}°C | {patient.status}")


def extract_patient_name(patient):
    return patient.name


def extract_patient_age(patient):
    return patient.age


def extract_patient_id(patient):
    return patient.patient_id


def patient_to_dict(patient):
    return {
        "id": patient.patient_id,
        "name": patient.name,
        "age": patient.age,
        "diagnosis": patient.diagnosis,
        "status": patient.status,
        "doctor": patient.doctor_specialization,
        "temperature": patient.temperature,
        "pressure": f"{patient.systolic}/{patient.diastolic}",
        "type": patient.get_patient_type()
    }


def apply_discount_to_cost(discount_percent=10):
    def apply(patient):
        original_cost = patient.calculate_cost()
        discounted_cost = original_cost * (1 - discount_percent / 100)
        patient._discounted_cost = discounted_cost
        return patient
    return apply


def add_veteran_discount(patient):
    if patient.age >= 70:
        original_cost = patient.calculate_cost()
        patient._veteran_discount = original_cost * 0.7
    return patient


class PriorityStrategy:
    def __call__(self, patient):
        if patient.status == "критическое состояние":
            return 1
        elif patient.status == "на лечении" and patient.temperature >= 39:
            return 2
        elif patient.status == "на лечении":
            return 3
        elif patient.age >= 75:
            return 4
        elif patient.age >= 60:
            return 5
        else:
            return 6


class TreatmentPlanStrategy:
    def __call__(self, patient):
        patient_type = patient.get_patient_type()
        
        if patient_type == "InPatient":
            return (f"🏥 {patient.name} (ID: {patient.patient_id}): "
                    f"СТАЦИОНАРНОЕ ЛЕЧЕНИЕ\n"
                    f"   → Палата №{patient.room_number}\n"
                    f"   → Стоимость дня: {patient.daily_cost:.2f} руб.\n"
                    f"   → План: ежедневный осмотр, приём лекарств")
        
        elif patient_type == "OutPatient":
            return (f"📅 {patient.name} (ID: {patient.patient_id}): "
                    f"АМБУЛАТОРНОЕ ЛЕЧЕНИЕ\n"
                    f"   → Дата приёма: {patient.appointment_date}\n"
                    f"   → Стоимость: {patient.consultation_fee:.2f} руб.\n"
                    f"   → План: консультация, выписка рецептов")
        
        elif patient_type == "EmergencyPatient":
            urgency_text = "КРИТИЧЕСКИЙ" if patient.urgency_level <= 2 else "Стандартный"
            return (f"🚑 {patient.name} (ID: {patient.patient_id}): "
                    f"ЭКСТРЕННАЯ ГОСПИТАЛИЗАЦИЯ ({urgency_text})\n"
                    f"   → Уровень срочности: {patient.urgency_level}\n"
                    f"   → Скорая помощь: {'Да' if patient.ambulance_arrival else 'Нет'}\n"
                    f"   → План: немедленная диагностика, интенсивная терапия")
        
        return f"❓ {patient.name}: Обычное наблюдение"


class StatusUpdateStrategy:
    def __call__(self, patient):
        if patient.temperature >= 39:
            if patient.status != "критическое состояние":
                patient._update_status("критическое состояние")
        elif patient.temperature >= 38:
            if patient.status == "активен":
                patient._update_status("на лечении")
        elif patient.temperature < 37 and patient.status == "критическое состояние":
            if patient.age < 70:
                patient._update_status("на лечении")
        
        return patient


class DischargeCheckStrategy:
    def __call__(self, patient):
        from validate import validate_hospitalization
        
        if patient.status == "выписан":
            return f"⚠️ {patient.name} УЖЕ ВЫПИСАН"
        
        if patient.status == "умер":
            return f"⚰️ {patient.name} (пациент умер)"
        
        needs_hospital, msg = validate_hospitalization(patient.age, patient.diagnosis)
        
        if not needs_hospital:
            patient._can_be_discharged = True
            return f"✅ {patient.name} МОЖЕТ БЫТЬ ВЫПИСАН: {msg}"
        else:
            patient._can_be_discharged = False
            return f"❌ {patient.name} НЕ МОЖЕТ БЫТЬ ВЫПИСАН: {msg}"


def print_patients(collection, title="Пациенты"):
    print(f"\n{'='*60}")
    print(f"📋 {title}")
    print(f"{'='*60}")
    
    if len(collection) == 0:
        print("  (пусто)")
        return
    
    for i, patient in enumerate(collection.get_all(), 1):
        print(f"{i:2}. {patient_to_short_string(patient)}")