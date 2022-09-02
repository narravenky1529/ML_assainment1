'''

Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list

'''

dog = {}
# Dictionary with data values
dog= {'name':'cheddy', 'color':'yellow', 'breed':'german sheperd', 'legs':'four','age':'5'}

print(dog)

student = {
    'first_name':'venkat',
    'last_name':'narra',
    'gender':'male',
    'age':'22',
    'martial status':'un married',
    'skills':['JavaScript', 'Python'],
    'country':'india',
    'city':'guntur',
    'address':{
        'street':'jai balayya',
        'zipcode':'66223'
    }
    }

print(student)

len(student)
print(student['skills'])

print(type ('skills'))


student['skills'].append('HTML')
print(student)

keys = student.keys()
print(keys) 

values = student.values()
print(values)



