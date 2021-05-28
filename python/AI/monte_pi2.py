#-*- coding:utf-8 -*-
from random import random
num=int(input('실험 횟수는 ? '))
cnt=0.0
for i in range(num):
    x=random()
    y=random()
    if x*x + y*y <= 1:
        cnt+=1
print((cnt/num)*4)
