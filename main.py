import math
# szam = 2
# while szam < 10000000:
#     szam = math.pow(szam, 2)
#     print(szam)

# szam = 2
# db = 0
# while szam < 10000000:
#     print(szam)
#     db = db + 1
#     szam = szam * 2

# print(f'a 2nek {db} hatványa van 10Mig')

# nev = input('írd be a neved: ')
# print('tessék, itt a neved 10x:')

# db = 0
# while db < 10:
#     print(nev)
#     db += 1

# for x in range(10):
#     print(f'{x} {nev}')

# szam = 2
# for k in range(1, 11):
#     print(int(math.pow(2, k)))

# \\pdc\Diakkaptar\Juhász Zoltán\GYAKORLO FELADATOK

# feladatok 2/2

# szam = int(input('szám: '))
# szoveg = input('szöveg: ')

# for x in range(szam):
#     print(szoveg, end=' ')

# feladatok 2/3
import time
import os

# os.system("cls")
# for x in range(10):
#     print(10 - x)
#     time.sleep(1)
#     os.system("cls")
# print("viszont látásra!")

# nev = "Zolikaaaa"
# os.system("cls")
# for x in range(40):
#     print(x * ' ', end='')
#     print(nev)
#     time.sleep(.2)
#     os.system("cls")

import random

# feladatok 1/31
# for x in range(10):
#     print(random.randint(100, 999), end= ' ')

# feladatok 1/32
# for x in range(10):
#     print(random.randint(0, 250) / 10)

# feladatok 1/34
# for x in range(10):
#     print(random.randint(0, 49) * 2)

# feladatok 1/35
# print(random.randint(20, 40) * 5)

# tsz = random.randint(0, 1000)
# print(f'a szám: {tsz}')
# if tsz > 999: print('4 jegyű')
# elif tsz > 99: print('3 jegyű')
# elif tsz > 9: print('2 jegyű')
# else: print('1 jegyű')

szam1 = random.randint(10, 50)
szam2 = random.randint(10, 50)

eredmeny = int(input(f'{szam1} + {szam2} = '))
if eredmeny == szam1 + szam2: print('így van!')
else: print(f'nope, az eredmény {szam1 + szam2}') 