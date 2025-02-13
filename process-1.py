import multiprocessing
from datetime import datetime

import requests


def task(number):
    result = 0
    value = number ** number

    for i in range(1, value + 1):
        result += i
        if i % 1000000 == 0:
            requests.get('https://python.org')

    print('Среднее арифметическое равно:', result / value)


if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()
    t1 = multiprocessing.Process(target=task, args=(8,))
    t2 = multiprocessing.Process(target=task, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
