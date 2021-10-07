import time
  
def pausa(tiempo=0.5):
    time.sleep(tiempo)
    
def loading_text(texto,tiempo=0.1):
    for i in texto:
        print(i, end=' ',flush=True)
        time.sleep(tiempo) 
        
def mensaje_error():
    loading_text('\n***** ERROR *****\n')
    pausa()

def error_valor_numerico():
    mensaje_error()
    loading_text('\nTu tipo de dato no es válido \nDebes ingresar solo caracteres numericos.\n')

def zero_error():
    mensaje_error()
    loading_text('\nEl valor no puede ser cero\n')
    pausa()
    loading_text('\n***** Intenta nuevamente *****\n')
    pausa()

def numero_negativo_invalido():
    mensaje_error()    
    loading_text('\nIngresa solo valores positivos \nIntenta nuevamente\n')
    pausa()

def dots():
    loading_text('\n....\n',0.3)

def opcion_invalida():
    mensaje_error()
    loading_text('\n*** Opción inválida ***\nTeclea solamente "1" o "0"\n')
    pausa()