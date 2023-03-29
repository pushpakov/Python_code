# a student management task to perform the crud operation 

class Student:
    def __init__(self, division, name, subject, roll):
        self.division = division
        self.name = name
        self.subject = subject
        self.roll = roll
    def __repr__(self):
        return f"Student(name='{self.name}', roll='{self.roll}',division='{self.division}', subject='{self.subject}')"
    
students = []

def create_student(division, name, subject, roll):
    student = Student(division, name, subject, roll)
    students.append(student)

def read_students():
    return students 

def read_student_by_roll(roll):
    for student in students:
        if student.roll == roll:
            return student
        return None

def update_student(roll, division=None, name=None, subject=None):
    for student in students:
        if student.roll == roll:
            if division:
                student.division = division
            if name:
                student.name = name
            if subject:
                student.subject = subject
            return True
    return False

def delete_student(roll):
    for index, student in enumerate(students):
        if student.roll == roll:
            pooped = students.pop(index)
            return ("The student with following detail is deleted from the list : ", pooped)
    return False

create_student('A', 'amar', 'Math', 1)
create_student('B', 'akbar', 'English', 2)
create_student('C', 'anthony', 'Science', 3)


print(read_students())
print(read_student_by_roll(1)) 
print(update_student(2, division=None, name="Lala", subject="Quantum Physics"))
print(read_students())
print(*delete_student(3))
print(read_students())








