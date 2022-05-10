from datetime import date, datetime

class Person:
    def __init__(self, firstname : str, lastname: str, age : str):
        self.firstname = firstname
        self.name = lastname
        self.age = datetime.strptime(age,"%d.%m.%Y")
        
    def getAgeInYears(self):
        ageInDays = self.getAgeInDays()
        ageInYears = ageInDays / 365
        return ageInYears
    
    def getAgeInDays(self):
        today = datetime.now()
        agedif = today - self.age
        return agedif.days
    
    def say_hello(self):
        return f"{self.firstname} says hello"