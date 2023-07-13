import numpy as np

list_1 = np.array([1,2,3,4,5,6])
list_2 = np.array([[1,2,3],[4,5,6]])

x = [1,2,3,4,5,6]
y = [[1,2,3],[4,5,6]]


print(list_1, x)
print(list_2, y)


#________________

print(list_1[1:4])
print(list_2[0])


#________________


list_3 = np.array([1,2,3,4,5,6])

print(list_3)
print("Reshape: ", list_3.reshape(2, 3))


#_______________


print("Mean: ", np.mean(list_3))
print("Max: ", np.max(list_3))
print("Sum: ", np.sum(list_3))


