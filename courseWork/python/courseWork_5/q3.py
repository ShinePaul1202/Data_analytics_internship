from abc import ABC, abstractmethod


# =========================================================
# Task 1: Person Abstract Class
# =========================================================

class Person(ABC):

    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

        super().__init__()

    def __str__(self):
        return (
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Gender: {self.gender}, "
            f"Address: {self.address}"
        )

    def greet(self, other_person):
        return f"Hello {other_person.name}! My name is {self.name}."

    @abstractmethod
    def introduce(self):
        pass

    @staticmethod
    def is_adult(age):
        return age >= 18


# =========================================================
# Task 2: Employee Class
# =========================================================

class Employee(Person):

    counter=0

    def __init__(self, name, age, gender, address, salary):
        super().__init__(name, age, gender, address)

        self._salary = salary

        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter:02d}"

    def __del__(self):
        if Employee.counter > 0:
            Employee.counter -= 1

    @property
    def employee_count(self):
        return Employee.counter

    @property
    def employee_id(self):
        return self.__employee_id

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary

    def increase_salary(self, amount):
        self._salary += amount

    def decrease_salary(self, amount):
        self._salary -= amount

    def introduce(self):
        return f"Hello, my name is {self.name} and I work as an employee."


# =========================================================
# Task 3: Teacher Class
# =========================================================

class Teacher(Employee):

    # Class attribute
    counter = 0

    def __init__(self, name, age, gender, address, salary, subjects):
        # Call parent constructor
        super().__init__(name, age, gender, address, salary)

        # Store subjects as a list
        self.subjects = list(subjects)

        # Generate teacher ID
        Teacher.counter += 1
        self.__teacher_id = f"TEC{Teacher.counter:02d}"

    def __del__(self):
        # Decrease Teacher counter
        if Teacher.counter > 0:
            Teacher.counter -= 1

        # Call parent destructor
        super().__del__()

    @property
    def teacher_count(self):
        return Teacher.counter

    @property
    def teacher_id(self):
        return self.__teacher_id

    def add_subject(self, subject):
        self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def introduce(self):
        subject_list = ", ".join(self.subjects)
        return f"My ID is {self.teacher_id} and I teach: {subject_list}"

    @property
    def employee_id(self):
        raise AttributeError(
            f"{self.__class__.__name__} object has no attribute 'employee_id'"
        )


# =========================================================
# Main Block
# =========================================================

if __name__ == "__main__":

    teacher1=Teacher(
        "John",
        35,
        "Male",
        "Kochi",
        50000,
        ["Mathematics", "Physics"]
    )

    teacher2=Teacher(
        "Anu",
        30,
        "Female",
        "Thrissur",
        45000,
        ["Chemistry", "Biology"]
    )

    print("Teacher 1:")
    print(teacher1)

    print("\nTeacher 2:")
    print(teacher2)

    print("\nTeacher IDs:")
    print("Teacher 1 ID:", teacher1.teacher_id)
    print("Teacher 2 ID:", teacher2.teacher_id)

    print("\nTeacher Count:")
    print(teacher1.teacher_count)

    print("\nSubjects:")
    print("Teacher 1:", teacher1.subjects)
    print("Teacher 2:", teacher2.subjects)

    teacher1.add_subject("Computer Science")
    print("\nAfter adding Computer Science:")
    print(teacher1.subjects)

    teacher1.remove_subject("Physics")
    print("\nAfter removing Physics:")
    print(teacher1.subjects)

    print("\nIntroduction:")
    print(teacher1.introduce())
    print(teacher2.introduce())

    print("\nEmployee ID Access:")

    try:
        print(teacher1.employee_id)
    except AttributeError as error:
        print(error)
