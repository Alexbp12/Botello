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
