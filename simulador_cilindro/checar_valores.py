import mensajes_error

def verificar_valor_numerico(valor):
    try:
        valor = float(valor)
    except ValueError:
        mensajes_error.error_valor_numerico()
    else:
        return True
        

