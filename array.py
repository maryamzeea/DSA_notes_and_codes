#initilization of array

import array as arr
A = arr.array("i", [1, 2, 3, 4, 5]) #A=reference , array=constructor, i=type , []=list-value
#type i compulsory, list is optional(empty array means none), Array reference is optional
#second parameter in the array constructor always be python list
print(A[0])
print(A[4])
print(A[-2])

B = arr.array("f", [1.1, 2.1, 3.4, 4.2, 5.9])
print(f"{B[0]:.2f} {B[1]:.3f} {B[2]:.4f} {B[3]:.5f}")

C=arr.array("f")
C.append(3.4)
print(f"{C[0]:.3f}")
#ANONYMOUS ARRAY
print(f"{arr.array("f", [1.1, 2.1, 3.4, 4.2, 5.9]) [1]:.2f}")
#floating value list can't be converting into integer but integer can be converting into float
print(arr.array("f", [1,3,5,6,3,2,4]) [2])