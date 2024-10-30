"""Исполняемый модуль(грязный)"""
import datetime
import logging
import sys

from src.application.db.people import *
from src.application.salary import *
from src.documents.data import *

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