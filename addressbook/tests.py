import addressbook
import unittest


address = addressbook.Address(
    address1='1102, Mulund Saraswati CHSL',
    address2='Mulund EAST',
    landmark='Opp MHADA Bus Depot',
    city='Mumbai',
    country='India',
    pincode='400081'
)

p1 = addressbook.Person(
    first_name='Noopur',
    last_name='Phalak'
)
p1.add_street_address(address)
p1.add_email('noopurphalak007@gmail.com')
p1.add_phone('7208080835')

p2 = addressbook.Person(
    first_name='Ramakant',
    last_name='Phalak'
)
p2.add_street_address(address)
p2.add_email('ramakantphalak@gmail.com')
p2.add_phone('9876543211')

p3 = addressbook.Person(
    first_name='Rekha',
    last_name='Phalak'
)
p3.add_street_address(address)
p3.add_email('rekhaphalak@gmail.com')
p3.add_phone('9876643211')

g = addressbook.Group()
g.add_person(p1)
g.add_person(p3)

ab = addressbook.AddressBook()
ab.add_person(p2)
ab.add_group(g)


class TestAPIMethods(unittest.TestCase):

    def test_person_added_to_addressbook(self):
        assert len(ab.people) == 1
        assert ab.people[0].first_name == 'Ramakant'
        assert ab.people[0].last_name == 'Phalak'
        assert ab.people[0].email_addresses[0] == 'ramakantphalak@gmail.com'

    def test_group_added_to_addressbook(self):
        assert len(ab.groups) == 1
        assert len(ab.groups[0].people) == 2
        assert ab.groups[0].people[0].first_name == 'Noopur'
        assert ab.groups[0].people[1].first_name == 'Rekha'

    def test_members_by_group(self):
        assert len(g.people) == 2
        assert g.people[0].first_name == 'Noopur'
        assert g.people[1].first_name == 'Rekha'

    def test_group_from_person(self):
        assert p1.groups
        assert len(p1.groups) == 1

    def test_person_by_name(self):
        selected = ab.find_person_by_name(first_name='Noopur')
        assert selected
        assert len(selected) == 1
        assert selected[0].first_name == 'Noopur'
        selected = ab.find_person_by_name(first_name='asdasdasd')
        assert not selected

    def test_person_by_email(self):
        selected = ab.find_person_by_email(email_string='ramakant')
        assert selected
        assert len(selected) == 1
        assert selected[0].first_name == 'Ramakant'
        selected = ab.find_person_by_email(email_string='asd@asd.com')
        assert not selected


if __name__ == '__main__':
    unittest.main()
