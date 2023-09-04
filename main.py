# Primer codigo python
# Ejercicio 1:
'''
print("Hola Mundo")
'''
# Ejercicio 2:
''''
Lapicero= 'Hola Mundo'
print(Lapicero)
'''
# Ejercicio 3:
''''
nombre= "escribe tu nombre de usuario: "
mensaje = input (nombre)
print('¡Hola ' +  mensaje  + '!')
'''
# Ejercicio 4
'''
print(((3+2)/(2*5))**2)
'''
# Ejercicio 5
'''
horas= float(input ("digita el numero de horas trabajadas: "))
costo= float(input ("digita el costo de cada hora: "))
print (horas*costo)
'''
# Ejercicio 6  
'''
mensaje = "Ingresa el numero entero positivo: "
n = int(input(mensaje))
Calculo= (n*(n+1))/2
print (Calculo)
'''
# Ejercicio 7
'''
peso= (input ("digita tu peso en kg: "))
estatura = (input ("digita tu estatura en metros: "))
inc= round(float(peso)/float(estatura)**2,2)
print("Tu masa corporal es: ",inc)
'''
# Ejercicio 8
'''
N= float(input ("digita un numero entero: "))
M= float(input ("digita otro numero entero: "))
C=(N//M)
R=(N%M)
print("El cociente de tus numeros es:", C, "y el residuo de tus numeros es:" ,R,)
'''
#Ejercicio 9
'''
C= float(input ("digita la cantidad a invertir: "))
I= float(input ("digita el interes anual: "))
Años= float(input ("digita la cantidad de años: "))
inc= round (C*(I/100+1)**Años,2)
print ("El capital obtenido por la inversion seria:", inc)
'''
# Ejercicio 10
'''
M= float(input ("Ingresa la cantidad de muñecas "))
P= float(input ("Ingresa la cantidad de payasos "))
Payaso= 112
Muñeca= 75
inc= round((Muñeca*M)+(Payaso*P),2)
print("El peso total del paquete sera de: ",inc,"g")
'''
# Ejercicio 11
'''
Ahorros= float(input ("Ingresa la cantidad de dinero depositado"))
Interes = 0.04
Formula=(Ahorros*Interes)
Año1=round((Ahorros-Formula),2)
Formula1=(Año1*Interes)
Año2=round((Año1-Formula1),2)
Formula2=(Año2*Interes)
Año3=round((Año2-Formula2),2)
print("La cantidad de ahorros tras el primer año sera de: ",Año1, 
"La cantidad de ahorros tras el segundo año sera de: ", Año2,
"La cantidad de ahorros tras el tercer año sera de: ", Año3) 
'''
# Ejercicio 12
'''
PanesV= int(input ("Ingresa el número de panes vendidos que no son del día: "))
Pan = 3000
Descuento = 0.4
Formula1=(PanesV*Pan)
Formula2=(Formula1*Descuento)
print("El precio habitual de", PanesV,"panes es de", Formula1, "pero al no ser del dia tienen un descuento del 40%, por lo que pagarias:", Formula2 )
'''
# TEMA CONDICIONALES
# Ejercicio 1
'''
N= int(input ("Digita el numero: "))
Suma=int((N*(N+1)/2))
if Suma > 20 :
  print ("Es un gran numero!", Suma)
else:
  print ("El numero es:",Suma)
'''
'''
# Ejercicio 2 
N= int(input ("Digita el primer numero: "))
M= int(input ("Digita el segundo numero: "))
Division= (N/M)
C=(N//M)
R=(N%M)
if C < 1 :
  print (" La division entre los dos numeros es:",Division,"El cociente de la division es:",C,"El residuo de la operacion es:",R,"El divisor es mayor al dividendo")
elif C > 1:
   print (" La division entre los dos numeros es:",Division,"El cociente de la division es:",C,"El residuo de la operacion es:",R,"El divisor es menor al dividendo")
else:
  print (" La division entre los dos numeros es:",Division,"El cociente de la division es:",C,"El residuo de la operacion es:",R,"El divisor y el dividendo son iguales")
'''
# Ejercicio 3
'''
Invertir=int(input ("Ingresa la cantidad a invertir: "))
Interes= float(input ("Ingresa el interes anual: "))
Años= int(input ("Ingresa el numero de años: "))
Formula= (Invertir*((Interes/100)+1)**Años)
if Formula < 100000:
  print ("El capital es:",formula,"Baja rentabiidad")
elif 100000<Formula<1000000:
  print ("El capital es:",formula,"Rentabilidad baja")
else: 
  print ("El capital es:",formula,"Es una buena inversion")
  '''
