import array as arr

#BUBBLE SORTING
# A = arr.array("i",[13, 7, 25, 9, 17])

# for i in range(len(A)):
#     for j in range(0,len(A)-i-1):
#         if A[j] > A[j+1]:
#             A[j], A[j+1] = A[j+1], A[j]
#     print(f"pass{i+1}:{A.tolist()}")

#DESCENDING ORDER
# for i in range(len(A)):
#      for j in range(0,len(A)-i-1):
#          if A[j] < A[j+1]:
#              A[j], A[j+1] = A[j+1], A[j]
#      print(f"pass{i+1}:{A.tolist()}")
#

#SELECTION SORTING
# A= arr.array("i",[29, 10, 14, 37, 13])
#
# for i in range(0,len(A)):
#     min_value = i
#     for j in range(i+1,len(A)):
#         if A[j] < A[min_value]:
#             min_value = j
#     A[i],A[min_value] = A[min_value],A[i]
#     print(f"pass{i+1}:{A.tolist()}")

#DECSENDING ORDER
# A = arr.array("i", [18, 5, 9, 12, 3])
#
# for i in range(0,len(A)):
#     min_value = i
#     for j in range(i+1,len(A)):
#         if A[j] > A[min_value]:
#             min_value = j
#     A[min_value], A[i]  =  A[i],A[min_value]
#     print(f"pass{i+1}:{A.tolist()}")



