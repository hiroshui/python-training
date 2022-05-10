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
    
    person = Person("Maxi","Krone","05.07.1993")
    
    print(person.getAgeInYears())
    
    print(person.say_hello())

    student = Student("Maxi", "Krone", "05.07.1993")
    print(student.learn("Java"))
    
    #base = MaxiBase()
    
    #base.print_something()
    
    #son = Derived()
    #son.print_something()
    

main()