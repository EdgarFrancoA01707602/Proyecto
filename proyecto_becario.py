from PIL import Image

def function_promedio(cali_lista, credi_lista):
    acum_cali=0.0
    acum_credi=0
    pos=0
    for elem in cali_lista:
        acum_cali=acum_cali+((cali_lista[pos])*(credi_lista[pos]))
        acum_credi=acum_credi+credi_lista[pos]
        pos=pos+1
    return acum_cali/acum_credi

def function_prestamo(pagos, credi_r):
    if(pagos=="si" and credi_r<9):
        print("Conservas tu préstamo educativo")
    else:
        print("Se te retirara tu préstamo educativo")

def function_beca(cali_lista, credi_lista, carg, beca, aprob):
    if((function_promedio(cali_lista, credi_lista))>=85 and carg>=18 and beca==70 and aprob==0):
        print("Conservas tu beca")
    else:
        print("Se te retirara la beca")
        
def function_creditos(credi_r):
    if (credi_r>=9):
        print("Tu estatus academico es Condicional")
    else:
        print("Tu estatus academico es Regular")

aprob=0
carg=0
credi_r=0

cali_lista=[]
credi_lista=[]
suma=0
cont=1


uni=int(input("¿Cuántas unidades llevaste al semestre? "))

for a in range(uni):
    cali=float(input("Calificación de la unidad {} sobre 100: ".format(cont)))
    credi=int(input("Cantidad de creditos que equivale la unidad {}: ".format(cont)))
    if (cali<70):
        aprob=aprob+1
        credi_r=credi_r+credi
    carg=carg+credi
    cali_lista.append(cali)
    credi_lista.append(credi)
    cont=cont+1

beca=int(input("¿Cuántas horas de servicio de becario hiciste? "))
pagos=str(input("¿Estas al corriente de tus pagos? Escribe 'si' o 'no' "))

print("\nTu promedio general es: ", "%.2f"% function_promedio(cali_lista, credi_lista))

if(aprob>=1):
    print("Reprobaste ",aprob," materias")
else:
    print("Aprobaste todas tus materias")

function_prestamo(pagos, credi_r)

function_creditos(credi_r)

function_beca(cali_lista, credi_lista, carg, beca, aprob)

mostrar=str(input("¿Quieres ver como se calcula el promedio? "))

if(mostrar=="si"):
    try:
        img = Image.open("promedio.jpg")
        img.show()
    except:
        print("No se pudo cargar la imagen")
