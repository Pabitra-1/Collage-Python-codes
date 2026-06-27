from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    id: int
    salary: float


emp = Employee("Pabitra Pal", 654656465, 18000)

print("Name:", emp.name)
print("ID:", emp.id)
print("Salary:", emp.salary)