# Ejercicio 4
'''
M= float(input ("Ingresa la cantidad de muñecas vendidas: "))
P= float(input ("Ingresa la cantidad de payasos vendidas: "))
Payaso= 112/1000
Muñeca= 75/1000
answer=()
Kg= (Muñeca*M)+(Payaso*P) 
if Kg > 3000:
  answer=input("¿Desea enviar el paquete?")
  if answer == "si":
    print ("Contenedor Enviado")
  elif answer == "no":
     print ("Contenedor No Enviado")
  else:
   print ("Error")
else:
   print ("Contenedor Enviado")
'''

#Ejercicio 5
'''
= float(input (": "))
'''

# Ejercicio 1
'''
n1=int(input ("Ingresa el primer numero: "))
n2=int(input ("Ingresa el segundo numero: "))
def Suma(n1,n2):
  Operacion= n1+n2
  return Operacion
print (Suma(n1,n2)) 
'''
# Ejercicio 2
'''
n1=int(input ("Ingresa el primer numero: "))
n2=int(input ("Ingresa el segundo numero: "))
def Resta(n1,n2):
  Operacion= n1-n2
  return Operacion
print (Resta(n1,n2)) 
'''
# Ejercicio 3
'''
n1=int(input ("Ingresa el primer numero: "))
n2=int(input ("Ingresa el segundo numero: "))
def Multiplicacion(n1,n2):
  Operacion= n1*n2
  return Operacion
print (Multiplicacion(n1,n2)) 
'''
'''
# Ejercicio 4
n1=int(input ("Ingresa el primer numero: "))
n2=int(input ("Ingresa el segundo numero: "))
if n2==0:
    print("No se puede dividir por 0, respete")
else:
    def Division(n1,n2):
      Operacion=float(n1/n2)
      return Operacion
      
print (Division(n1,n2)) 
'''
#Calculadora
'''
n1=int(input ("Ingresa el primer numero: "))
n2=int(input ("Ingresa el segundo numero: "))
Operacion=str(input("¿Que operacion deseas realizar? "))
if Operacion == "suma":
  def Sum(n1,n2):
    x= n1+n2
    return x
  print (Sum(n1,n2)) 
elif Operacion == "resta":
  def Rest(n1,n2):
    x= n1-n2
    return x 
  print (Rest(n1,n2)) 
elif Operacion == "multiplicacion":
  def Producto(n1,n2):
    x= n1*n2
    return x
  print (Producto(n1,n2))
elif Operacion == "division":
  if n2==0:
    print("No se puede dividir por 0, respete")
  else:
    def Division(n1,n2):
      Operacion=float(n1/n2)
      return Operacion
    print (Division(n1,n2)) 
else:
   print("ERROR, porfavor ingresa una operacion valida")
'''

# Ejercicio inversion 
'''
def intereses(inv):
  d=inv
  if (d>0 and d<100000):
    return 2
  elif (d> 10000000 and d<2000000):
    return 5
  else:
    return 7
  
def calbalance(int,inv):
  n=int
  d=inv
  return round(d*(1+(n/100)),2)

def ctaAhorro():
  inversion=float(input("Ingresa el valor de la inversion: "))
  interes=intereses(inversion)
  b1=calbalance(interes,inversion)
  b2=calbalance(interes,b1)
  b3=calbalance(interes,b2)
  print("Balance año 1:" + str(b1) + "Balance año 2" + str(b2) +        "Balance año 3:" + str(b3))

ctaAhorro() 
'''
#AreasFig
'''
def Cuad(lado):
  l=lado
  area= (l*l)
  return area

def Trian(bas,alt):
  b=bas
  h=alt
  area=(b*h/2)
  return area 
  
def Circ(rad):
  r=rad
  area= (3.14169*(r**2))
  return area

def Romb(rad):
  r=rad
  area= (3.14169*(r**2))
  return area

def pent(diagma,diagme):
  y=diagma
  n=diagme
  area= ((y*n)/2)
  return area

def AreasFig():
  Figura=str(input("Escribe a que figura se le debe calcular el area: "))
  
  if (Figura.lower() == "cuadrado"):
    Ladito=float(input("Ingresa el lado del cuadrado: "))
    Cuad(Ladito)
    print("El area del Cuadrado es:", Cuad(Ladito))
    
  elif (Figura.lower() == "triangulo"):
    base=float(input("Ingresa la base del triangulo: "))
    altura=float(input("Ingresa la altura del triangulo: "))
    Trian(base,altura)
    print("El area del triangulo es:", Trian(base,altura))
    
  elif (Figura.lower() == "circulo"):
    radio=float(input("Ingresa el radio de el circulo: "))
    Circ(radio)
    print("El area del circulo es:", Circ(radio))

  elif (Figura.lower() == "pentagono"):
    perimetro=float(input("Ingresa el perímetro del pentagono: "))
    apotema=float(input("Ingresa el apotema del pentagono: "))
    pent(perimetro,apotema)
    print("El area del pentagono es:", pent(perimetro,apotema))

  elif (Figura.lower() == "rombo"):
     diagonalmayor=float(input("Ingresa la diagonal mayor del rombo: "))
     diagonalmenor=float(input("Ingresa la diagonal menor del rombo: "))
     pent(diagonalmayor,diagonalmenor)
     print("El area del rombo es:", pent(diagonalmayor,diagonalmenor))
    
  else:
    print("**Error** Ingresa una figura valida")
    
AreasFig()
'''
#Ejercicio 4
'''
def Mar(m,b):
  y=m
  x=b
  if y.lower()== "nosy":
    Desc=(x * (5/100))
    return Desc
  else:
    return 0


def Pricipal():
  Pestereo=float(input("Ingresa el precio del estereo: "))
  Marca=str(input("Ingresa la marca del estereo: "))
  
  if Pestereo >= 2000000:
    Siniva=(Pestereo*(10/100))
    Desc=(Pestereo-Siniva)
    total=((Desc-Mar(Marca,Pestereo))*(20/100))
    Pago=((Desc-Mar(Marca,Pestereo))+total)
    print("El total que se pagara por el estereo es de:", Pago)
  else:
    Precio= Pestereo
    total=((Precio-Mar(Marca,Pestereo))*(20/100))
    Pago=((Precio-Mar(Marca,Pestereo))+total)
    print("El total que se pagara por el estereo es de:", Pago)
Pricipal()
'''
#TALLER
#1
'''
Año=int(input("Ingresa el año: "))

if Año % 4 and Año % 100 != 0 or Año % 400 == 0:
   print(Año, "es bisisesto")
else:
  print(Año, "no es bisisesto")
'''
  
