#15
import os
os.system('cls')



def jameAddad():
    numbers = int(input("Type Count of Your Numbers : "))
    total = 0
    for i in range(numbers):
        a = int(input(f' Num {i + 1} = '))
        total+= a
    print(f'Sum od Your Numbers is : {total}')    


jameAddad()
