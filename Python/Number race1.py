'''
Script description:
Cree un juego en Python que permita a un solo
jugador lanzar dos dados en varias oportunidades
consecutivas, y finalice el juego cuando obtenga un par de unos [D1:1-D2:2]

'''
import os 
from random import randint, uniform, random

os.system("clear")
print(":::JUEGO CARRERA NUMERICA:::")

status=True
while status: #while status == true
    key=input("Preciona una tecla para jugar :v")
    dice1=randint(1,6)
    dice2=randint(1,6)
    print("dice1, ", dice1)
    print("dice2, ", dice2)
    if dice1==1 and dice2==1:
        status=False
        print("Sacaste par")
        key=input("EL JUEGO TERMINO, PRECIONA CUALQUIER TECLA")
