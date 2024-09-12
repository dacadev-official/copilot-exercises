from pathlib import Path
from typing import TypeVar
import csv


T = TypeVar("T")


def load_csv_data(path: Path, data_cls: T) -> list[T]:
    with open(path, "r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return [data_cls(**row) for row in reader]


def record_data_to_csv(path: Path, data: list[T]) -> None:
    if len(data) <= 0:
        return

    with open(path, "w", encoding="utf-8") as csvfile:
        headers = data[0].__dict__.keys()
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()

        list(map(lambda d: writer.writerow(d.__dict__), data))


def record_data(path: Path, data: str) -> None:
    with open(path, "w", encoding="utf-8") as file:
        file.write(data)
