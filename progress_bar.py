from time import sleep

from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(20), desc='Прогресс чтения данных'):
        sleep(0.1)

    for j in tqdm(range(60), desc='Прогресс анализа данных'):
        sleep(0.1)

    for j in tqdm(range(40), desc='Прогресс записи данных'):
        sleep(0.1)
