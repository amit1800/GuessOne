#This script keeps generating random five digit numbers till it generates 1
import random
i, n = 0, 0
while i!=1:
    i = random.randint(0,99999)
    print(i)
    n = n + 1
print("It took", n, "attempts to guess 1")