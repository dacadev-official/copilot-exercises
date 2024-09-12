from pathlib import Path
import os

from models import Employee
from utils import load_csv_data
from services import benefits_service, report_benefits_service


def main() -> int:
    current_folder = Path(__file__).resolve().parent
    data_folder = current_folder / "../data"
    data_path = data_folder / "data.csv"

    employees_data = load_csv_data(data_path, Employee)
    benefits = benefits_service(employees_data)
    report_benefits_service(benefits, data_folder)

    return 0


if __name__ == "__main__":
    os._exit(main())
