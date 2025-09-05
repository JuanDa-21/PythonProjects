calificacion= int(input("Cual es tu calificacion?"))

def verificar_calificacion(calificacion):
    if calificacion >= 70:
        print("Aprobaste")
    if calificacion < 70:
        print("Perdiste")

verificar_calificacion(calificacion)