## need a student object
class Student:
    def __init__(self, id, name, major, reason, excited_level, experience_level="low"):
        self.id = id
        self.name = name
        self.major = major
        self.reason = reason
        self.excited_level = excited_level
        self.experience_level = experience_level

class Course: 
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    

