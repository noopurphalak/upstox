import re


EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
PHONE_REGEX = re.compile(r"^[789][0-9]{9}$")


class Address(object):
    '''Class representing an Address'''

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
        self.people = []


class Person(object):
    '''Class representing a person'''

    def __init__(self, **kwargs):
        validated = [
            True if k in ['first_name', 'last_name'] else False for k in kwargs
        ]
        if False in validated or not validated:
            raise ValueError('Please enter both first name and last name of the person')

        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.street_addresses = []
        self.email_addresses = []
        self.phone_numbers = []
        self.groups = []
        self.addressbooks = []

    def add_street_address(self, address):
        if not isinstance(address, Address):
            raise TypeError('This function only accepts object of type Address')

        self.street_addresses.append(address)
        address.people.append(self)

    def add_email(self, email):
        if not EMAIL_REGEX.match(email):
            raise ValueError('Please input a proper email address')
        self.email_addresses.append(email)

    def add_phone(self, phone):
        if not PHONE_REGEX.match(phone):
            raise ValueError('Please input a proper 10 digit Phone Number')
        self.phone_numbers.append(phone)


class Group(object):
    '''Class representing a group of People'''

    def __init__(self):
        self.people = []
        self.addressbooks = []

    def add_person(self, person):
        if not isinstance(person, Person):
            raise TypeError('This function only accepts object of type Person')
        self.people.append(person)
        person.groups.append(self)


class AddressBook(object):
    '''Class representing an addressbook'''

    def __init__(self):
        self.people = []
        self.groups = []

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
        if not person_list:
            return []
        if last_name:
            selected = [person for person in person_list if person.first_name == first_name and person.last_name == last_name]
        else:
            selected = [person for person in person_list if person.first_name == first_name]

        return selected

    def _is_email_present(self, email_string, email_list):
        if not email_list:
            return False
        selected = [True if email_string in email else False for email in email_list]

        return True in selected

    def find_person_by_name(self, first_name, last_name=''):
        selected_list = self._find_person_by_name(first_name, last_name, self.people)

        for group in self.groups:
            selected_list += self._find_person_by_name(first_name, last_name, group.people)

        return selected_list

    def find_person_by_email(self, email_string):
        filtered_list = []

        for person in self.people:
            if self._is_email_present(email_string, person.email_addresses):
                filtered_list.append(person)

        for group in self.groups:
            for person in group.people:
                if self._is_email_present(email_string, person.email_addresses):
                    filtered_list.append(person)

        return filtered_list
