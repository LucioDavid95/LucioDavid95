# Proyecto: Gestion de estacionamiento
import sqlite3
import RPi.GPIO as GPIO
from datetime import datetime
import time

#Pines para los pulsadores de estacionamiento
pul1 = 2
pul2 = 3
pul3 = 4

#Pines de los sensores ultrasonicos
TRIG1 = 23
ECHO1 = 24
TRIG2 = 5
ECHO2 = 6


GPIO.setmode(GPIO.BCM)
GPIO.setup(pul1, GPIO.IN)
GPIO.setup(pul2, GPIO.IN)
GPIO.setup(pul3, GPIO.IN)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.output(Trig1,GPIO.LOW)
GPIO.output(Trig2,GPIO.LOW)

idv=0
ban1=0
ban2=0
ban3=0
con=sqlite3.connect("BDestacionamiento.db")
cur=con.cursor()
cur.execute("UPDATE Ubicacion SET estado=0 WHERE idUbicacion='A1'")
cur.execute("UPDATE Ubicacion SET estado=0 WHERE idUbicacion='A2'")
cur.execute("UPDATE Ubicacion SET estado=0 WHERE idUbicacion='A3'")
cur.execute("DELETE FROM Vehiculo")
con.commit()
while True:

    # Estado de los lugares
    if GPIO.input(pul1) == GPIO.HIGH:
        if ban1==0:
            print("Ocupado lugar 1")
            cur.execute("UPDATE Ubicacion SET estado=1 WHERE idUbicacion='A1'")
            idt=input("IDTarjeta:")
            cur.execute("UPDATE Tarjeta SET idUbicacion='A1' WHERE idTarjeta=%i" %int(idt))
            con.commit()
            ban1=1
    else:
        if ban1==1:
            cur.execute("UPDATE Ubicacion SET estado=0 WHERE idUbicacion='A1'")
            con.commit()
            ban1=0
    if GPIO.input(pul2) == GPIO.HIGH:
        if ban2==0:
            print("Ocupado lugar 2")
            cur.execute("UPDATE Ubicacion SET estado=1 WHERE idUbicacion='A2'")
            idt=input("IDTarjeta:")
            cur.execute("UPDATE Tarjeta SET idUbicacion='A2' WHERE idTarjeta=%i" %int(idt))
            con.commit()
            ban2=1
    else:
        if ban2==1:
            cur.execute("UPDATE Ubicacion SET estado=0 WHERE idUbicacion='A2'")
            con.commit()
            ban2=0
    if GPIO.input(pul3) == GPIO.HIGH:
        if ban3==0:
            print("Ocupado lugar 3")
            cur.execute("UPDATE Ubicacion SET estado=1 WHERE idUbicacion='A3'")
            idt=input("IDTarjeta:")
            cur.execute("UPDATE Tarjeta SET idUbicacion='A3' WHERE idTarjeta=%i" %int(idt))
            con.commit()
            ban3=1
    else:
        if ban3==1:
            cur.execute("UPDATE Ubicacion SET estado=0 WHERE idUbicacion='A3'")
            con.commit()
            ban3=0
            
  # Primer sensor (Entrada)
    time.sleep(0.5)
    GPIO.output(Trig1, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trig1, GPIO.LOW)
    while True:
        pulso_inicio1 = time.time()
        if GPIO.input(Echo1) == GPIO.HIGH:
            break
    while True:
        pulso_fin1 = time.time()
        if GPIO.input(Echo1) == GPIO.LOW:
            break
    duracion1 = pulso_fin1 - pulso_inicio1
    distancia1 = (34300 * duracion1) / 2
    if distancia1<=10:
        print("Auto en la entrada")
        chapa=input("Chapa:")
        marca=input("Marca:")
        modelo=input("Modelo:")
        color=input("Color:")
        print("Listo!")
        idv=idv+1
        cur.execute("insert into Vehiculo(idVehiculo,Matricula,Marca,Modelo,Color) values(?,?,?,?,?)", (int(idv),chapa,marca,modelo,color))
        cur.execute("update Tarjeta set idVehiculo=%i where idTarjeta in (select min(idTarjeta) from Tarjeta where entrada is null)" %int(idv))
        cur.execute("update Tarjeta set entrada=DATETIME() where idVehiculo=%i" %int(idv))
        con.commit()
  # Segundo sensor (Salida)
    time.sleep(0.5)
    GPIO.output(Trig2, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(Trig2, GPIO.LOW)
    while True:
        pulso_inicio2 = time.time()
        if GPIO.input(Echo2) == GPIO.HIGH:
            break
    while True:
        pulso_fin2 = time.time()
        if GPIO.input(Echo2) == GPIO.LOW:
            break
    duracion2 = pulso_fin2 - pulso_inicio2
    distancia2 = (34300 * duracion2) / 2
    if distancia2<=10:
        print("Auto en la salida")
        idtsalida=input("ID Tarjeta:")
        cur.execute("update Tarjeta set salida=DATETIME() where idTarjeta=%i" %int(idtsalida))
        for list in cur.execute("select entrada,salida from Tarjeta where idTarjeta=%i" %int(idtsalida)):
            print(list)
        cur.execute("update Tarjeta set idVehiculo=null,idUbicacion=null,entrada=null,salida=null where idTarjeta=%i" %int(idtsalida))
        con.commit()
cur.close()
con.close()
        
        
        
        
        
        
        
