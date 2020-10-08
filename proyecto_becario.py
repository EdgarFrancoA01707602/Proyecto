from PIL import Image

def function_promedio(unidades):
    acum_cali=0.0
    acum_credi=0
    pos=0
    for cali in unidades:
        acum_cali=acum_cali+(unidades[pos][0]*unidades[pos][1])
        acum_credi=acum_credi+unidades[pos][1]
        pos=pos+1
    return acum_cali/acum_credi

def function_carga(unidades):
    carg=0
    pos=0
    for credi in unidades:
        carg=carg+unidades[pos][1]
        pos=pos+1
    return carg

def function_reprobadas(unidades):
    reprob=0
    pos=0
    for cali in unidades:
        if(unidades[pos][0]<70):
            reprob=reprob+1
        pos=pos+1
    return reprob

def function_creditos(unidades):
    credi_r=0
    pos=0
    for credi in unidades:
        if(unidades[pos][0]<70):
            credi_r=credi_r+unidades[pos][1]
        pos=pos+1
    return credi_r

def function_prestamo(pagos, unidades):
    if(pagos=="si" and (function_creditos(unidades))<9):
        print("Conservas tu préstamo educativo")
    else:
        print("Se te retirara tu préstamo educativo")

def function_beca(unidades, beca):
    if((function_promedio(unidades))>=85 and (function_carga(unidades))>=18 and beca==70 and (function_reprobadas(unidades))==0):
        print("Conservas tu beca")
    else:
        print("Se te retirara la beca")
        
def function_estatus(unidades):
    if ((function_creditos(unidades))>=9):
        print("Tu estatus academico es Condicional")
    else:
        print("Tu estatus academico es Regular")
        
def function_imprimir(unidades):
    print(" ________________________________________________")
    print('{:^10}{:^10}{:^10}{:^10}'.format('| Unidad |',' Calificación ','| Créditos |',' Ponderación |'))
    acum_cali=0.0
    acum_credi=0
    pos=0
    cont=1
    for cali in unidades:
        acum_cali=acum_cali+(unidades[pos][0]*unidades[pos][1])
        acum_credi=acum_credi+unidades[pos][1]
        print('|{:^8}|{:^14}|{:^10}|{:^13}|'.format(cont,unidades[pos][0],unidades[pos][1],unidades[pos][0]*unidades[pos][1]))
        pos=pos+1
        cont=cont+1
    print(" ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")


uni=int(input("¿Cuántas unidades llevaste al semestre? "))

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
    
    
beca=int(input("¿Cuántas horas de servicio de becario hiciste? "))
pagos=str(input("¿Estas al corriente de tus pagos? Escribe 'si' o 'no' "))

function_imprimir(unidades)

print("Tu promedio general es: ", "%.2f"% function_promedio(unidades))

if((function_reprobadas(unidades))>=1):
    print("Reprobaste ",aprob," materias")
else:
    print("Aprobaste todas tus materias")

function_prestamo(pagos, unidades)

function_estatus(unidades)

function_beca(unidades, beca)

mostrar=str(input("¿Quieres ver como se calcula el promedio? "))

if(mostrar=="si"):
    try:
        img = Image.open("promedio.jpg")
        img.show()
    except:
        print("No se pudo cargar la imagen")
