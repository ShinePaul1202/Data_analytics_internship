from abc import ABC, abstractmethod


# ---------------------------------------------------------
# Task 1: Person Abstract Class
# ---------------------------------------------------------

class Person(ABC):

    def __init__(self, name, age, gender, address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

        # Cooperative inheritance
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


# ---------------------------------------------------------
# Task 2: Employee Class
# ---------------------------------------------------------

class Employee(Person):

    # Class attribute
    counter = 0

    def __init__(self, name, age, gender, address, salary):
        # Call the parent constructor
        super().__init__(name, age, gender, address)

        # Initialize protected salary attribute
        self._salary = salary

        # Generate employee ID using the counter
        Employee.counter += 1
        self.__employee_id = f"EMP{Employee.counter:02d}"

    def __del__(self):
        # Decrease counter when Employee object is deleted
        if Employee.counter > 0:
            Employee.counter -= 1

    @property
    def employee_count(self):
        # Return the current number of Employee objects
        return Employee.counter

    @property
    def employee_id(self):
        # Getter for private employee ID
        return self.__employee_id

    @property
    def salary(self):
        # Getter for salary
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        # Setter for salary
        self._salary = new_salary

    def increase_salary(self, amount):
        # Increase salary
        self._salary += amount

    def decrease_salary(self, amount):
        # Decrease salary
        self._salary -= amount

    def introduce(self):
        # Implementation of the abstract method
        return f"Hello, my name is {self.name} and I work as an employee."


# ---------------------------------------------------------
# Main Block
# ---------------------------------------------------------

if __name__ == "__main__":

    # Create Employee objects
    employee1 = Employee(
        "John",
        25,
        "Male",
        "Kochi",
        30000
    )

    employee2 = Employee(
        "Anu",
        28,
        "Female",
        "Thrissur",
        40000
    )

    # Display employee information
    print("Employee 1:")
    print(employee1)

    print("\nEmployee 2:")
    print(employee2)

    # Display employee IDs
    print("\nEmployee IDs:")
    print("Employee 1 ID:", employee1.employee_id)
    print("Employee 2 ID:", employee2.employee_id)

    # Display employee count
    print("\nEmployee Count:")
    print(employee1.employee_count)

    # Salary getter
    print("\nOriginal Salary:")
    print(employee1.salary)

    # Increase salary
    employee1.increase_salary(5000)
    print("\nSalary after increase:")
    print(employee1.salary)

    # Decrease salary
    employee1.decrease_salary(2000)
    print("\nSalary after decrease:")
    print(employee1.salary)

    # Salary setter
    employee1.salary = 35000
    print("\nSalary after using setter:")
    print(employee1.salary)

    # Introduce employees
    print("\nIntroduction:")
    print(employee1.introduce())
    print(employee2.introduce())

    # Greeting
    print("\nGreeting:")
    print(employee1.greet(employee2))
