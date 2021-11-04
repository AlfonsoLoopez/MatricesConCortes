from random import sample

##Variables
maximo = 0
tamaño = 0
gaps = 5
texto=""
cadena =""

##Obteniendo la cantidad de cadenas 
print("Ingrese el numero de cadenas que desea: ")
Columnas = int(input())

##Creacion de matrices
Matriz = []
MatrizM1 = []
MatrizM2 = []
MatrizHijo = []
RandomM1 = []
RandomM2 = []

##Agregando cadenas de caracteres en matriz de elementos
for i in range(Columnas):
    print("Ingrese la ",i+1, " cadena de elementos:")
    texto=input()
    Matriz.append(list(texto))

##Obteniendo el valor maximo de caracteres y minimo
minimo = len(Matriz[0])
for i in range(Columnas):
    tamaño = len(Matriz[i])
    if maximo<=tamaño:
        maximo = tamaño
        cadena = Matriz[i]
    if tamaño<=minimo:
        minimo = tamaño

##Añadiendo los gaps adicionales
maximo = maximo + gaps

##Creando las matriz M1 y M2
for i in range(Columnas):
    MatrizM1.append([])
    MatrizM2.append([])
    for j in range(maximo):
        if(j<len(Matriz[i])):
            MatrizM1[i].append(Matriz[i][j])
            MatrizM2[i].append(Matriz[i][j])
        else:
            MatrizM1[i].append("-")
            MatrizM2[i].append("-")

##Generando las posiciones random de gaps
for i in range(Columnas):
    RandomM1.append([])
    RandomM2.append([])
    L1 = sorted(sample(range(0,maximo-gaps),gaps))
    L2 = sorted(sample(range(0,maximo-gaps),gaps))
    for j in range(5):
        RandomM1[i].append(L1[j])
        RandomM2[i].append(L2[j])

##Transformando la lista de posiciones a posiciones enteras
for i in range(Columnas):
    for j in range(len(RandomM1[i])):
        RandomM1[i][j] = int(RandomM1[i][j])
        RandomM2[i][j] = int(RandomM2[i][j])

##Insertando los gaps aleatorios en las matrices
for i in range(Columnas):
    j = len(RandomM1[i])-1
    while(j>=0):
        ##Matriz M1
        k1=len(MatrizM1[i])-1
        pos1 = RandomM1[i][j]
        while(pos1<k1):
            MatrizM1[i][k1] = MatrizM1[i][k1-1]
            k1=k1-1
        MatrizM1[i][k1]="-"
        
        ##Matriz M2
        k2=len(MatrizM2[i])-1
        pos2 = RandomM2[i][j]
        while(pos2<k2):
            MatrizM2[i][k2] = MatrizM2[i][k2-1]
            k2=k2-1
        MatrizM2[i][k2]="-"
        j=j-1

##pidiendo el numero de cortes
cortes = 0
while(cortes<2 or cortes>minimo):
    print("\nIngrese el numero de cortes: [2,",minimo,"]")
    cortes=int(input())
    if(cortes>1 and cortes<=minimo):
        print("Cortes dentro de rango!!")
    else:
        print("Cortes fuera de rango!!")
        print("Intente de nuevo.")

##Matriz de cortes
numlet = []
resultado = 0
modulo = 0
for i in range(len(Matriz)):
    numlet.append([])
    resultado =int(len(Matriz[i]) / cortes)
    modulo = len(Matriz[i]) % cortes
    numlet[i].append(resultado)
    numlet[i].append(modulo)

##Declarando variables necesarias para matriz hijo
indicador1 = 0
indicador2 = 0
letras1 = 0
letras2 = 0
posicion = 0
##Creando la matriz hijo
for i in range(Columnas):
    print()
    MatrizHijo.append([])
    j = 0
    turno = True
    while((j+1)<cortes):
        for k in range(cortes):
            if(k+1<cortes):
                letras2 =int(numlet[i][0])
            else:
                letras2 = int(numlet[i][0]) + int(numlet[i][1])
            if(turno):
                while(letras1<letras2):
                    posicion = int(indicador1)
                    MatrizHijo[i].append(MatrizM1[i][posicion])
                    if(MatrizM1[i][posicion]!="-"):
                        letras1 = letras1 + 1
                    indicador1 = indicador1 +1
                    j = j + 1
            
                letras1 = 0
                while(letras1<letras2):
                    posicion = int(indicador2)
                    if(MatrizM2[i][posicion]!="-"):
                        letras1 = letras1 + 1
                    indicador2 = indicador2 + 1

                letras1 = 0
                MatrizHijo[i].append("|")
                turno = not turno
                print("Cadena: ",i+1,", numero de corte: ",k+1,", numero de elementos en el corte de la Matriz M1: ", letras2)
            else:
                while(letras1<letras2):
                    posicion = int(indicador2)
                    MatrizHijo[i].append(MatrizM2[i][posicion])
                    if(MatrizM2[i][posicion]!="-"):
                        letras1 = letras1 +1
                    j = j + 1
                    indicador2 = indicador2 + 1

                letras1 = 0
                while(letras1<letras2):
                    posicion = int(indicador1)
                    if(MatrizM1[i][posicion]!="-"):
                        letras1 = letras1 + 1
                    indicador1 = indicador1 + 1
                letras1 = 0
                MatrizHijo[i].append("|")
                turno = not turno
                print("Cadena: ",i+1,", numero de corte: ",k+1,", numero de elementos en el corte de la Matriz M2: ", letras2)
            
        indicador1 = 0
        indicador2 = 0
            

##imprimiendo matriz de elementos sin gaps
print("\nMatriz:")
for i in range(Columnas):
    print(Matriz[i])

##Imprimiendo posiciones random de la matriz M1
print("\nPosiciones M1:")
for i in range(Columnas):
    print(RandomM1[i])

##Imprimiendo posiciones random de la matriz M2
print("\nPosiciones M2:")
for i in range(Columnas):
    print(RandomM2[i])

##Imprimiendo matriz M1
print("\nMatriz M1:")
for i in range(Columnas):
    print("[", end=" ")
    for j in range(len(MatrizM1[i])):
        print(MatrizM1[i][j], end=" ")
    print("]")

##Imprimiendo matriz M2
print("\nMatriz M2:")
for i in range(Columnas):
    print("[", end=" ")
    for j in range(len(MatrizM2[i])):
        print(MatrizM2[i][j], end=" ")
    print("]")

##Obteniendo la longitud mas larga de la Matriz Hijo
maximo = 0
for i in range(Columnas):
        tamaño = len(MatrizHijo[i])
        if(maximo<=tamaño):
            maximo = tamaño
##Haciendo la matriz hijo cuadrada
for i in range(Columnas):
    for j in range(maximo):
        if(j>=len(MatrizHijo[i])):
            MatrizHijo[i].append("-")

##Imprimiendo matriz hijo
print("\nMatriz hijo:")
for i in range(Columnas):
    print("[", end=" ")
    for j in range(len(MatrizHijo[i])):
        print(MatrizHijo[i][j], end=" ")
    print("]")