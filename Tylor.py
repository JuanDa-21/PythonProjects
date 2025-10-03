import math 
def taylor_sin(grados, num_terminos):
    """
    Calcula la aproximación de sin(x) usando la serie de Taylor (Maclaurin).

    :param grados: El ángulo en grados.
    :param num_terminos: Número de términos a sumar (n=0, 1, 2, ..., N-1).
    :return: El valor aproximado de sin(x) y la lista de los términos calculados.
    """
    # 1. Convertir grados a radianes
    x_radianes = grados * (math.pi / 180)
    
    # El valor 'x' utilizado en los cálculos es x_radianes
    x = x_radianes 
    
    # Inicializar la suma de la serie
    suma_total = 0
    
    # Lista para almacenar los términos individuales para verificación
    terminos_calculados = [] 

    print(f"Ángulo en grados: {grados}°")
    print(f"Ángulo en radianes (x): {x:.4f}")
    print("-" * 30)

    # El bucle va de n = 0 hasta num_terminos - 1
    for n in range(num_terminos):
        
        # El exponente es 2n + 1 (impar)
        exponente = 2 * n + 1
        
        # El factorial es (2n + 1)!
        denominador_factorial = math.factorial(exponente)
        
        # El signo es (-1)^n
        signo = (-1) ** n
        
        # Calcular el término actual
        # término = (signo / factorial) * (x ** exponente)
        termino_n = (signo / denominador_factorial) * (x ** exponente)
        
        # Sumar a la serie
        suma_total += termino_n
        
        # Guardar y mostrar el término
        terminos_calculados.append(termino_n)
        print(f"n={n}: Término (x^{exponente}/{exponente}! * {signo}): {termino_n:.6f}")

    print("-" * 30)
    return suma_total, terminos_calculados

# --- Ejemplo de Uso ---

# Basado en tu imagen, vamos a asumir que el ángulo inicial era 45 grados (pi/4) 
# ya que 0.7853 es la aproximación de pi/4. 
# Y vamos a calcular 3 términos (n=0, n=1, n=2).

angulo_grados = 45
cantidad_terminos = 3 

# Ejecutar la función
aproximacion, terminos = taylor_sin(angulo_grados, cantidad_terminos)

print(f"Aproximación de sin({angulo_grados}°): {aproximacion:.6f}")
print(f"Valor real de sin({angulo_grados}°): {math.sin(math.radians(angulo_grados)):.6f}")

# El valor de -0.7853 que calculas parece ser un error en la transcripción
# de tu paso a paso, ya que el término n=0 es:
# término_0 = ((-1)^0 / 1!) * (0.7853^1) = 1 * 0.7853 = 0.7853

# Si usamos el valor de tu imagen (0.7853) para x en el cálculo del primer término (n=0):
x_img = 0.7853
termino_n0_img = ((-1)**0 / math.factorial(1)) * (x_img**1)
print("-" * 30)
print(f"Cálculo del Término para n=0 usando x={x_img}: {termino_n0_img:.4f}")
# El resultado es 0.7853, no -0.7853 como tienes en la última línea.
