import pytest 
from registration import count_registrations, create_attendee_list

@pytest.fixture
def registrations():
    return [
        {'first_name': 'John', 'last_name': 'Doe'},
        {'first_name': 'Jane', 'last_name': 'Smith'},
        {'first_name': 'Diana', 'last_name': 'Rogers'}
    ]

def test_count_registrations(registrations):
    count = count_registrations(registrations)
    assert count == 3

def test_create_attendee_list(registrations):
    attendees = create_attendee_list(registrations)
    assert attendees == ['John Doe', 'Jane Smith', 'Diana Rogers']
