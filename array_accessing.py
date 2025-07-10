import array as arr
import timeit

A = arr.array("i", [1, 2, 3, 4, 5])
print(A[-2])
#access individual element using subscription
#access multiple element using subscription with loop
B = arr.array("i", [12, 23, 34, 45, 55])
print("Index"+" "+"Elements")
for i in range(len(B)):
    print(f"  {i}  =  {B[i]}\n")

#print horizontally
C = arr.array("i", [11, 22, 33, 42, 52])
for i in range(len(C)):
    print(C[i], end=" ")

#negtive indexing

D = arr.array("i", [11, 22, 33, 42, 52])
time_taken = timeit.timeit(lambda: D[3], number=1)
print(f"\n{time_taken:.10f}")

for i in range(len(D)-1,-1,-1):
    print(i, end="\n")
    print(D[i], end="\n ")

#forward indexing
E = arr.array("i", [19, 53, 213, 244, 93])
for i in range(len(E)):
    print(i, end=" \n")
    print(E[i], end=" \n")