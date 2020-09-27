#Task 1
import numpy as np
Matrix1 = np.random.randint(1,20,size=[3,5])
print(Matrix1)
np.median(Matrix1, axis=1)
print(Matrix1.max())
print(Matrix1.min())

#Task 2
print(Matrix1[:,1].max())
print(Matrix1[:,1].min())

#Task 3
print(np.median(Matrix1))


#Task 4
Matrix2 = np.random.randint(1,20,size=[2,2])
Matrix3 = np.random.randint(1,20,size=[2,6])
print(np.dot(Matrix2, Matrix3))