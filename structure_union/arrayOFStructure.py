from dataclasses import dataclass

@dataclass
class Student:
    id: int
    per: float
    name: str


record = []

for i in range(3):
    print("Enter Record:")
    name = input("Enter name: ")
    student_id = int(input("Enter Id: "))
    percentage = float(input("Enter percentage: "))

    record.append(Student(student_id, percentage, name))

for student in record:
    print("Record of Student")
    print("Id:", student.id)
    print("Name:", student.name)
    print("Percentage:", student.per)