import random

user=[]

nombre=(input("Hola, ingresa el nombre de la organización: "))
user.append(nombre)

#contraseñas aleatorias
minus = "abcdefghijklmnopqrstuvwxyz"
mayus=minus.upper()
numeros="1234567890"

base=minus+mayus+numeros
longitud= 6

muestra = random.sample(base,longitud)
password = "".join(muestra)

#print(password)
cuentas=("Usuario: ", nombre,"contraseña", password)
print("Bienvenido/a, tu cuenta es:", cuentas)



#pienso en armar el ciclo

def cuentas_automaticas():
    nueva_cuenta = nombre
