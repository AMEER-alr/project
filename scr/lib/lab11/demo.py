from model import Student

def demonstrate_level_3():
    print("=" * 60)
    print("LEVEL 3 DEMONSTRATION")
    print("=" * 60)
    
    try:
        student1 = Student("Ahmed", 20, 3.5, "STU-1234")
        print("✅ Student created successfully")

        print("\n📌 Student info:")
        print(student1)

        student2 = Student("Ahmed", 20, 3.5, "STU-1234")
        student3 = Student("Sara", 22, 3.8, "STU-5678")
        
        print(f"\n📌 student1 == student2: {student1 == student2}")
        print(f"📌 student1 == student3: {student1 == student3}")

        print(f"\n📌 Promotion status: {student1.promote()}")

        print("\n📌 Testing invalid data:")
        try:
            invalid_student = Student("", -5, 5.5, "1234")
        except (TypeError, ValueError) as e:
            print(f"❌ Error caught: {e}")
            
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def demonstrate_level_4():
    print("\n" + "=" * 60)
    print("LEVEL 4 DEMONSTRATION")
    print("=" * 60)
    
    student = Student("Mohammed", 21, 3.2, "STU-4321")

    print("\n📌 __repr__ output:")
    print(repr(student))

    print("\n📌 Testing setter with validation:")
    try:
        student.gpa = 3.9
        print(f"✅ GPA updated successfully: {student.gpa}")
        
        student.gpa = 5.0
    except ValueError as e:
        print(f"❌ GPA update failed: {e}")

    print(f"\n📌 Class attribute (via class): {Student.university}")
    print(f"📌 Class attribute (via instance): {student.university}")
    print(f"📌 Total students created: {Student.total_students}")

    print("\n📌 GPA update method:")
    if student.update_gpa(3.7):
        print(f"✅ New GPA: {student.gpa}")

    print(f"\n📌 Student GPA: {student.gpa:.2f}")

def demonstrate_level_5():
    print("\n" + "=" * 60)
    print("LEVEL 5 DEMONSTRATION")
    print("=" * 60)
    
    student = Student("Fatima", 19, 3.4, "STU-9876")

    print("\n📌 SCENARIO 1: Active student with good GPA")
    print(student)
    print(f"Promotion: {student.promote()}")
    
    print("\n📌 SCENARIO 2: State change (deactivate)")
    student.deactivate()
    print(student)
    print(f"Promotion: {student.promote()}")
    
    print("\n📌 SCENARIO 3: Reactivate and update GPA")
    student.activate()
    student.update_gpa(1.5)
    print(student)
    print(f"Promotion: {student.promote()}")

    print("\n📌 Testing validation methods:")
    test_cases = [
        ("", 20, 3.0, "STU-1111"),
        ("Ali", 15, 3.0, "STU-2222"),
        ("Omar", 25, 4.5, "STU-3333"),
        ("Huda", 22, 3.2, "1234567"),
    ]
    
    for i, (name, age, gpa, sid) in enumerate(test_cases, 1):
        print(f"\nTest {i}: name='{name}', age={age}, gpa={gpa}, id='{sid}'")
        try:
            s = Student(name, age, gpa, sid)
            print(f"✅ Success: {s}")
        except (TypeError, ValueError) as e:
            print(f"❌ Failed: {e}")

def main():
    print("STUDENT CLASS DEMONSTRATION")
    print("Developed for Lab 1 - Encapsulation")
    
    demonstrate_level_3()
    demonstrate_level_4()
    demonstrate_level_5()
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)

if __name__ == "__main__":
    main()