import os
import time


clear = lambda: os.system('cls')


def progress_bar(solution_time, quote_amount):
    
    array = '|'
    
    for i in range(0, 11):
        
        clear()
        print('Cantidad de cotizaciones generadas: ' + str(10*quote_amount))
        print('Procesando cotizaciones... ')
        array = array + '|'
        print('Progreso: ' + array + " " + str(i*10) + '%')
        time.sleep(solution_time/150)
