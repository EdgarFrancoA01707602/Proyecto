"""
El programa lo que hace es pedirte ciertos datos
de las unidades que llevas, tus horas de
servicio y sobre como vas con tus pagos para que
al final te diga tus estatus academico, promedio,
datos de tus materias, si conservas o no tu beca y tu prestamo
y si te gustaria vizualizar el como se calculó todo lo anterior
en una imagen
"""

#biblioteca
"""
PIL (Python Imagin Library) son unas librerías de Python destinadas
al procesamiento de imágenes. Gracias a esto podemos manipular imágenes,
crearlas, insertar texto, imágenes y todo ello lanzando un simple script.
Llama la librería para poder trabajar con lo que seria la clase Image.
"""
from PIL import Image

"""
=============== funciones ===============
"""

def function_promedio(unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas y ciclos)
    recibe: unidades matriz de enteros
    Se usa un ciclo que pueda recorrer toda la lista anidada
    y vaya sumando en un acumulador las calificacion de la
    unidad multiplicada por los creditos que vale y otro
    acumulador para ir sumando los creditos, asi al terminar
    el ciclo solo se divide la suma se las calificaciones
    entre el total de creditos
    devuelve: promedio general
    """
    acum_cali=0.0
    acum_credi=0
    pos=0
    for cali in unidades:
        acum_cali=acum_cali+(unidades[pos][0]*unidades[pos][1])
        acum_credi=acum_credi+unidades[pos][1]
        pos=pos+1
    return acum_cali/acum_credi

def function_carga(unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas y ciclos)
    recibe: unidades matriz de enteros
    Saca la carga academica sumando solo los elementos en donde
    se encuentran los creditos de las unidades
    devuelve: la carga academica
    """
    carg=0
    pos=0
    for credi in unidades:
        carg=carg+unidades[pos][1]
        pos=pos+1
    return carg

def function_reprobadas(unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas, ciclos y condicionales)
    recibe: unidades matriz de enteros
    Saca la cantidad de unidades reprobadas haciendo uso de
    un ciclo que recorra los elementos de la matriz donde estan
    almacenadas las calificaciones y al mismo tiempo compara si
    son menores a 70, en caso de que la condición
    se cumpla se suma 1 punto al acumulador
    devuelve: cantidad de unidades reprobadas
    """
    reprob=0
    pos=0
    for cali in unidades:
        if(unidades[pos][0]<70):
            reprob=reprob+1
        pos=pos+1
    return reprob

def function_creditos(unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas, ciclos y condicionales)
    recibe: unidades matriz de enteros
    Saca la cantidad de unidades reprobadas haciendo uso de
    un ciclo que recorra los elementos de la matriz donde estan
    almacenadas las calificaciones y al mismo tiempo compara si
    son menores a 70, en caso de que la condición
    se cumpla se suma la cantidad de creditos que vale esa unidad
    devuelve: la cantidad de creditos reprobados
    """
    credi_r=0
    pos=0
    for credi in unidades:
        if(unidades[pos][0]<70):
            credi_r=credi_r+unidades[pos][1]
        pos=pos+1
    return credi_r

def function_prestamo(pagos, unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas y condicionales)
    recibe: unidades matriz de enteros y pagos texto
    Saca un texto que dice si conservas tu prestamo educativo solo
    si se cumplen las dos condiciones, en caso de que no cumplas las
    dos condicones te rroja un mensaje que te dira que se te retirara
    tu prestamo educativo si no estas al corriente de tus pagos y tienes
    9 o mas creditos reprobados
    """
    if(pagos=="si" and (function_creditos(unidades))<9):
        print("Conservas tu préstamo educativo")
    else:
        print("Se te retirara tu préstamo educativo")

def function_beca(unidades, beca):
    """
    (uso de operadores, funciones, listas, listas anidadas y condicionales)
    recibe: unidades matriz de enteros y beca valor númerico
    Dentro de la condición se manda a llamar otras funciones para comparar
    que el promedio general sea igual o mayor a 85, si se lleva una carga
    academica igual o mayor a 18, si cumpliste con 70 horas de servicio de
    becario y si no tienes niguna unidad reprobada, si todas se cumplen,
    conservas tu beca y con una que no se cumpla se te retira la beca
    """
    if((function_promedio(unidades))>=85 and (function_carga(unidades))>=18 and beca==70 and (function_reprobadas(unidades))==0):
        print("Conservas tu beca")
    else:
        print("Se te retirara la beca")
        
def function_estatus(unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas y condicionales)
    recibe: unidades matriz de enteros
    Dentro de la condición se manda a llamar la funcion para calcular los
    creditos academicos reprobados, esto para saber si la cantidad de creditos
    rebrobados es igual o mayor a 9, en caso de que sea asi, el estatus
    del estudiante sera condicional y en caso de que no se cumpla la condición
    el estatus sera regular
    """
    if ((function_creditos(unidades))>=9):
        print("Tu estatus academico es Condicional")
    else:
        print("Tu estatus academico es Regular")
        
