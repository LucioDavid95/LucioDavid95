# Proyecto: Gestion de estacionamiento
import RPi.GPIO as GPIO
import time

Lugar1 = 2
Lugar2 = 3
Lugar3 = 4
TRIG1 = 23
ECHO1 = 24
TRIG2 = 5
ECHO2 = 6


GPIO.setmode(GPIO.BCM)
GPIO.setup(Lugar1, GPIO.IN)
GPIO.setup(Lugar2, GPIO.IN)
GPIO.setup(Lugar3, GPIO.IN)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)


while True:

    # Sensor 1------------------------------------------------------
    GPIO.output(TRIG1, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG1, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG1, GPIO.LOW)

    while True:
        pulso_inicio1 = time.time()
        if GPIO.input(ECHO1) == GPIO.HIGH:
            break

    while True:
        pulso_fin1 = time.time()
        if GPIO.input(ECHO1) == GPIO.LOW:
            break

    duracion1 = pulso_fin1 - pulso_inicio1

    distancia1 = (34300 * duracion1) / 2

    print("Distancia: %.2f cm" % distancia1)

    # Sensor 2-----------------------------------------------------
    GPIO.output(TRIG2, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG2, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG2, GPIO.LOW)

    while True:
        pulso_inicio2 = time.time()
        if GPIO.input(ECHO2) == GPIO.HIGH:
            break

    while True:
        pulso_fin2 = time.time()
        if GPIO.input(ECHO2) == GPIO.LOW:
            break

    duracion2 = pulso_fin2 - pulso_inicio2

    distancia2 = (34300 * duracion2) / 2

    print("Distancia: %.2f cm" % distancia2)

    # Estado del lugar de estacionamiento
    if GPIO.input(Lugar1) == GPIO.HIGH:
        print("Ocupado lugar 1")
    if GPIO.input(Lugar1) == GPIO.HIGH:
        print("Ocupado lugar 2")
    if GPIO.input(Lugar1) == GPIO.HIGH:
        print("Ocupado lugar 3")
