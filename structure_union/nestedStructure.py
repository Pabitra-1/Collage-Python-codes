from dataclasses import dataclass

@dataclass
class DOB:
    dd: int
    mm: int
    yy: int


@dataclass
class Student:
    name: str
    id: int
    dob: DOB


name = input("Enter Name: ")
student_id = int(input("Enter Roll No.: "))

mm = int(input("Enter Month: "))
dd = int(input("Enter Day: "))
yy = int(input("Enter Year: "))

student = Student(name, student_id, DOB(dd, mm, yy))

print("Name of student:", student.name)
print("Roll no.:", student.id)
print(f"Date of birth: {student.dob.mm}/{student.dob.dd}/{student.dob.yy}")