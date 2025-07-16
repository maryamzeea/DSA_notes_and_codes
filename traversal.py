# Print the sum, maximum, and minimum value from this array: [25, 42, 17, 89, 53, 17]
# Count how many times 17 appears in the array.
import array as arr
#sum
A = arr.array('i',[25, 42, 17, 89, 53, 17])

Total = 0

for num in A:
    Total += num
print("sum =",Total)

#maximum
max_value = max(A)
for num in A:
    if num > max_value:
        max_value = num
print("max =",max_value)

#minmum
min_value = min(A)
for num in A:
    if num < min_value:
        min_value = num
print("min =",min_value)

#count
total = A[-1]
count = 0
for num in A:
    if num == total:
        count += 1
print("count =",count)