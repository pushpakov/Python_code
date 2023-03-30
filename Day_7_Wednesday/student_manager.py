class Student:
    def __init__(self, division: str, name: str, subject: str, roll: int):
        self.division = division
        self.name = name
        self.subject = subject
        self.roll = roll
    
    def __repr__(self):
        return f"Student(name='{self.name}', roll='{self.roll}', division='{self.division}', subject='{self.subject}')"

students = []

class StudentNotFoundError(Exception):
    pass

def create_student(division: str, name: str, subject: str, roll: int) -> None:
    student = Student(division, name, subject, roll)
    students.append(student)

def read_students() -> list:
    return students 

def read_student_by_roll(roll: int) -> Student:
    for student in students:
        if student.roll == roll:
            return student
    raise StudentNotFoundError(f"Student with roll number {roll} not found")

def update_student(roll: int, division: str = None, name: str = None, subject: str = None) -> bool:
    for student in students:
        if student.roll == roll:
            if division is not None:
                student.division = division
            if name is not None:
                student.name = name
            if subject is not None:
                student.subject = subject
            return True
    return False

def delete_student(roll: int) -> tuple:
    for index, student in enumerate(students):
        if student.roll == roll:
            deleted_student = students.pop(index)
            return ("The student with the following details is deleted from the list:", deleted_student)
    raise StudentNotFoundError(f"Student with roll number {roll} not found")

create_student('A', 'amar', 'Math', 1)
create_student('B', 'akbar', 'English', 2)
create_student('C', 'anthony', 'Science', 3)

try:
    print(read_students())
    print(read_student_by_roll(1)) 
    print(update_student(2, division=None, name="Lala", subject="Quantum Physics"))
    print(read_students())
    print(*delete_student(7))
    print(read_students())
except StudentNotFoundError as e:
    print(e)
