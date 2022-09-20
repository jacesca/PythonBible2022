students = {
    'male': ['Tom', 'Charlie', 'Harry', 'Frank'],
    'female': ['Sarah', 'Huda', 'Samantha', 'Emily', 'Elizabeth']
}


print('Names list:', [name for key in students.keys() for name in students[key]])
name_that_has_a = [name for key in students.keys() for name in students[key] if 'a' in name]
print('Names that have an "a":', name_that_has_a)
