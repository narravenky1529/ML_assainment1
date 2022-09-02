'''
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
'''



sisters=('lavanya','indra','akhila')
brothers=('ajay','ntr')
print(sisters)
print(brothers)

sisters=('lavanya','indra','akhila')
brothers=('ajay','ntr')
siblings = sisters + brothers
print(siblings)

temp = list(siblings)
temp.extend(['Raju','Rani'])
family_members = tuple(temp)
print(f"family members are:{family_members}")
