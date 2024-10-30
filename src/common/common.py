"""
Модуль содержит функции для имитации загрузки
"""
from time import sleep

from tqdm import tqdm
from tabulate import tabulate


def fake_loading(desc_: str):
    with tqdm(total=100, desc=desc_) as pbar:
        for i in range(20):
            sleep(0.1)
            pbar.update(5)
        pbar.set_description('Success')


def employees_table(headers_: list[str], data: list[list[str]]):
    print(
        tabulate(
            tabular_data=data,
            headers=headers_,
            tablefmt='github'
        )
    )
