'''
The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

Sort the list and find the min and max age
Add the min age and the max age again to the list
Find the median age (one middle item or two middle items divided by two)
Find the average age (sum of all items divided by their number)
Find the range of the ages (max minus min)
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)


min(ages) 
max(ages)

ages.extend([min(ages),max(ages)])
print(f"New list: {ages}")


# Import statistics Library 
import statistics
print(statistics.median(ages))


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
avg=sum(ages)/len(ages)
print("The average is ", round(avg,2))


n_min = min(ages)
n_max = max(ages)
n_range = n_max - n_min
print(n_range)