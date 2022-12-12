class Address:
    def __init__(self, street, number, flat_number, city, zip_code):
        self.street = street
        self.number = number
        self.flat_number = flat_number
        self.city = city
        self.zip_code = zip_code

    def __repr__(self):
        return (f'{self.street} {self.number}/{self.flat_number}\n'
                f'{self.zip_code} {self.city}')


class ChildWithAddress:
    def __init__(self, name, surname, address):
        self.address = address
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f'{self.name} {self.surname}\n{self.address}'


list_of_addresses = [
        ChildWithAddress(
            'Jasiu',
            'Kowalski',
            Address('Serniczkowa',
                    '4B',
                    2,
                    'Krakow',
                    '02-326'
                    )),
        ChildWithAddress(
            'Kasia',
            'Nowak',
            Address('Pierniczkowa',
                    '289',
                    55,
                    'Gdansk',
                    '02-326'
                    )),
        ChildWithAddress(
            'Asia',
            'Wisniewska',
            Address('Barszczykowa',
                    '234',
                    5,
                    'Rzeszow',
                    '37-326'
                    )),
        ChildWithAddress(
            'Tomek',
            'Wojcik',
            Address('Uszkowa',
                    '43H',
                    5,
                    'Wroclaw',
                    '02-326'
                    ))
    ]
for item in list_of_addresses:
    print(f"{item} \n" + (20 * "_"))