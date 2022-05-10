
from re import L
from model.bankaccount import BankAccount
from model.person import Person
from model.student import Student

def main():
    """Entry point for the application script"""
    print("Hello World!")
    
    #bankaccount
    account = BankAccount("Maxi")
    account.deposit(100)
    account.display_balance()
    print(str(account))
    
    account_new = BankAccount("Joris")
    account_new.deposit(99)
    print(account < account_new)
    account_new.deposit(2)
    print(account < account_new)
    
    person = Person("Maxi","Krone","05.07.1993","177")
    print(person.getAgeInYears())
    print(person.say_hello())
    print(person.ageInYears);
    print(person.fullname)
    
    #person.set_name("Joris","Hoendervangers")
    
    print (person.fullname)
    
    print(repr(person))
    student = Student("Maxi", "Krone", "05.07.1993","180")
    print(student.learn("Java"))
    
    print(student < person)
    
    #base = MaxiBase()
    #base.print_something()
    #son = Derived()
    #son.print_something()

main()