"""People module"""

from src.common.common import fake_loading, employees_table

def get_employees(headers_: list[str], data: list[list[str]]):
    fake_loading('check login')
    fake_loading('check password')
    print('-------------------------------------------------')
    employees_table(headers_, data)


if __name__ == '__main__':
    pass