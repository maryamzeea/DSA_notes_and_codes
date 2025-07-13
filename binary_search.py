import array as arr
# L = list(map(int,input("Enter a list:").split()))
# A = arr.array('i',L)
#
# def binary_search(arr,x):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         if arr[mid]==x:
#             return f"{x} is at index {mid}"
#         elif arr[mid]<x:
#             low = mid+1
#         else:
#             high = mid-1
#
#     return f"{x} is not in the list"
#
# x=int(input("Enter a number:"))
# print(binary_search(A,x))

#INDEX TRACES
# B = [2, 4, 7, 11, 18, 23, 29]
# C = arr.array('i',B)
#
# def binary_search_index(arr,x):
#     low=0
#     high=len(arr)-1
#     while low<=high:
#         mid=(low+high)//2
#         print(f"searching for at index {mid} is {arr[mid]}")
#         if arr[mid]==x:
#             return f"{x} is at index {mid}"
#         elif arr[mid]<x:
#             low = mid+1
#         else:
#             high = mid-1
#     return f"{x} is not in the list"
#
# for search_value in [11,23,28]:
#     print(f"searching for {search_value}")
#     print(binary_search_index(C,search_value))

# A = arr.array('i', [5, 10, 15, 20, 25, 30])
#
# def binary_search(A, x):
#     low = 0
#     high = len(A) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if A[mid] == x:
#             return f"{x} is found at index {mid}"
#         elif A[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return "Index out of range(-1)"
#
# print(binary_search(A, 25))
# print(binary_search(A, 18))

# A = arr.array('i', [101, 104, 109, 112, 115, 120, 125])
#
# def binary_search(A, x):
#     low = 0
#     high = len(A) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         print(f"Checking index {mid}:{A[mid]}")
#         if A[mid] == x:
#             return f"{x} is at index {mid}"
#         elif A[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return f"{x} is not in the list"
#
# x= int(input("Enter a number: "))
# print(binary_search(A,x))


