import os
import random
import time

def print_mass(a):
    os.system("cls")
    for i in a:
        print(i)

def my_count(a, i, j):
    res = 0
    if a[i][j-1] == 1:
        res += 1
    if a[i-1][j] == 1:
        res += 1
    if a[i-1][j-1] == 1:
        res += 1
    if a[i][j+1] == 1:
        res += 1
    if a[i+1][j] == 1:
        res += 1
    if a[i+1][j+1] == 1:
        res += 1
    if a[i+1][j-1] == 1:
        res += 1
    if a[i-1][j+1] == 1:
        res +=1
    return res

os.system("cls")

n = 30
a = []
#while True:  
for i in range(n):
    a.append([random.randrange(2) for i in range(n)]) #генерировали в каждом элементе массива другой массив длинной в m
#print_mass(a)
#[random.randrange(0,3,2) for j in range(m)]
while True:
    temp = []
    temp = a.copy()
    for i in range(1,len(a)-1):
        for j in range(1,len(a[i])-1):
            if (a[i][j] == 1 and my_count(a,i,j) == 2) or my_count(a,i,j) == 3:
                temp[i][j] = 1
            else:
                temp[i][j] = 0
    a = temp.copy()
    print_mass(a)
    time.sleep(2)
#print (my_count(a,i,j))
    #time.sleep(0.9)
#print("==============================")

