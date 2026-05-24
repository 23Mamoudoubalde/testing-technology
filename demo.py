# A list is ordered and changeable (mutable).
# Lists use square brackets [].
values = [1,2,"Go", 4, 5, 7, "worldcup"]
print(values[0]) #1
print(values[-1]) # last values worldcup
values.insert(3,"added value")
print(values) #[1, 2, 'Go', 'added value', 4, 5, 7, 'worldcup']
# to update
values[0] = 10
print(values) # [10, 2, 'Go', 'added value', 4, 5, 7, 'worldcup']
# TUPLE
# A tuple is ordered but NOT changeable (immutable).
# Tuples use parentheses ().

my_tuple = (10, 20, 30, 40)

print(my_tuple)

# accessing tuple values
print(my_tuple[1])

# DICTIONARY
# A dictionary stores data in key:value pairs.
# Dictionaries use curly braces {}.

student = {
    "name": "Mamoudou",
    "age": 21,
    "course": "Python"
}

print(student)

# accessing dictionary values
print(student["name"])

# changing dictionary value
student["age"] = 22

print(student)