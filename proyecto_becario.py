def function_promedio(suma,uni):
    return suma/uni

def function_prestamo(pagos, estat):
    if(pagos=="si" and estat=="si"):
        print("Conservas tu préstamo educativo")
    else:
        print("Se te retirara tu préstamo educativo")

def function_beca(suma, uni, carg, beca, aprob):
    if((function_promedio(suma,uni))>=85 and carg>=18 and beca==70 and aprob==0):
        print("Conservas tu beca")
    else:
        print("Se te retirara la beca")

uni=int(input("¿Cuántas unidades llevaste? "))
cont=1
suma=0
aprob=0

while (cont<=uni):
    cali=float(input("Calificación de la unidad {} sobre 100: ".format(cont)))
    if (cali<70):
        aprob=aprob+1
    suma=suma+cali
    cont=cont+1

carg=int(input("¿Cuánta carga académica llevaste (créditos)? "))
beca=int(input("¿Cuántas horas de servicio de becario hiciste? "))
estat=str(input("¿Tu estatus academico es regular? Escribe 'si' o 'no' "))
pagos=str(input("¿Estas al corriente de tus pagos? Escribe 'si' o 'no' "))

print("\nTu promedio general es: ", function_promedio(suma,uni))

if(aprob>=1):
    print("Reprobaste ",aprob," materias")
else:
    print("Aprobaste todas tus materias")

function_prestamo(pagos, estat)

function_beca(suma, uni, carg, beca, aprob)
