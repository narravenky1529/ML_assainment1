Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in a separate list using Loop. N: No of students (Read input from user)

Ex: L1: [150, 155, 145, 148]

Output: [68.03, 70.3, 65.77, 67.13]


l=[]
n=int(input("enter number of students"))
for i in range(0,n):
    element=int(input("enter weights of students in lb:"))
l.append(element)
print(l)
l_kg=[i*0.45 for i in l]
print("students weight in kg:"+str(l_kg))