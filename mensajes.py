def loading_text(texto):
    for i in range(len(texto)):
        print(texto[i], sep='', end=' ', flush=True)
        time.sleep(0.01)

def mensaje_error():
    loading_text('\n***** ERROR *****\n')
    time.sleep(1)

def err_valor_numerico():
    mensaje_error()
    loading_text('\nTu tipo de dato no es válido \nDebes ingresar solo caracteres numericos.')

def zero_error():
    mensaje_error()
    loading_text('\nEl valor no puede ser cero\n')
    time.sleep(1)
    loading_text('\n***** Intenta nuevamente *****\n')
    time.sleep(1)

def negative_error():
    mensaje_error()    
    loading_text('\nIngresa solo valores positivos \nIntenta nuevamente\n')
    time.sleep(1)

def dots():
    dots = '\n....\n'
    for i in range(len(dots)):
        print(dots[i], sep=' ', end=' ')
        time.sleep(0.3)

def opcion_invalida():
    mensaje_error()
    loading_text('\n*** Opción inválida ***\nTeclea solamente "1" o "0"\n')
    time.sleep(1)


