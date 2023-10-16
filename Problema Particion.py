import random 

def generenumeros(totalNumeros, maxNumeros):
  numeros = []
  for i in range (0,totalNumeros):
    numeros.append(random.randint(0,maxNumeros))
  print("numeros a trabajar: ",numeros)
  return numeros

#el ADN es de 12 debido al total de numeros a trabajar (0y1)
def genereADN(totalNumeros):
  ADN = []
  for i in range(0,totalNumeros):
    a = random.randint(0,100)
    if(a>50):
      ADN.append(1)
    else:
      ADN.append(0)
  return ADN

#Calcula el error de cada individuo
def calculaError(totalNumeros,numeros, adn):
  TotalA = 0
  TotalB = 0
  Error = 0
  for i in range(0,totalNumeros):
    if adn[i] == 0:
      TotalA = TotalA + numeros[i]
    else:
      TotalB = TotalB + numeros[i]
  Error = abs(TotalA-TotalB)
  return Error

def imprime(totalNumeros,ErrorPoblacion,poblIt):
    #Tabla de evaluación de la Población
    acumula=0
    print ("\n",'Tabla Iteración:',"\n")
    print ("\t        Individuos \t Fitness \t Probabilidad \t Acumulada")
    for i in range(0, totalNumeros):
        probab=1/ErrorPoblacion[i]
        acumula+=probab
        print(" ",[i+1],"\t\t", poblIt[i],"\t ",ErrorPoblacion[i],"\t\t    ","{0:.3f}".format(probab),"\t  ","{0:.3f}".format(acumula))


def generehijos(totalNumeros, padres):
    hijos = []
    num_padres = len(padres)
    num_hijos = len(padres) * 2  # Quieres tener el mismo número de hijos que de padres

    for _ in range(num_hijos):
        # Elige dos padres al azar
        padre1, padre2 = random.sample(padres, 2)

        # Elige una semilla al azar
        semilla = random.randint(0, totalNumeros - 1)

        # Genera hijos combinando los padres en la semilla
        hijo1 = padre1[0:semilla] + padre2[semilla:totalNumeros]
        hijo2 = padre2[0:semilla] + padre1[semilla:totalNumeros]

        # Agrega los hijos a la lista de hijos
        hijos.append(hijo1)
        hijos.append(hijo2)

    return hijos

def generemutacion(totalNumeros,hijos):
  for i in range(0,2):
    individuo = random.randint(0,totalNumeros-1)
    #print("individuo mutacion: ",individuo)
    for j in range(0,4):
      cromosoma = random.randint(0,totalNumeros-1)
      #print("cromosoma mutacion: ",cromosoma)
      if hijos[cromosoma][individuo] == 0:
        hijos[cromosoma][individuo] = 1
      else:
        hijos[cromosoma][individuo] = 0
  return hijos

totalNumeros = int(input("Ingrese el total de numeros a trabajar: "))
maxNumeros = int(input("Ingrese el maximo valor de los numeros: "))
numeros = generenumeros(totalNumeros,maxNumeros)

#Variables de uso general del algortimo
Maxiteraciones = int(input("Ingrese el numero maximo de iteraciones: "))
iteraciones = 1
MinError = int(input("Ingrese el error minimo: "))
termina = True

#Genera la primera población EL ORIGEN
poblacion = []
for i in range(0,totalNumeros):
  poblacion.append(genereADN(totalNumeros))
print("generacion",iteraciones,": ",poblacion)

#Ciclo principal del algoritmo genético
while(termina):

  #Calculo el Error para los 10 individuos de la población
  ErrorPoblacion = []
  for i in range(0,totalNumeros):
    ErrorPoblacion.append(calculaError(totalNumeros,numeros,poblacion[i]))
  print("Errores población: ",ErrorPoblacion)

  #Buscar si el error es menor-igual con el error minimo
  for i in range(0,totalNumeros):
    if ErrorPoblacion[i] <= MinError:
      termina = False
      print("solucion:",poblacion[i])
  
  #Verifica que no se haya el numero máximo de iteraciones
  iteraciones += 1
  if iteraciones == Maxiteraciones:
    termina = False

  #Validar si no termina, para calcular la nueva generación
  if(termina == True):
    Mejorespadres = []

    #Selección de los cuatro mejores padres
    for i in range (0,4):
      posmenor = ErrorPoblacion.index(min(ErrorPoblacion))
      print(posmenor)
      Mejorespadres.append(poblacion[posmenor])
      ErrorPoblacion.pop(posmenor)
      poblacion.pop(posmenor)

    print("mejores padres: ",Mejorespadres)
    
    #Realiza la mezcla de los padres para sacar la nueva generación
    #1-2 1-3 1-4 2-3 2-4 3-4 Cada pareja arroja 2 hijos (12 Total)
    poblacion = generehijos(totalNumeros,Mejorespadres)

    #Realiza la mutación en 2 de los 12 nuevos individuos
    #Modifica 4 de los 12 valores en los 2 individuos mutados
    poblacion = generemutacion(totalNumeros,poblacion)
    print("generacion",iteraciones,": ",poblacion)


