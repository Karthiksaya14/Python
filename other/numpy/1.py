import numpy as np

array= [10,20,30,40,50]

arr= np.array(array)
print (arr)

print(f"The type of the array is:{type(arr)}")

multiply = arr * 20

print(F"The array after multiplication is: {multiply}")

mean= np.mean(arr)
print(f"The mean of the array is: {mean}")
