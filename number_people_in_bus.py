'''
Por la ciudad circula un autobús que lleva y deja a algunas personas en cada parada.

Se le proporciona una lista (o matriz) de pares de números enteros. Los elementos de cada par representan el número de personas que suben al autobús (el primer elemento) y el número de personas que bajan del autobús (el segundo elemento) en una parada.

Tu tarea es devolver el número de personas que siguen en el autobús después de la última parada (después de la última matriz). Aunque sea la última parada, puede que el autobús no esté vacío y que todavía haya gente dentro, probablemente durmiendo :D

Echa un vistazo a los casos de prueba.
'''

def number(bus_stops):
    final = sum([bus[0] - bus[1] for bus in bus_stops])
    return final