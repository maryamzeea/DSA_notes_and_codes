#TIME COMPLEXITY
import datetime
from time import time

def sum_of_n(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
#
# def sum_of_n(n):
#     return f"{n * (n + 1) / 2:.0f}"
start_time = time()
time_stamp_start =datetime.datetime.fromtimestamp(start_time)
X = sum_of_n(50000000)
end_time = time()
end_time_stamp = datetime.datetime.fromtimestamp(end_time)
duration = end_time - start_time
print(X)
print(time_stamp_start)
print(end_time_stamp)
print(f"{duration:.10f} seconds")