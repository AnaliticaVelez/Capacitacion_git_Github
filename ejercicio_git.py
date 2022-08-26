from gettext import npgettext
from multiprocessing.spawn import import_main_path
import pandas as pd
import numpy as np

print('Somos el equipo de analtica mercadeo Cueros Vélez')


def rombo(n):

    result1=[" "*(n-i)+"$"*(i+i-1) for i in range(1,n+1)]
    return "\n".join(result1+list(reversed(result1[:-1])))
 
numero=int(input("indica un numero: "))
print(rombo(numero))´

print("Desarollado por Simon")