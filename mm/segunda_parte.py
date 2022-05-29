#!/usr/bin/env python3

# 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
 
    def presentation(self):
        print(f"Hola! Soy {self.nombre} y tengo {self.edad} años")

class Trabajador(Persona):
    def __init__(self, nombre, edad, departamento, puesto):
        super().__init__(nombre, edad)
        self.departamento = departamento
        self. puesto = puesto
    def presentation(self):
        super().presentation()
        print(f"Trabajo como {self.puesto} en el departamento de {self.departamento}")



nombre = 'Alberto'
persona_1 = Persona(nombre, 20)
persona_1.presentation()

#2
trabajador_1 = Trabajador('Juan',23,'I+D','ingeniero')
trabajador_1.presentation()