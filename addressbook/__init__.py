import re


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
        validated = [
            True if k in ['address1', 'address2', 'landmark', 'city', 'country', 'pincode'] else False for k in kwargs
        ]
        if False in validated or not validated:
            raise ValueError('Please enter all the values required for complete Address')
        self.address1 = kwargs.get('address1')
        self.address2 = kwargs.get('address2')
        self.landmark = kwargs.get('landmark')
        self.city = kwargs.get('city')
        self.country = kwargs.get('country')
        self.pincode = kwargs.get('pincode')


class Person(object):
    '''Class representing a person'''

    first_name = ''
    last_name = ''
    street_addresses = []
    email_addresses = []
    phone_numbers = []
    groups = []
    addressbooks = []

    def __init__(self, **kwargs):
        validated = [
            True if k in ['first_name', 'last_name'] else False for k in kwargs
        ]
        if False in validated or not validated:
            raise ValueError('Please enter both first name and last name of the person')

        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')


class Group(object):
    '''Class representing a group of People'''

    people = []
    addressbooks = []

    def add_person(self, person):
        if not isinstance(person, Person):
            raise TypeError('This function only accepts object of type Person')
        self.people.append(person)
        person.groups.append(self)


class AddressBook(object):
    '''Class representing an addressbook'''

    people = []
    groups = []

    def add_person(self, person):
        if not isinstance(person, Person):
            raise TypeError('This function only accepts object of type Person')
        self.people.append(person)
        person.addressbooks.append(self)

    def add_group(self, group):
        if not isinstance(group, Group):
            raise TypeError('This function only accepts object of type Group')

        if not group.people:
            raise Exception('An Empty Group cannot be added to the AddressBook')

        self.groups.append(group)
        group.addressbooks.append(self)

    def _find_person_by_name(self, first_name, last_name, person_list):
        if last_name:
            selected = [person for person in person_list if person.first_name == first_name and person.last_name == last_name]
        else:
            selected = [person for person in person_list if person.first_name == first_name]

        return selected

    def find_person_by_name(self, first_name, last_name=''):
        selected_list = self._find_person_by_name(first_name, last_name, self.people)

        for group in self.groups:
            selected_list += self._find_person_by_name(first_name, last_name, group.people)

        return selected_list

    def find_person_by_email(self, email_string):
        pass
