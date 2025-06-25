import time
import datetime
import pytz

tz_CL = pytz.timezone('America/Santiago')
datetime_CL = datetime.datetime.now(tz_CL)

try:
    edad = int(input("ingresa la edad: "))
except Exception as e:
    with open(f"error.log","a", encoding="utf-8") as log:
        log.write(f"el error es: {datetime_CL.strftime("%d/%m/%Y %H:%M:%S")}, {e} \n")






""" lista = ["pera", "manzana", "naranja"]

file = open("logs/archivo.txt","a", encoding="utf-8")

file.write("Hola\n")

for fruta in lista:
    file.write(fruta + "\n")

file.close() """

""" with open("logs/archivo.txt","r", encoding="utf-8") as a:
    lineas = a.readlines()
    print(lineas) """
