import numpy as np
x = np.repeat("*",10, axis = 0)
print(x, "\n")

#Task 1

my_list = [1,2,3,4,5,6,7,8,9]
my_array = np.array(my_list)
print(my_array, "\n", x, "\n")

#Task 2
my_array2 = np.arange(2,11)
print(my_array2, "\n", x, "\n")

#Task 3
my_array3 = np.zeros(10)
print(my_array3)
my_array3[5:8] = 11
print(my_array3, "\n", x, "\n")

#Task 4
Arr1 = np.arange(10)
Arr2 = np.arange(11)
print(Arr1)
print(Arr2)
for i in range(0, len(Arr1)):
    print(i, Arr1[i]==Arr2)
print("\n", x)
