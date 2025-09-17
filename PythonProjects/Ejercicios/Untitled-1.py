import math


angulo_grados = 45
n_terminos = 100

x_radianes = math.radians(angulo_grados)


seno_aproximado = 0


for i in range(n_terminos):
 
    termino = ((-1)**i) * (x_radianes**(2 * i + 1)) / math.factorial(2 * i + 1)
    
    
    seno_aproximado += termino

print(f"El seno de {angulo_grados} grados es aproximadamente: {seno_aproximado}")

