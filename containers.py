print('<---------------Ex One------------------>')
students = ['Brad', 'Kelsey', 'Katie', 'Erica']
print(students[1])
print(students[-1])

print('<---------------Ex Two------------------>')
foods = ('Bacon', 'Chicken', 'Cheese', 'Yogurt')
for food in foods:
    print(f'{food} is a good food.')

print('<---------------Ex Three------------------>')
for food in foods[-2:]:
    print(food)

#non for Loop
print(foods[2:])

print('<---------------Ex Four------------------>')
home_town = {
    'city': 'Welland',
    'state': 'Ontario',
    'population': 50000
}

print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

print('<---------------Ex Five------------------>')
print(home_town.items())

for key, value in home_town.items():
    print(f"{key} = {value}")

print('<---------------Ex Six------------------>')
cohort = []

for index, student in enumerate(students):
    cohort.append({
        'student': student,
        'fav_food': foods[index]
    })

for student in cohort:
    print(student)

print('<---------------Ex Seven------------------>')

awesome_students = [f'{name} is awesome!'for name in students]

for student in awesome_students:
    print(student)

print('<---------------Ex Eight------------------>')

for food in [food for food in foods if 'a' in food]:
    print(food)

