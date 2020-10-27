from Estudiante import Estudiante
from Stack import Stack

miPila=Stack()
#creo el objeto Estudiante1 y lo apilo
miEstudiante1 = Estudiante("2299", "Pedro", "Nanotecnología")
miPila.apilar(miEstudiante1)

#creo el objeto Estudiante2 y lo apilo
miEstudiante2 = Estudiante("3209", "Ezequiel", "Ing. en IA")
miPila.apilar(miEstudiante2)
#miPila.desapilar()

#creo el objeto Estudiante3 y lo apilo
miEstudiante3 = Estudiante("3233", "Isaias", "Ing. en Ciencia de datos")
miPila.apilar(miEstudiante3)

#creo el objeto Estudiante4 y lo apilo
miEstudiante4 = Estudiante("3119", "Emmanuel", "Ing. en TI")
miPila.apilar(miEstudiante4)


print(len(miPila))
#mostrar la pila de estudiantes
for ele in miPila:
    print(ele)

print('Pila después de desapilar')

miPila.desapilar()
for ele in miPila:
    print(ele)