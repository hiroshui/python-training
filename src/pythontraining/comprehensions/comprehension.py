
#lists
names = ["johnson", "brewer", "smith", "rogers", "wilson", "jones", "amrstrong", "ray", "rich"]

#old way
names_capitalized = []
for item in names:
    names_capitalized.append(item.upper())    
print(names_capitalized)

#new way
names_capitalized = [item.upper() for item in names]
print(names_capitalized)

#dict
# Example
languages = ["C", "Java", "Python", "JavaScript"]

#old way
language_lengths = {}
for lang in languages:
    language_lengths[lang] = len(lang)
print(language_lengths)  # prints {'C': 1, 'Java': 4, 'Python': 6, 'JavaScript': 10}

#new way
language_lengths = {lang: len(lang) for lang in languages}
print(language_lengths)

#Exercise
employees = {"john": 1234, "claire": 1235, "danny": 1236}

new_employees = {}

for employee in employees:
    value = employees[employee]
    key = employee
    new_employees[value] = key

print(new_employees)

employees_reversed = {employees[employee]:employee for employee in employees}

print(employees_reversed)
# {1234: 'john', 1235: 'claire', 1236: 'danny'}