#2
'''
def pequeño(alt,pes):
  x=alt
  y=pes
  if x<30:
    if y<15:
      return "si"
    else: 
      return "no"
  else:
    return "no"
    
def mediano(alt,pes):
  a=alt
  b=pes
  if a==30 or a<40:
    if b==15 or b<25:
      return "si"
    else: 
      return "no"
  else:
    return "no"

def grande(alt,pes):
  x=alt
  y=pes
  if x==40 or x<=60:
    if y==25 or y<=45:
      return "si"
    else: 
      return "no"
  else:
    return "no"

def Principal():
  Altura=float(input("Ingresa la altura: "))
  Peso=float(input("Ingresa el peso: "))
  if pequeño(Altura,Peso)=="si":
    print("El perro es un mestizo pequeño")
  elif mediano(Altura,Peso)=="si":
    print("El perro es un mestizo mediano")
  elif grande(Altura,Peso)=="si":
    print("El perro es un mestizo grande")
  else:
    print("El perro no cumple con los tamaños establecidos")
    
Principal()
'''
#3





#4
'''
def Niños(edades):
  x=edades
  precio=25000
  if x>=13:
    descuento=(precio*(15/100))
    pago=(precio-descuento)
    return pago
  else:
    descuento=(precio*(8/100))
    pago=(precio-descuento)
    return pago

def Adultos(edades):
  x=edades
  precio=35000
  if x<30:
    descuento=(precio*(11/100))
    pago=(precio-descuento)
    return pago
  else:
    descuento=(precio*(9/100))
    pago=(precio-descuento)
    return pago

def Adulto_Mayor(edades):
  x=edades
  precio=50000
  if x>65:
    descuento=(precio*(40/100))
    pago=(precio-descuento)
    return pago
  else:
    return pago

def Principal():
  Nombre=str(input("Ingresa tu nombre: "))
  Edad=int(input("Ingresa tu edad: "))

  if Edad>=13 and Edad<=17:
    Pago=Niños(Edad)
    print(Nombre, "quedas en el grupo de niños.", "El valor del grupo es de $25000 pero al tener",Edad,"años tienes un descuento y pagas",Pago)
  elif Edad>=18 and Edad<=50:
    Pago=Adultos(Edad)
    print(Nombre, "quedas en el grupo de adultos.", "El valor del grupo es de $35000 pero al tener",Edad,"años tienes un descuento y pagas",Pago)
  elif Edad>=51:
    Pago=Adulto_Mayor(Edad)
    if Pago < 50000:
      print(Nombre, "quedas en el grupo de adulto mayor.", "El valor del grupo es de $50000 pero al tener",Edad ,"años tienes un descuento y pagas",Pago)
    else:
      print(Nombre, "quedas en el grupo de adulto mayor.", "El valor del grupo es de $50000.")
  else:
    print(Nombre,"Tu edad no es apta para las clases de baile")
  
Principal()
'''
#5