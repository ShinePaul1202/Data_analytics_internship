from abc import ABC, abstractmethod


# ============================================================
# Abstract Class: Person
# ============================================================

class Person(ABC):

    def __init__(self, name, age, gender, address):
        """
        Initialize the attributes of a Person.
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

        # Cooperative inheritance
        super().__init__()

    # --------------------------------------------------------
    # Magic Method
    # --------------------------------------------------------

    def __str__(self):
        """
        Return the person's details in the required format.
        """
        return (
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Gender: {self.gender}, "
            f"Address: {self.address}"
        )

    # --------------------------------------------------------
    # Greet Method
    # --------------------------------------------------------

    def greet(self, other_person):
        """
        Greet another Person object.
        """
        return f"Hello {other_person.name}! My name is {self.name}."

    # --------------------------------------------------------
    # Abstract Method
    # --------------------------------------------------------

    @abstractmethod
    def introduce(self):
        """
        Abstract method that must be implemented
        by child classes.
        """
        pass

    # --------------------------------------------------------
    # Static Method
    # --------------------------------------------------------

    @staticmethod
    def is_adult(age):
        """
        Return True if age is 18 or above,
        otherwise return False.
        """
        return age>=18


# ============================================================
# Child Class for Demonstration
# ============================================================

class Student(Person):

    def __init__(self, name, age, gender, address):
        """
        Initialize Student using the parent class constructor.
        """
        super().__init__(name, age, gender, address)

    def introduce(self):
        """
        Implement the abstract introduce() method.
        """
        return f"Hello, my name is {self.name}."


# ============================================================
# Main Program
# ============================================================

if __name__=="__main__":

    try:

        # Create two Student objects
        person1 = Student(
            "John",
            21,
            "Male",
            "Kochi"
        )

        person2 = Student(
            "Anu",
            17,
            "Female",
            "Thrissur"
        )

        # Demonstrate __str__()
        # ----------------------------------------------------

        print("Person 1:")
        print(person1)

        print("\nPerson 2:")
        print(person2)

        # Demonstrate greet()
        # ----------------------------------------------------

        print("\nGreeting:")
        print(person1.greet(person2))

        # Demonstrate introduce()
        # ----------------------------------------------------

        print("\nIntroduction:")
        print(person1.introduce())
        print(person2.introduce())

        # Demonstrate is_adult()
        # ----------------------------------------------------

        print("\nAdult Check:")
        print("Is person 1 an adult?", Person.is_adult(person1.age))
        print("Is person 2 an adult?", Person.is_adult(person2.age))

    except TypeError as error:
        print("TypeError:", error)

    except Exception as error:
        print("An unexpected error occurred:", error)