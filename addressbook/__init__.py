class Address(object):
    '''Class representing an Address'''

    address1 = ''
    address2 = ''
    landmark = ''
    city = ''
    country = ''
    pincode = ''
    people = []

    def __init__(self, **kwargs):
        super(Address, self).__init__()
        self.address1 = kwargs.get('address1')
        self.address2 = kwargs.get('address2')
        self.landmark = kwargs.get('landmark')
        self.city = kwargs.get('city')
        self.country = kwargs.get('country')
        self.pincode = kwargs.get('pincode')

    @property
    def __dict__(self):
        return {
            'address1': self.address1,
            'address2': self.address2,
            'landmark': self.landmark,
            'city': self.city,
            'country': self.country,
            'pincode': self.pincode,
            'people': self.people
        }


class Person(object):
    '''Class representing a person'''

    first_name = ''
    last_name = ''
    street_addresses = []
    email_addresses = []
    phone_numbers = []
    groups = []
    addressbooks = []


class Group(object):
    '''Class representing a group of People'''

    people = []
    addressbooks = []


class AddressBook(object):
    '''Class representing an addressbook'''

    people = []
    groups = []
