from random import random

def is_in(r):
    x = random() * r * 2
    y = random() * r * 2
    #print( (x - r) ** 2 + (y - r) ** 2 <= r ** 2 ),
    return (x - r) ** 2 + (y - r) ** 2 <= r ** 2

total = 100000
success = 0.0
for _ in range(total):
    if is_in(1):
        success += 1
print(success / total * 4 )