def function_imprimir(unidades):
    """
    (uso de operadores, funciones, listas, listas anidadas y ciclos)
    recibe: unidades matriz de enteros
    Muestra en la pantalla un tipo de tabla que organiza la información
    de cada unidad gracias a un ciclo que va imprimiendo el número de
    unidad, la calificación, los creditos que vale y su ponderación
    """
    print(" ________________________________________________")
    print('{:^10}{:^10}{:^10}{:^10}'.format('| Unidad |',' Calificación ','| Créditos |',' Ponderación |'))
    pos=0
    cont=1
    for cali in unidades:
        print('|{:^8}|{:^14}|{:^10}|{:^13}|'.format(cont,unidades[pos][0],unidades[pos][1],unidades[pos][0]*unidades[pos][1]))
        pos=pos+1
        cont=cont+1
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


"""
=============== parte principal del programa ===============
"""

#te pide la cantidad de unidades que llevaste en el semestre
uni=int(input("¿Cuántas unidades llevaste al semestre? "))

#se hace uso de un ciclo para ir guardando la calificación y los creditos en una lista anidada
cont=1
i=0
unidades=[]
for cali in range(uni):
    unidad=[]
    cali=float(input("Calificación de la unidad {} sobre 100: ".format(cont)))
    unidad.append(cali)
    credi=int(input("Cantidad de creditos que equivale la unidad {}: ".format(cont)))
    unidad.append(credi)
    unidades.append(unidad)
    i==i+1
    cont=cont+1
    
#pregunta la cantidad de horas de servicio que hiciste
beca=int(input("¿Cuántas horas de servicio de becario hiciste? "))

#pregunta sobre si estas al corriente de tus pagos
pagos=str(input("¿Estas al corriente de tus pagos? Escribe 'si' o 'no' "))

#imprime en la pantalla la tabla con los datos de las unidades
function_imprimir(unidades)

#imprime en la pantalla un mensaje con el promedio general
print("Tu promedio general es: ", "%.2f"% function_promedio(unidades))

"""
Se usa una condición que recibe la cantidad de unidades reprobadas
y si esa cantidad es igual o mayor a uno imprime un mensaje con la
cantidad de unidades rebrobadas y si no se cumple solo imprime un
mensaje que dice que aprobaste todas tus materias
"""
if((function_reprobadas(unidades))>=1):
    print("Reprobaste ",aprob," materias")
else:
    print("Aprobaste todas tus materias")

#imprime en la pantalla si se conserva el prestamo o no
function_prestamo(pagos, unidades)

#imprime en la pantalla el estatus del alumno
function_estatus(unidades)

#imprime en la pantalla si se conserva la beca o no
function_beca(unidades, beca)

#pregunta si quiere ver como se realiza el calculo del promedio
mostrar=str(input("¿Quieres ver como se calcula el promedio? "))

"""
Se hace uso de un condicional que compara si la respuesta a la
pregunta de si quiere ver como se calcula el promedio es 'si',
si la respuesta es si aqui es donde se hace uso de la libreria
en donde muestra una imagen en donde se observa como es que se
obtiene el promedio general y en caso de que no quiera ver la
imagen se termina el programa
"""
if(mostrar=="si"):
    try:
        img = Image.open("promedio.jpg")
        img.show()
    except:
        print("No se pudo cargar la imagen")
