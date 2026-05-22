def validate_name(name):
    if not isinstance(name, str):
        return False, "Имя должно быть строкой"
    
    name = name.strip()
    if not name:
        return False, "Имя не может быть пустым"
    
    if len(name) < 2:
        return False, "Имя должно содержать минимум 2 символа"
    
    if len(name) > 100:
        return False, "Имя слишком длинное (макс. 100 символов)"

    for c in name:
        if not (c.isalpha() or c.isspace() or c == '-' or c == '.'):
            return False, "Имя может содержать только буквы, пробелы, дефисы и точки"
    
    return True, "OK"


def validate_age(age):
    if not isinstance(age, (int, float)):
        return False, "Возраст должен быть числом"
    
    if age < 0:
        return False, "Возраст не может быть отрицательным"
    
    if age > 150:
        return False, "Возраст не может превышать 150 лет"
    
    if isinstance(age, float) and age != int(age):
        return False, "Возраст должен быть целым числом"
    
    return True, "OK"


def validate_diagnosis(diagnosis):
    if not isinstance(diagnosis, str):
        return False, "Диагноз должен быть строкой"
    
    diagnosis = diagnosis.strip()
    if not diagnosis:
        return False, "Диагноз не может быть пустым"
    
    if len(diagnosis) < 3:
        return False, "Диагноз должен содержать минимум 3 символа"
    
    if len(diagnosis) > 500:
        return False, "Диагноз слишком длинный (макс. 500 символов)"
    
    return True, "OK"


def validate_doctor_specialization(specialization):
    if not isinstance(specialization, str):
        return False, "Специализация должна быть строкой"
    
    specialization = specialization.strip()
    if not specialization:
        return False, "Специализация не может быть пустой"
    
    valid_specializations = [
        "терапевт", "хирург", "кардиолог", "невролог", "педиатр",
        "офтальмолог", "дерматолог", "гинеколог", "уролог", "онколог",
        "психиатр", "стоматолог", "отоларинголог", "эндокринолог"
    ]
    
    if specialization.lower() not in valid_specializations:
        return False, f"Недопустимая специализация. Допустимые: {', '.join(valid_specializations)}"
    
    return True, "OK"


def validate_temperature(temperature):
    if not isinstance(temperature, (int, float)):
        return False, "Температура должна быть числом"
    
    if temperature < 30:
        return False, "Температура ниже критической (< 30°C)"
    
    if temperature > 45:
        return False, "Температура выше критической (> 45°C)"
    
    return True, "OK"


def validate_pressure(systolic, diastolic):
    if not isinstance(systolic, (int, float)) or not isinstance(diastolic, (int, float)):
        return False, "Давление должно быть числом"
    
    if systolic < 30 or systolic > 300:
        return False, "Систолическое давление вне допустимого диапазона (30-300)"
    
    if diastolic < 20 or diastolic > 200:
        return False, "Диастолическое давление вне допустимого диапазона (20-200)"
    
    if systolic <= diastolic:
        return False, "Систолическое давление должно быть больше диастолического"
    
    return True, "OK"


def validate_status_for_operation(status, operation):
    if status == "выписан":
        return False, f"Нельзя {operation}: пациент выписан"
    
    if status == "умер":
        return False, f"Нельзя {operation}: пациент умер"
    
    return True, "OK"


def validate_hospitalization(age, diagnosis):
    critical_diagnoses = ["инфаркт", "инсульт", "онкология", "пневмония"]
    
    if age > 80 and any(critical in diagnosis.lower() for critical in critical_diagnoses):
        return True, "Требуется срочная госпитализация"
    
    if age < 1 and "температура" in diagnosis.lower():
        return True, "Требуется госпитализация (грудной ребенок с температурой)"
    
    return False, "Госпитализация не требуется"