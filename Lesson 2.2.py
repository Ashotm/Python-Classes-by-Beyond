#Task 1
import numpy as np
Str="*****************************"
print(Str)
Matrix1 = np.random.randint(1,10, size=[3,3])
Matrix2 = np.random.randint(1,10, size=[3,3])
MultMat = np.dot(Matrix1, Matrix2)
print(MultMat, "\n", Str)
print(Matrix1)

#Task 2
print (np.linalg.det(Matrix1), "\n", Str)

#Task 3
print (np.diagonal(Matrix1),"\n", Str)
print (np.trace(Matrix1),"\n", Str)

#Task 4
Matrix1Inv = np.linalg.inv(Matrix1)
print(Matrix1Inv,"\n", np.dot(Matrix1Inv, Matrix1),"\n",  Str)

#Task 5
Matrix3 = np.random.randint(1,10, size=[3,3])
np.save("Matrix3", Matrix3)
LoadMatrix3 = np.load("Matrix3.npy")
print (Matrix3, "\n", LoadMatrix3)
