from datetime import date, datetime
from functools import total_ordering
import math


"""_summary_
Raises:
    TypeError: _description_
    AttributeError: _description_
    AttributeError: _description_
Returns:
    _type_: _description_
"""
@total_ordering
class Person:
    def __init__(self, firstname : str, lastname: str, age : str, height : int):
        self._firstname = firstname
        self._lastname = lastname
        self._birthday = datetime.strptime(age,"%d.%m.%Y")
        self.ageInDays=self.getAgeInDays()
        self.ageInYears=self.getAgeInYears()
        self.height = height
    
    def check_instance(self, other):
        if not isinstance(other, Person):
            raise TypeError("Cannot compare Person with different class.")    
    
    def getAgeInYears(self):
        ageInDays = self.getAgeInDays()
        daysInYear = 365
        ageInYears = math.trunc(ageInDays / daysInYear)
        return ageInYears
    
    def getAgeInDays(self):
        today = datetime.now()
        agedif = today - self._birthday
        return agedif.days
    
    def say_hello(self):
        return f"{self._firstname} says hello"
    
    def __repr__(self):
        rep = 'Person(' + self.get_name() + ',' + str(self.ageInYears) + ')'
        return rep
    
    def __gt__(self, other):
        self.check_instance(other)
        return self.height > other.height
    
    def __eq__(self, other):
        self.check_instance(other)
        return self.height == other.height
    
    
    '''
    Getter and setter
    '''

    def get_name(self):
        return f"{self._firstname} {self._lastname}"

    def set_name(self, aiFirstname : str, aiLastname : str):
        raise AttributeError("can't set attribute")

    #def set_name(self, aiFirstname : str, aiLastname : str):
    #    if len(aiFirstname) <= 1 or len(aiLastname) <= 1:
    #        raise ValueError("The first- or lastname is too short")
    #    firstname = aiFirstname.capitalize()
    #    lastname = aiLastname.capitalize()
    #    self._name = f"{firstname} {lastname}"

    def del_name(self):
        raise AttributeError("Deleting is not allowed, you can only change a person's name.")
        #del self._name

    fullname = property(get_name, set_name, del_name,"I am the fullname of a person") 

    @property
    def age(self):
        return self.getAgeInYears()

    @age.setter
    def age(self, birthday):
        self._birthday = datetime.strptime(birthday,"%d.%m.%Y")
