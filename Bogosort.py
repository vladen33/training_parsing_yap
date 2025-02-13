from random import shuffle


def bogosort(data):
    attempt = 1
    while not sorted(data) == data:
        print('Попытка #', attempt)
        attempt += 1
        shuffle(data)
    return data


if __name__ == '__main__':
    # Новый набор чисел для перемешевания.
    a = [8, 6, 1, 9, 3, 7, 2, 5, 4]
    print(bogosort(a))
    # Новая независимая команда.
    print('Строчка, которая гуляет сама по себе')
