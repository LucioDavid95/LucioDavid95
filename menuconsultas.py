import time
import datetime
import sqlite3
while True:
  print("\n\nMENU DEL GESTOR DE ESTACIONAMIENTO")
  print("Elegir una opcion:")
  print("1-Mostrar lista de usuarios actuales del estacionamiento")
  print("2-Mostrar lugares libres")
  print("3-Ver caracteristicas de un vehiculo por su chapa")
  print("4-Mostrar hora de entrada de un vehiculo por su chapa")
  print("\nMENU DEL USUARIO DEL ESTACIONAMIENTO")
  print("5-Mostrar ubicacion y hora de entrada de un vehiculo por ID de tarjeta")
  print("0-Salir")
  res=input("\nNumero de la opcion:")
  
  con.sqlite3.connect("BDestacionamiento.db")
  cur.con.cursor()
  if res=="1":
    for list1 in cur.execute("select entrada,idUbicacion,Matricula,Marca,Modelo,Color from Tarjeta join Vehiculo on Tarjeta.idVehiculo=Vehiculo.idVehiculo where salida is null")
        print(list1)
  elif res=="2":
    for list2 in cur.execute("select idUbicacion from Ubicacion where estado=0"):
      print(list2[0])
  elif res=="3":
    chapa=str(input("\nEscriba la chapa del vehiculo (ej. 'ABC123'): "))
    chapa=(chapa,)
    for list3 in cur.execute("select * from Vehiculo where Matricula like ?", chapa):
      print(list3)
  elif res=="4":
    chapa=str(input("\nEscriba la chapa del vehiculo (ej. 'ABC123'): "))
    chapa=(chapa,)
    for entrada in cur.execute("select Matricula,entrada from Vehiculo join Tarjeta on Vehiculo.idVehiculo=Tarjeta.idTarjeta where Matricula like ?", chapa):
      print(entrada)
  elif res=="5":
    id=input("ID:")
    for list5 in cur.execute("select idUbicacion and entrada from Tarjeta where idTarjeta=%i" %int(id))
      print(list5)
  elif res=="0":
    break
  cur.close()
  con.close()
