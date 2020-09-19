#Task 1
import numpy as np
my_list = [1,2,3,4,5,6,7,8,9]
my_array = np.array(my_list)

#Task 2
my_array2 = np.arange(2,11)
print(my_array2)

#Task 3
my_array3 = np.zeros(10)
print(my_array3)
my_array3[5:8] = 11
print(my_array3)

#Task 4
Arr1 = np.modf(np.random.randn(10)*100)
Arr2 = np.modf(np.random.randn(10)*100)
print(Arr1, "\n")
print(Arr2, "\n")





