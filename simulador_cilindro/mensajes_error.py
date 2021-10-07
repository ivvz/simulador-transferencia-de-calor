import time

def err_valor_numerico():
    print(' ***ERROR*** \nTu tipo de dato no es válido \nDebes ingresar solo caracteres numericos.')
    
def loading_text(texto):
    for i in range(len(texto)):
        print(texto[i], sep=' ', end=' ', flush=True)
        time.sleep(0.2)

def error_msj():
    print('\n***** ERROR *****\n')
    time.sleep(1)

def zero_error():
    error_msj()
    print('\nEl valor no puede ser cero')
    time.sleep(1)
    print('\nIntenta nuevamente')
    time.sleep(1)

def numero_negativo_invalido():
    error_msj()
    print('\nIngresa solo valores positivos \nIntenta nuevamente')
    time.sleep(1)


def dots():
    dots = '\n....\n'
    for i in range(len(dots)):
        print(dots[i], sep=' ', end=' ')
        time.sleep(0.3)

def opcion_invalida():
    error_msj()
    print('\n*** Opción inválida ***\nTeclea solamente "1" o "0"')
    time.sleep(1)
