'''
se a tab escape sequence to get the following lines.

Name Age Country City

Asabeneh 250 Finland Helsinki
'''

string = "I am a teacher and I love to inspire and teach people"
list = string.split(' ')
print(list)

unique_count = len(set(list))
print(f"number of unique words in the given string is:{unique_count}")