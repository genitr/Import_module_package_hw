"""Исполняемый модуль"""
import datetime
import logging
import sys

from src.application.db.people import get_employees
from src.application.salary import calculate_salary
from src.documents.data import headers, employees

date = datetime.datetime.now().date()


def main():
    get_employees(headers, employees)
    average_salary = calculate_salary(employees)
    print('-------------------------------------------------')
    print(f'средняя зарплата: {average_salary} рублей')
    print('-------------------------------------------------')
    print(date)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        main()
    except Exception as e:
        print(e)
