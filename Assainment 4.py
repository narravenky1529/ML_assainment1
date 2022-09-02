'''
_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
Convert the ages to a set and compare the length of the list and the set.
'''

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
len(it_companies)

it_companies.add('twitter')
print(it_companies)

it_companies.update(['hcl','tcs','cap gemini'])
print(it_companies)

it_companies.remove('twitter')
print(it_companies)

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
C=A.union(B)
print(C)

print(A.intersection(B))

print(A.issubset(B)) 

print(A.isdisjoint(B)) 


print(A.symmetric_difference(B))

A.update(B)
print(A)


B.update(A)
print(B)


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.clear()
B.clear()

age = [22, 19, 24, 25, 26, 24, 25, 24]
st=set(age)
print(st)

len(age)

len(st)
