#Clases no privadas, puedo acceder sin get y sin set
"""LLlamar a las funciones de prueba creadas en la clase matematicas.py"""

class  Main:
    #Constructor ¿Que es un constructor y clases de constructores?
    
    def _init_(self):
      self.value= "Curso de Python POO"
    
    #Metodo para llamar las funciones del modulo model 
    
    def operaciones(self,a,b):
        from src.model.Matematicas import Matematicas  
        print(f"Suma:{Matematicas.fun_sumar(a,b)}")
        print(f"Resta:{Matematicas.fun_restar(a,b)}")
        print(f"Multiplicar:{Matematicas.fun_multiplicar(a,b)}")
        print(f"Dividir{Matematicas.fun_division(a,b)}")
#Ejecutar la clase Main
if __name__=="__main__":
  #Crear una instancia de clase Main
  main= Main()
  print("="*50)
  print(f"UNIMINUTO {main.value}")
  print("="*50)
  
  #Solicitar los numeros al usuario 
  try:
    a=float(input("Ingrese el primer numero: "))
    b=float(input("Ingrese el segundo numero: "))
    print("\n"+"-"* 40)
    print(F"Operciones con los numeros{a}y{b}")
    print("-"*40)
    
    #Ejecutar las operaciones 
    main.operaciones(a,b)
  except ValueError:
    print("Error: por favor ingrese numeros vlidos")
    print("\nEjecuntando con valores por ejemplo (10,5)")
    print("-" * 40)
    main.operaciones(10,5)