def format_record(rec):
    if not isinstance(rec, tuple):
        raise TypeError("Input must be a tuple")
    
    if len(rec) != 3:
        raise ValueError("Tuple must have exactly 3 elements")
    
    ФИО, group, gpa = rec
    
    if not isinstance(ФИО, str):
        raise TypeError("ФИО must be a string")
    if not isinstance(group, str):
        raise TypeError("Group must be a string")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA must be a number")
    
    ФИО = ФИО.strip()
    if not ФИО:
        raise ValueError("ФИО cannot be empty")
    
    group = group.strip()
    if not group:
        raise ValueError("Group cannot be empty")
    
    if gpa < 0:
        raise ValueError("GPA cannot be negative")
    
    names = [name.strip() for name in ФИО.split() if name.strip()]
    
    if len(names) < 2:
        raise ValueError("ФИО must contain at least last name and first name")
    
    last_name = names[0]
    first_names = names[1:]
    
    initials = '.'.join(name[0].upper() for name in first_names) + '.'
    
    formatted_gpa = f"{gpa:.2f}"
    
    result = f"{last_name} {initials}, гр. {group}, GPA {formatted_gpa}"
    
    return result


print("=== format_record ===")
    
print(format_record(("Иванов Иван Иванович", "БИВТ-25", 4.6)))
    
print(format_record(("Петров Пётр", "IKB0-12", 5.0)))
    
print(format_record(("Петров Пётр Петрович", "IKB0-12", 5.0)))
    
print(format_record(("Сидорова анна аергеевна", "АВВ-01", 3.999)))
    
try:
    print(format_record(("", "БИВТ-25", 4.5)))
except ValueError as e:
    print("Error:", e)
    
try:
    print(format_record(("Иванов", "БИВТ-25", 4.5)))
except ValueError as e:
    print("Error:", e)
    
try:
    print(format_record(("Иванов Иван", "", 4.5)))
except ValueError as e:
    print("Error:", e)
    
try:
    print(format_record(("Иванов Иван", "БИВТ-25", -1.0)))
except ValueError as e:
    print("Error:", e)
