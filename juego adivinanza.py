from importlib.metadata import EntryPoint
import random
from tkinter import Entry


numero_secreto = random.randint(0,101)
adivinado = False
cant_intentos = 0
cant_max_intentos = 10

print("bienvenido a la practica 1")

while not adivinado and cant_intentos< cant_max_intentos:
    if not cant_intentos< cant_max_intentos:
     print("no mas intentos")
     break
    numero =  int(input('introduce un numero del 0 al 100: '))
  

    if numero == numero_secreto:
       print("felicidades, adivinaste")   
       adivinado = True
    elif numero < numero_secreto:
        print("el numero es mayor al ingresado")  
    else:
         print("el numero es menor al ingresado")
    cant_max_intentos += 1    
