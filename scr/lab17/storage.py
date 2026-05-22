import json
import os
from typing import List, Any
from models import InPatient, OutPatient, EmergencyPatient
from exceptions import StorageError


PATIENT_TYPE_MAP = {
    "InPatient": InPatient,
    "OutPatient": OutPatient,
    "EmergencyPatient": EmergencyPatient,
}

def patient_to_dict(patient: Any) -> dict:
    data = {
        "patient_id": patient.patient_id,
        "type": patient.get_patient_type(),
        "name": patient.name,
        "age": patient.age,
        "diagnosis": patient.diagnosis,
        "doctor_specialization": patient.doctor_specialization,
        "temperature": patient.temperature,
        "systolic": patient.systolic,
        "diastolic": patient.diastolic,
        "status": patient.status,
        "admission_date": patient.admission_date.isoformat(),
        "treatment_history": patient.treatment_history,
    }
    if patient.get_patient_type() == "InPatient":
        data["room_number"] = patient.room_number
        data["daily_cost"] = patient.daily_cost
    elif patient.get_patient_type() == "OutPatient":
        data["appointment_date"] = patient.appointment_date
        data["consultation_fee"] = patient.consultation_fee
    elif patient.get_patient_type() == "EmergencyPatient":
        data["urgency_level"] = patient.urgency_level
        data["ambulance_arrival"] = patient.ambulance_arrival
    return data

def patient_from_dict(data: dict) -> Any:
    patient_type = data["type"]
    saved_id = data.get("patient_id")
    
    if patient_type not in PATIENT_TYPE_MAP:
        raise ValueError(f"Unknown patient type: {patient_type}")
    
    cls = PATIENT_TYPE_MAP[patient_type]
    
    if patient_type == "InPatient":
        patient = cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"],
            doctor_specialization=data["doctor_specialization"],
            room_number=data["room_number"],
            daily_cost=data["daily_cost"],
            temperature=data["temperature"],
            systolic=data["systolic"],
            diastolic=data["diastolic"],
            patient_id=saved_id
        )
    elif patient_type == "OutPatient":
        patient = cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"],
            doctor_specialization=data["doctor_specialization"],
            appointment_date=data["appointment_date"],
            consultation_fee=data["consultation_fee"],
            temperature=data["temperature"],
            systolic=data["systolic"],
            diastolic=data["diastolic"],
            patient_id=saved_id
        )
    elif patient_type == "EmergencyPatient":
        patient = cls(
            name=data["name"],
            age=data["age"],
            diagnosis=data["diagnosis"],
            doctor_specialization=data["doctor_specialization"],
            urgency_level=data["urgency_level"],
            ambulance_arrival=data["ambulance_arrival"],
            temperature=data["temperature"],
            systolic=data["systolic"],
            diastolic=data["diastolic"],
            patient_id=saved_id
        )
    else:
        raise ValueError(f"Cannot deserialize patient type: {patient_type}")
    
    return patient

def save(collection: List[Any], filepath: str) -> None:
    try:
        data = [patient_to_dict(p) for p in collection]
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise StorageError(f"Failed to save data: {e}")

def load(filepath: str) -> List[Any]:
    if not os.path.exists(filepath):
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        patients = [patient_from_dict(item) for item in data]
        
        from base import Patient
        max_id = 1000
        for p in patients:
            id_num = int(p.patient_id[3:])
            if id_num >= max_id:
                max_id = id_num + 1
        
        Patient.set_next_id(max_id)
        
        return patients
    except Exception as e:
        raise StorageError(f"Failed to load data: {e}")