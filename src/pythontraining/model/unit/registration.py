from typing import List, Dict

def count_registrations(registration_list : List[Dict[str,str]]):
    return len(registration_list)

def create_attendee_list(registration_list : List[Dict[str,str]]):
    erg_list : List[str] = []
    
    for attende in registration_list:
        firstname = attende.get("first_name")
        lastname = attende.get("last_name")
        fullname = f"{firstname} {lastname}"
        erg_list.append(fullname)
    return erg_list
