'''
I am a teacher and I love to inspire and teach people”

How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''

string = "I am a teacher and I love to inspire and teach people"
list = string.split(' ')
print(list)

unique_count = len(set(list))
print(f"number of unique words in the given string is:{unique_count}")