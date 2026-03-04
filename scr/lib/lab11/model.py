class Student:
    university = "Python University"
    total_students = 0
    
    def __init__(self, name: str, age: int, gpa: float, student_id: str):
        self.__name = ""
        self.__age = 0
        self.__gpa = 0.0
        self.__student_id = ""
        self.__is_active = True

        self.name = name
        self.age = age
        self.gpa = gpa
        self.student_id = student_id
        
        Student.total_students += 1

    def _validate_name(self, name: str) -> bool:
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name.strip()) == 0:
            raise ValueError("Name cannot be empty")
        if len(name) < 2:
            raise ValueError("Name must be at least 2 characters")
        return True
    
    def _validate_age(self, age: int) -> bool:
        if not isinstance(age, int):
            raise TypeError("Age must be an integer")
        if age < 16 or age > 100:
            raise ValueError("Age must be between 16 and 100")
        return True
    
    def _validate_gpa(self, gpa: float) -> bool:
        if not isinstance(gpa, (int, float)):
            raise TypeError("GPA must be a number")
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        return True
    
    def _validate_student_id(self, student_id: str) -> bool:
        if not isinstance(student_id, str):
            raise TypeError("Student ID must be a string")
        if not student_id.startswith("STU-"):
            raise ValueError("Student ID must start with 'STU-'")
        if len(student_id) != 8:
            raise ValueError("Student ID must be in format STU-XXXX")
        return True

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if self._validate_name(value):
            self.__name = value.strip()
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if self._validate_age(value):
            self.__age = value
    
    @property
    def gpa(self):
        return self.__gpa
    
    @gpa.setter
    def gpa(self, value):
        if self._validate_gpa(value):
            self.__gpa = float(value)
    
    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, value):
        if self._validate_student_id(value):
            self.__student_id = value
    
    @property
    def is_active(self):
        return self.__is_active
 

    def update_gpa(self, new_gpa: float) -> bool:
        try:
            self.gpa = new_gpa
            return True
        except (TypeError, ValueError):
            return False
    
    def promote(self) -> str:
        if not self.__is_active:
            return f"{self.__name} is inactive - cannot promote"
        
        if self.__gpa >= 2.0:
            return f"{self.__name} can be promoted (GPA: {self.__gpa:.2f})"
        else:
            return f"{self.__name} cannot be promoted - GPA too low ({self.__gpa:.2f})"
    
    def activate(self):
        self.__is_active = True
        print(f"{self.__name} is now ACTIVE")
    
    def deactivate(self):
        self.__is_active = False
        print(f"{self.__name} is now INACTIVE")

    def __str__(self):
        status = "Active" if self.__is_active else "Inactive"
        return f"👨‍🎓 {self.__name} | ID: {self.__student_id} | Age: {self.__age} | GPA: {self.__gpa:.2f} | {status}"
    
    def __repr__(self):
        return f"Student(name='{self.__name}', age={self.__age}, gpa={self.__gpa}, student_id='{self.__student_id}')"
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return (self.__student_id == other.__student_id and 
                self.__name == other.__name)