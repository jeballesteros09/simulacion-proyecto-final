import simpy
import random
from progressbar import progress_bar
from comments import quote_comments
from excelgenerator import excel_generator


#   generador de cantidad de cotizaciones
quote_amount = random.randint(1, 2)


def analyst(env, name, quote, tools, concepts):
    #   calculo de habilidad
    ability = tools + concepts

    #   experto
    if ability == 2 and quote == 1:
        solution_time = random.randint(3, 5)
    elif ability == 2 and quote == 2:
        solution_time = random.randint(6, 8)
    
    #   intermedio
    elif ability == 1 and quote == 1:
        solution_time = random.randint(6, 8)
    elif ability == 1 and quote == 2:
        solution_time = random.randint(9, 11)

    #   novato
    elif ability == 0 and quote == 1:
        solution_time = random.randint(8, 10)
    elif ability == 0 and quote == 2:
        solution_time = random.randint(10, 30)

    progress_bar(solution_time, quote_amount)        
    
    yield env.timeout(solution_time)

    print(str(quote_comments(name, quote, ability, env.now)))

    excel_generator(name, quote, ability, env.now)


env = simpy.Environment()

for i in range(quote_amount):
    #   instanciamos a los analistas
    #   estructura para los analistas: 
    #   analyst(ambiente de simulacion, 'nombre apellido', dificultad de cotizacion, conocimiento de herramientas, conocimiento de conceptos)
    env.process(analyst(env, 'Juan Perez', random.randint(1, 2), 1, 1))
    env.process(analyst(env, 'Diana Prince', random.randint(1, 2), 1, 1))
    env.process(analyst(env, 'Robin Hood', random.randint(1, 2), 1, 0))
    env.process(analyst(env, 'Juana de Arco', random.randint(1, 2), 0, 1))
    env.process(analyst(env, 'Johnny Bravo', random.randint(1, 2), 1, 0))
    env.process(analyst(env, 'Clark Kent', random.randint(1, 2), 0, 0))
    env.process(analyst(env, 'Michael Jackson', random.randint(1, 2), 1, 1))
    env.process(analyst(env, 'Ruben Blades', random.randint(1, 2), 0, 0))
    env.process(analyst(env, 'Pablo Marmol', random.randint(1, 2), 0, 0))
    env.process(analyst(env, 'Pedro Picapiedra', random.randint(1, 2), 0, 0))

env.run(until=31)   #   unidad de tiempo: minutos
