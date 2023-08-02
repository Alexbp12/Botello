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