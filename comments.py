import random
from phrases import phrases


def quote_comments(name, quote, ability, time):
    
    a = []

    a.append('Analista: ' + name)

    if ability == 2:
        a.append('Habilidad: Experto')
    elif ability == 1:
        a.append('Habilidad: Intermedio')
    else: 
        a.append('Habilidad: Novato')
    
    if quote == 1:
        a.append('Dificultad de solicitud: Facil') 
    else:
        a.append('Dificultad de solicitud: Dificil')
        
    comment = random.randint(0, 6)

    a.append('Comentarios: ' + phrases[comment])
    a.append('Cotizacion completada a los ' + str(time) + ' minutos.')

    return a
