'''
The diagram below shows a dataset with 2 classes and 8 data points, each with only one feature value, labeled f. Note that there are two data points with the same feature value of 6. These are shown as two x’s one above the other.


Divide this data equally into two parts. Use first part as training and second part as testing. Using KNN classifier, for K=3, what would be the predicted outputs for the test samples? Show how you arrived at your answer.
Compute the confusion matrix for this and calculate accuracy, sensitivity and specificity values.
'''


import numpy as np
from sklearn.model_selection import train_test_split #train_test_split to split the data
from sklearn.neighbors import KNeighborsClassifier #this library is to implement kNN
#Given
f = [1,2,3,6,6,7,10,11]
label = [1,1,2,2,2,1,1,2]
data = []

for i in range(0,len(f)):
  data.append([f[i],label[i]])

x = np.array(data)

#classes as per given question
y = np.array([0,0,1,1,1,0,0,0])
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.5, random_state= 0, shuffle = False)


#given to implement KNN with k=3
neighbor = KNeighborsClassifier(n_neighbors = 3)  
neighbor.fit(X_train,y_train) 
y_pred = neighbor.predict(X_test) 
print(y_test)
y_pred