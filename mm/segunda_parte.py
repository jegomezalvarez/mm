#!/usr/bin/env python3

# 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento = 'Data', puesto = 'Analyst'):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self. puesto = puesto
    def presentation(self):
        super().presentation()
        print(f"Trabajo como {self.puesto} en el departamento de {self.departamento}")

nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

# 2
trabajador_1 = Trabajador('Juan',23,'I+D','ingeniero')
trabajador_1.presentation()

# 3
# self.nombre hace referencia a la variable nombre dentro del objeto, su alcance es únicamente el objeto. 
# En el caso de nombre, el alcance será de archivo, se trata de una variable global.

# 4
trabajador_test = Trabajador('Javier',33)
trabajador_test.presentation()

# 5
my_var_list = ['Andrea', '42', 'Ventas', 'Manager']
trabajador_2 = Trabajador(*my_var_list)
trabajador_2.presentation()