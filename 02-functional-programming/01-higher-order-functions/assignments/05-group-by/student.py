from collections import defaultdict

def group_by(xs, key_function):
    grouped = defaultdict(list)
    for item in xs:
        key = key_function(item)
        grouped[key].append(item)
    return dict(grouped)


"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

def age(person):
    return person.age

people = [
    Person(name='John', age=14),
    Person(name='Marc', age=17),
    Person(name='Sophie', age=15),
    Person(name='Chris', age=17),
    Person(name='Morgan', age=15),
]

print(group_by(people, age))"
"""