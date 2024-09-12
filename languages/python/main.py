from pathlib import Path
import os

from services import benefits_service, report_benefits_service, load_employee_service


def main() -> int:
    current_folder = Path(__file__).resolve().parent
    data_folder = current_folder / "../data"
    data_path = data_folder / "data.csv"

    employees = load_employee_service(data_path)
    benefits = benefits_service(employees)
    report_benefits_service(benefits, data_folder)

    return 0


if __name__ == "__main__":
    os._exit(main())
