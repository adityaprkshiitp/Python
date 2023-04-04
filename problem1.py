import numbers
from sre_constants import RANGE


N = int(input())
numbers = range (N+1)
count=0
for i in numbers :
    count +=i
print(count)
