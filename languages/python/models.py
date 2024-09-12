from dataclasses import dataclass, field


@dataclass(frozen=True)
class Employee:
    id: str
    name: str
    email: str
    age: str
    salary: str
    department: str

    def __str__(self):
        return f"{self.name} ({self.email})"


@dataclass(frozen=True)
class Benefits:
    employee: Employee
    health: int
    end_of_year_bonus: int
    pension: int
    seniority_bonus: int
