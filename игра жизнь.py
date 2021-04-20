import os
import random
import time

def print_mass(a):
    for i in a:
        print(i)

os.system("cls")

n = 10
m = 10
a = []
while True:  
    for i in range(n):
        a.append([random.randrange(2)] * m)
    print_mass(a)
    #[random.randrange(0,3,2) for j in range(m)]  
    time.sleep(0.9)
    #print("==============================")
