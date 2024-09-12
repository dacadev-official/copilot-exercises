from pathlib import Path
from io import StringIO

from models import Employee, Benefits
from constants import (
    HEALTH_PERCENTAGE,
    END_OF_YEAR_BONUS_PERCENTAGE,
    PENSION_PERCENTAGE,
    MINIMUM_AGE_FOR_SENIORITY_BONUS,
    SENIORITY_BONUS_PERCENTAGE,
)
from utils import record_data_to_csv, record_data


def benefits_service(employees: list[Employee]) -> list[Benefits]:
    benefits = []

    for e in employees:
        salary = int(e.salary)
        age = int(e.age)

        health = HEALTH_PERCENTAGE * salary
        end_of_year_bonus = END_OF_YEAR_BONUS_PERCENTAGE * salary
        pension = PENSION_PERCENTAGE * salary
        seniority_bonus = (
            SENIORITY_BONUS_PERCENTAGE * salary
            if MINIMUM_AGE_FOR_SENIORITY_BONUS < age
            else 0
        )

        benefits.append(
            Benefits(
                health=health,
                end_of_year_bonus=end_of_year_bonus,
                pension=pension,
                seniority_bonus=seniority_bonus,
                employee=e,
            )
        )

    return benefits


def report_benefits_service(benefits: list[Benefits], dest_folder: Path) -> None:
    health_sum = 0
    end_of_year_bonus_sum = 0
    pension_sum = 0
    seniority_bonus_sum = 0
    LINE_LENGTH = 30

    buffer = StringIO()
    write_separator = lambda: buffer.write("-" * LINE_LENGTH + "\n")

    write_separator()
    buffer.write("Report of Benefits".center(LINE_LENGTH) + "\n")
    write_separator()

    for b in benefits:
        buffer.write(f"Employee: {b.employee.name} ({ b.employee.email})\n")
        buffer.write(f"Department: {b.employee.department}\n")
        buffer.write(f"Salary: ${b.employee.salary}\n")
        buffer.write("\n")
        buffer.write("Benefits sum\n")
        buffer.write(f"- Health: ${b.health}\n")
        buffer.write(f"- End of year bonus: ${b.end_of_year_bonus}\n")
        buffer.write(f"- Pension: ${b.pension}\n")
        buffer.write(f"- Seniority bonus: ${b.seniority_bonus}\n")
        buffer.write("\n")

        write_separator()

        health_sum += b.health
        end_of_year_bonus_sum += b.end_of_year_bonus
        pension_sum += b.pension
        seniority_bonus_sum += b.seniority_bonus

    buffer.write("Total Benefits for all employees\n")
    write_separator()

    buffer.write(f"- Health: ${health_sum}\n")
    buffer.write(f"- End of year bonus: ${end_of_year_bonus_sum}\n")
    buffer.write(f"- Pension: ${pension_sum}\n")
    buffer.write(f"- Seniority bonus: ${seniority_bonus_sum}\n")

    record_data_to_csv(dest_folder / "benefits.csv", benefits)
    record_data(dest_folder / "report.txt", buffer.getvalue())
