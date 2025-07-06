#fibonacci series

# def fibonacci(n):
#     if n < 0:
#         return
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(9))

n = int(input())

a,b =0,1
for i in range(0,n):
    a,b = b,a+b

print(f"F({n}) = {a}")
