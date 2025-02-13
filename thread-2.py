import threading
from datetime import datetime
from tqdm import tqdm
from random import randint

import requests


def task(number):
    result = 0
    value = number ** number

    name = 'ID-' + str(randint(1000, 9999))
    for i in tqdm(range(1, value + 1), desc=name, colour='GREEN'):
        result += i
        if i % 1000000 == 0:
            requests.get('https://python.org')

    print('Среднее арифметическое равно:', result / value)


if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()
    t1 = threading.Thread(target=task, args=(8,))
    t2 = threading.Thread(target=task, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')
