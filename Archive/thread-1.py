from datetime import datetime
from tqdm import tqdm

import requests


def task(number):
    result = 0
    value = number ** number

    for i in tqdm(range(1, value + 1)):
        result += i
        if i % 1000000 == 0:
            # Вот он GET-запрос.
            requests.get('https://python.org')

    print('Среднее арифметическое равно:', result / value)


if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()

    task(8)
    task(8)

    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.') 