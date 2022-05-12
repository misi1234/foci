from enum import Flag
import random


lista_1 = []
lista_2 = []

def atlag():
    atlag = (sum(lista_1) + sum(lista_2)) / 10
    return atlag
#1
for i in range(5):
    lista_1.append(random.randint(1,5))

for i in range(5):
    lista_2.append(random.randint(1,5))

print('1. feladat - Eredmények')

print(f"1. forduló: {lista_1[0]}:{lista_2[0]}")
print(f"2. forduló: {lista_1[1]}:{lista_2[1]}")
print(f"3. forduló: {lista_1[2]}:{lista_2[2]}")
print(f"4. forduló: {lista_1[3]}:{lista_2[3]}")

#2

avg = atlag()
print("\n2. feladat")
print(f"A meccseken átlagosan {avg} gól született!")

#3
print("\n3. feladat")
hazai = 0
dontetlen = False

for i in range(len(lista_1)):
    if lista_1[i] > lista_2[i]:
        hazai += 1

    if hazai > 2:
        print("A hazai csapat győzött többször!")
    else:
        print("A vendég csapat győzött többször!")

    if lista_1[i] == lista_2[i]:
        dontetlen = True

#4

if dontetlen == True:
    print("Döntetlen: igen")
elif dontetlen == False:
    print("Döntetlen: nem")


