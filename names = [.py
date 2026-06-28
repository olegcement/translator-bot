ivan = {
    "name": "Ivan",
    "age": 21,
    "city": "Warsaw"
}

def describe_person(person):
    return f"{person["name"]}, {person['age']} лет, живёт в {person["city"]}"

result = describe_person(ivan)
print(result)