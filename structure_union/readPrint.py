from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int
    salary: float


emp = Employee(
    input("Enter name: "),
    int(input("Enter ID: ")),
    float(input("Enter salary: "))
)

print("******** Printing the details of employee *****")
print("Name:", emp.name)
print("ID:", emp.id)
print("Salary:", emp.salary)