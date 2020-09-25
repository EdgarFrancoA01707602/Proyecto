# Proyecto Becario

### Contexto
Hay un alumno el cual cuenta con un apoyo económico que consiste en una beca de tipo socioeconómica junto con un préstamo educativo para realizar sus estudios superiores en el Tecnológico de Monterrey.

Para conservar la beca te piden ciertos requisitos, los cuales son:
  1.	Obtener un promedio final en cada semestre igual o mayor a 85/100.
  2.	Cursar lo correspondiente a la carga académica completa (18 créditos).
  3.	Realizar un servicio de becario satisfactorio (70 horas al semestre).
  4.	Aprobar todas las materias o unidades de formación con créditos.

Y para conservar su préstamo educativo debe cumplir con los siguientes requisitos:
  1.	Contar con estatus regular académicamente.
  2.	Mantenerte al corriente en los pagos efectuados al Tecnológico de Monterrey.

Al final de cada semestre el alumno quiere saber si sigue conservando su beca o no.

### Datos de entrada
Cuantas unidades llevaste al semestre

Calificación de cada unidad

Cantidad de creditos que equivale cada unidad

Horas de servicio de becario realizadas

Si se esta al corriente de los pagos o no

Si desea ver como se calcula el promedio


### Datos de salida
Promedio general

Cantidad de materias reprobadas

Si se conserva o no el prestamo educativo

Si el estatus del alumno es Regular o Condicional

Si se retira la beca o se conserva

 
### Pseudocódigo
Aqui se presenta el pseudocódigo que servira como base para el desarrollo del proyecto

INICIO

uni, carg, beca, suma=0, cont=1: Entero

promedio, cali: Flotante

aprob, estat, pagos: Cadena/string

ESCRIBA “¿Cuántas unidades llevaste?”

LEER uni

WHILE  cont  <=  uni

   ESCRIBA “Calificación de la unidad ”+cont
    
   LEER cali
    
   suma=suma+cali
    
   cont++
    
END WHILE

promedio  =  suma/uni

ESCRIBA “¿Cuánta carga académica llevaste (créditos)? ”

LEER carg

ESCRIBA “¿Cuántas horas de servicio de becario hiciste? ”

LEER beca

ESCRIBA “Escribe “Si” si aprobaste todas tus unidades o “No” si no aprobaste todas tus unidades ”

LEER aprob

ESCRIBA “¿Tu estatus académico es regular? Escribe “Si” o “No” ”

LEER estat

ESCRIBA “¿Estas al corriente de tus pagos? Escribe “Si” o “No” ”

LEER pagos

IF pagos == “Si”  AND  estat == “Si”

   MOSTRAR “Conservas tu préstamo educativo”
    
ELSE

   MOSTRAR “Se te retirara tu préstamo educativo”
    
END IF

IF promedio >= 85  AND  carg >= 18  AND  beca == 70  AND  aprob == “Si”

   MOSTRAR “Conservaras tu beca”
    
ELSE

   MOSTRAR “Se te retirara la beca”
    
END IF

FIN

### proyecto_becario
Todo lo anterior se esta haciendo en el archivo:

    python proyecto_becario.py
    
Se puede realizar una consulta o descargar para abrirlo en Thonny o dar clic en el boton de play.

Es importante mecionar que el archivo de imagen debe de estar siempre en el mismo directorio que el archivo del código.
