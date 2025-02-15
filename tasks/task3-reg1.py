# Импортируйте модуль для работы с регулярными выражениями.
import re

addresses = [
    ('Он проживал в городе Иваново на улице Наумова. '
     'Номер дома 125 был зеркальной копией его номера квартиры 521'),
    'Адрес: город Новосибирск, улица Фрунзе, дом 321, квартира 15.'
]

# С помощью регулярных выражений извлеките из обеих строк названия городов и улиц,
# номера домов и квартир. Распечатайте результат.

for address in addresses:
    # Напишите регулярное выражение.
    pattern = r'.*городе? (?P<city>\w+).* улиц[ае] (?P<street>\w+).+? (?P<house>\d+).*? квартир[ыа] (?P<flat>\d+).*'

    # Примените метод регулярных выражений, который
    # найдёт шаблон pattern в строке address.
    address_match = re.search(pattern, address)
    city = address_match.group('city')
    street = address_match.group('street')
    house = address_match.group('house')
    flat = address_match.group('flat')


    # Распечатайте названия городов и улиц, номера домов и квартир
    # из обеих строк.
    print(city, street, house, flat)
