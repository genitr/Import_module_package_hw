"""Salary module"""
from src.documents.data import employees


def calculate_salary(salary_data: list[list]):
    salary_count = 0
    employees_count = len(salary_data)

    for row in salary_data:
        salary_count += row[-1]

    average = salary_count // employees_count
    return average


if __name__ == '__main__':
    calculate_salary(employees)
