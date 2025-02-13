import multiprocessing
from datetime import datetime


def task(number):
    result = 0
    value = number ** number

    for i in range(1, value + 1):
        result += i
    print('Среднее арифметическое равно:', result / value)

if __name__ == '__main__':
    print('Начало работы основного потока')

    start_time = datetime.now()

    t1 = multiprocessing.Process(target=task, args=(8,))
    t2 = multiprocessing.Process(target=task, args=(8,))
    t3 = multiprocessing.Process(target=task, args=(8,))
    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    COUNT = 3
    # procs = [multiprocessing.Process(target=task, args=(8,)) for _ in range(COUNT)]
    # for proc in procs:
    #     proc.start()
    #     proc.join()

    end_time = datetime.now()

    print('Окончание работы основного потока')
    print(f'Итоговое время выполнения: {end_time - start_time} секунд.')