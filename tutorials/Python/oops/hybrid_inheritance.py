# Base class
class SchoolMember:
    def __init__(self, name):
        self.name = name

# Inherited from SchoolMember (single inheritance)
class Teacher(SchoolMember):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def getDetails(self):
        return f"Teacher: {self.name}, Subject: {self.subject}"

# Inherited from SchoolMember (single inheritance)
class Student(SchoolMember):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def getDetails(self):
        return f"Student: {self.name}, Grade: {self.grade}"

# Inherited from both Teacher and Student (multiple inheritance)
class TeachingAssistant(Student, Teacher):
    def __init__(self, name, grade, subject):
        Student.__init__(self, name, grade)
        Teacher.__init__(self, name, subject)

# Example usage
ta = TeachingAssistant('John', 'A', 'Mathematics')
print(ta.getDetails())  # Output depends on method resolution order (MRO)