
from datetime import date, timedelta

# Exercise 1
def countdown(n):
    while True:
        yield n
        if n == 0:
            break
        n -= 1
    
    

#for x in countdown(5):
#    print(x, end=" ")   # prints 5 4 3 2 1 0
#

# Exercise 2
def every_week(start):
    while True:
        yield start
        start += timedelta(days=7)

start_date = date(2022, 1, 3)       # Monday
weekly_appointment = every_week(start_date)

print(next(weekly_appointment))     # datetime.date(2022, 1, 3)
print(next(weekly_appointment))     # datetime.date(2022, 1, 10)
print(next(weekly_appointment))     # datetime.date(2022, 1, 17)

# Exercise 3
def reverse(word):
    length = len(word)
    while True:
        yield word[int(length - 1)]
        length -= 1
        if length <= 0:
            break

for char in reverse("Hello World"):
    print(char, end="")    # prints "dlroW olleH"