## Proyecto: Gestion de estacionamiento
##Integrantes:
##Lucio Aceval 3787999
##Jun Galeano 4328172
##Gabriel Mercado
##Theo Clement Torres Ferraro 4572374
##Francisco González 4304266

import RPi.GPIO as GPIO
import time

Lugar1 = 2 #Variable de entrada del primer lugar de estacionamiento de vehiculo
Lugar2 = 3 #Variable de entrada del segundo lugar de estacionamiento de vehiculo
Lugar3 = 4 #Variable de entrada del tercer lugar de estacionamiento de vehiculo
Led1 = 17 #Led que indica el estado del lugar 1
Led2 = 27 #Led que indica el estado del lugar 2
Led3 = 22 #Led que indica el estado del lugar 3
TRIG1 = 23 #Variable que contiene el GPIO al cual conectamos la señal TRIG del sensor 1
ECHO1 = 24 #Variable que contiene el GPIO al cual conectamos la señal ECHO del sensor 1
TRIG2 = 5 #Variable que contiene el GPIO al cual conectamos la señal TRIG del sensor 2
ECHO2 = 6 #Variable que contiene el GPIO al cual conectamos la señal ECHO del sensor 2


GPIO.setmode(GPIO.BCM)     #Establecemos el modo según el cual nos refiriremos a los GPIO de nuestra RPi            
GPIO.setup(Lugar1, GPIO.IN)
GPIO.setup(Lugar2, GPIO.IN)
GPIO.setup(Lugar3, GPIO.IN)
GPIO.setup(Led1, GPIO.OUT)
GPIO.setup(Led2, GPIO.OUT)
GPIO.setup(Led3, GPIO.OUT)
GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN) 
GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN) 


#Contenemos el código principal en un aestructura try para limpiar los GPIO al terminar o presentarse un error
try:
    #Implementamos un loop infinito
    while True:
	#Detectores de estacionamiento
	if GPIO.input(Lugar1) == GPIO.HIGH:
		GPIO.output(Led1,GPIO.HIGH)
	else
		GPIO.output(Led1,GPIO.LOW)
	
	
	if GPIO.input(Lugar2) == GPIO.HIGH:
		GPIO.output(Led2,GPIO.HIGH)
	else
		GPIO.output(Led2,GPIO.LOW)


	if GPIO.input(Lugar3) == GPIO.HIGH:
		GPIO.output(Led3,GPIO.HIGH)
	else
		GPIO.output(Led3,GPIO.LOW)
	
	#Sensor 1------------------------------------------------------
        # Ponemos en bajo el pin TRIG y después esperamos 0.5 seg para que el transductor se estabilice
        GPIO.output(TRIG1, GPIO.LOW)
        time.sleep(0.5)

        #Ponemos en alto el pin TRIG esperamos 10 uS antes de ponerlo en bajo
        GPIO.output(TRIG1, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG1, GPIO.LOW)
	
	while True:
            pulso_inicio1 = time.time()
            if GPIO.input(ECHO1) == GPIO.HIGH:
                break

        # El pin ECHO se mantendrá en HIGH hasta recibir el eco rebotado por el obstáculo. 
        # En ese momento el sensor pondrá el pin ECHO en bajo.
	# Prodedemos a detectar dicho evento para terminar la medición del tiempo
        
        while True:
            pulso_fin1 = time.time()
            if GPIO.input(ECHO1) == GPIO.LOW:
                break

        # Tiempo medido en segundos
        duracion1 = pulso_fin1 - pulso_inicio1

        #Obtenemos la distancia considerando que la señal recorre dos veces la distancia a medir y que la velocidad del sonido es 343m/s
        distancia1 = (34300 * duracion1) / 2

        # Imprimimos resultado
        print( "Distancia: %.2f cm" % distancia1)
	
	#Sensor 2-----------------------------------------------------
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

        print( "Distancia: %.2f cm" % distancia2)

finally:
    GPIO.cleanup()
