import time
import math
s = time.time()
counter = 0
for i in range(int(pow(10,8)*math.log(pow(10,8), 2))):
    counter += 1
    print(counter)
e = time.time()
print(e-s)