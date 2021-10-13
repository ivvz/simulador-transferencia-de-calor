import time
import mensajes_error

options = '\n\n1.- Sí \n0.- No \n\nTeclea la opcion deseda: '

def texto_inicio():
    mensajes_error.loading_text('\n\nEste es un programa que calcúla la distribución de temperatura en un cilindro. \n\nPara iniciar es necesario que definas las dimenciones del cilindro y el número de nodos en cada dirección.\n')

def set_radio_altura():
    while True:
        R = input('\n¿Cuál es el radio del cilindro? Introduce el valor en cm:  ')
        try:
            R = float(R)
            if R < 0:
                raise TypeError
            elif R == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            mensajes_error.zero_error()
        except TypeError:
            mensajes_error.numero_negativo_invalido()
        except ValueError:
            mensajes_error.error_valor_numerico() 
            mensajes_error.loading_text('\nPor favor ingresa nuevamente el radio.\n')
        else:
            while True:
                Z = input('\n¿Cual es la altura del clindro? Introduce el valor en cm: ')
                try:
                    Z = float(Z)
                    if Z < 0:
                        raise TypeError
                    elif Z == 0:
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    mensajes_error.zero_error()
                except TypeError:
                   mensajes_error.numero_negativo_invalido()
                except ValueError:
                  mensajes_error.error_valor_numerico()
                  mensajes_error.loading_text('\nPor favor ingresa nuevamente la altura.\n')
            
                else:                  
                    break
                
            time.sleep(1)
            print('\nEl radio del cilindro es de: ' + str(R) + ' cm y la altura es de: '  + str(Z) + ' cm\n') 
            break
    return R, Z

##################
def set_nodos():
    while True:

        opcion = input('\n¿Quieres el mismo nùmero de nodos en la dirección r y z? ' + options)

        if opcion == '1':
            while True:
                N = input('\n¿Cuantos nodos quieres en cada dirección? ')
                try:
                    N = int(N)
                    if N < 0:
                        raise TypeError
                    elif N == 0:
                        err = 0
                        raise ZeroDivisionError
                    elif N == 1:
                        err = 1
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    if err == 0:
                        mensajes_error.zero_error()
                    elif err == 1:
                       mensajes_error.loading_text('El valor tiene que ser mayor a 1\n')
                except TypeError:
                   mensajes_error.numero_negativo_invalido()
                except ValueError:
                   mensajes_error.error_valor_numerico() 
                   mensajes_error.loading_text('Por favor ingresa nuevamente el número de nodos en dirección r.')
                else:
                    opcion = False
                    M = N
                    break   
            break

        elif opcion == '0':
            while True:
                N = input('\n¿Cuantos nodos quieres en la dirección r?\n')
                try:
                    N = int(N)
                    if N < 0:
                        raise TypeError
                    elif N == 0:
                        err = 0
                        raise ZeroDivisionError
                    elif N == 1:
                        err = 1
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    if err == 0:
                        mensajes_error.zero_error()
                    elif err == 1:
                        mensajes_error.loading_text('\El valor tiene que ser mayor a 1\n')
                except TypeError:
                    mensajes_error.numero_negativo_invalido()             
                except ValueError:
                    mensajes_error.error_valor_numerico()
                    mensajes_error.loading_text('\nPor favor ingresa nuevamente el número de nodos en dirección r.\n')
                else:
                    opcion = False
                    while True:
                        M = input('\n¿Cuantos nodos quieres en la dirección z?\n')
                        try:
                            M = int(M)
                            if M < 0:
                                raise TypeError
                            elif M == 0:
                                err = 0
                                raise ZeroDivisionError
                            elif M == 1:
                                err = 1
                                raise ZeroDivisionError
                        except ZeroDivisionError:
                            if err == 0:
                               mensajes_error.zero_error()
                            elif err == 1:
                                mensajes_error.loading_text('\nEl valor tiene que ser mayor a 1\n')
                        except TypeError:
                            mensajes_error.numero_negativo_invalido()
                        except ValueError:
                            mensajes_error.error_valor_numerico() 
                            mensajes_error.loading_text('\nPor favor ingresa nuevamente el número de nodos en dirección z.\n')
                        else:
                            break
                    break
                break
            break    
        else:
            mensajes_error.opcion_invalida()
    time.sleep(0.5)
    print('\nEl sistema se dividirá en:', N, 'nodos en la dirección r y z, dando un total de:',N*M, 'nodos\n')
    time.sleep(1)
    return N,M
    


def propiedades_termodinamicas():
    print('\nBién. Ahora en necesario que definas las propiedades del material. Es importante que las captures en unidades mks e ingresando solo valores numericos. ')
    time.sleep(1)

    while True:
        k = input('\nIngresa el valor de la constante de conductividad térmica del material (k). Es importante que sus unidades sean: [W/mK] : ')
        try:
            k = float(k)
            if k < 0:
                raise TypeError
            elif k == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            mensajes_error.zero_error()   
        except TypeError:
            mensajes_error.numero_negativo_invalido()
        except ValueError:
            mensajes_error.error_valor_numerico()
            mensajes_error.loading_text('\nPor favor ingresa nuevamente la constante de conductividad del material.\n')
                
        else:
            while True:
                rho = input('\nIngresa el valor de la densidad del material. Es importante que sus unidades sean: [kg/m^3] : ')            
                try:
                    rho = float(rho)
                    if rho < 0:
                        raise TypeError
                    elif rho == 0:
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    mensajes_error.zero_error()
                except TypeError:
                    mensajes_error.numero_negativo_invalido()
                except ValueError:
                    mensajes_error.error_valor_numerico()
                    mensajes_error.loading_text('\nPor favor ingresa nuevamente la densidad del material.\n')
            
                else:
                    while True:
                        cp = input('\nIngresa el valor del cp del material. Es importante que sus unidades sean: [J/kgK] : ')
                        try:
                            cp = float(cp)
                            if cp < 0:
                                raise TypeError
                            elif cp == 0:
                                raise ZeroDivisionError
                        except ZeroDivisionError:
                            mensajes_error.zero_error()   
                        except TypeError:
                            mensajes_error.numero_negativo_invalido()
                        except ValueError:
                            mensajes_error.error_valor_numerico()
                            mensajes_error.loading_text('\nPor favor ingresa nuevamente el valor del cp del material.\n')
                                
                        else:
                            break
                    alpha = k / (rho * cp)
                    time.sleep(1)
                    print('\nLa constante de conductividad térmica (k) es:',k,'[W/mK] \nLa densidad del material ($rho$) es:',rho,'[kg/m^3], \nEl cp del material es:',cp,'[J/kgK], \nY la difusividad termica es:',alpha,'(alpha) [m^2/s]\n') 
                    break
            break
    return k, rho, cp, alpha

