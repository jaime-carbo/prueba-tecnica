from typing import List
from random import randint

class Persona:
    def __init__(self, sexo: str, edad: int):
        self.sexo = sexo
        self.edad = edad

def leer_personas() -> List[Persona]:
    vector = []
    for i in range(50):
        sexo = "femenina" if randint(0,1) == 0 else "masculina"
        edad = randint(0,100)
        vector.append(Persona(sexo, edad))
    return vector

def clasificar_personas(vector_personas: List[Persona]):
    mayores_edad, menores_edad, masculinas, femeninas = [], [], [], []
    for persona in vector_personas:
        if persona.edad >= 18:
            mayores_edad.append(persona)
        else:
            menores_edad.append(persona)
        if persona.sexo == "masculina":
            masculinas.append(persona)
        else:
            femeninas.append(persona)
    mayores_masculinas = [persona for persona in mayores_edad if persona.sexo == "masculina"]
    menores_femeninas = [persona for persona in menores_edad if persona.sexo =="femenina"]
    num_personas = len(vector_personas)
    num_mayores = len(mayores_edad)
    num_femeninas = len(femeninas)
    porcentaje_mayores =  num_mayores/num_personas * 100
    porcentaje_femeninas = num_femeninas/num_personas * 100
    print(f"El número de personas mayores de edad es {len(mayores_edad)}")
    print(f"El número de personas menores de edad es {len(menores_edad)}")
    print(f"El número de personas masculinas mayores de edad es {len(mayores_masculinas)}")
    print(f"El número de personas femeninas menores de edad es {len(menores_femeninas)}")
    print(f"El porcentaje de mayores respecto del total es {porcentaje_mayores}%")
    print(f"El porcentaje de personas femeninas del total es {porcentaje_femeninas}%")

vector = leer_personas()
clasificar_personas(vector)