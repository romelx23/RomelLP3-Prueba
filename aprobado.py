#Ejercicio que determine si un estudiante esta aprobado  o no.
#AUTOR:Romel

def determinarAprobado(promedio):
    if promedio>=11:
        resultado="Aprobado"
    else: 
        resultado="desaprobado"
    return resultado
promedio = int(input("Promedio:"))
print(determinarAprobado(promedio))
