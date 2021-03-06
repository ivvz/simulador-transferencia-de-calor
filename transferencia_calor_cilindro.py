import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime as date
import os 

T_lims_list = []

kelvin = 273.15
current_directory = os.getcwd()

def conv_k(t):
    return t + kelvin



dia = date.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
dia = str(dia)
dia = 'reporte_' + dia

folder_dia = os.path.join(current_directory, dia)
os.makedirs(folder_dia)
dia_path = os.path.abspath(dia)

folder_tablas = os.path.join(dia_path, r'tablas')
os.makedirs(folder_tablas)

folder_imgs = os.path.join(dia_path, r'imgs')
os.makedirs(folder_imgs) 


options = '\n\n1.- Sí \n0.- No \n\nTeclea la opcion deseda: '
dia = str(date.datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))

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

def negative_error():
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
    
#################
def input_r_z():
    global R
    global Z
    print('\n\nEste es un programa que calcúla la distribución de temperatura en un cilindro. \n\nPara iniciar es necesario que definas las dimenciones del cilindro y el número de nodos en cada dirección.')
    while True:
        R = input('\n¿Cuál es el radio del cilindro? Introduce el valor en cm:  ')
        try:
            R = float(R)
            if R < 0:
                raise TypeError
            elif R == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            zero_error()
        except TypeError:
            negative_error()
        except ValueError:
            error_msj()
            print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el radio.')
                
        else:
            while True:
                Z = input('¿Cual es la altura del clindro? Introduce el valor en cm: ')
                try:
                    Z = float(Z)
                    if Z < 0:
                        raise TypeError
                    elif Z == 0:
                        raise ZeroDivisionError
                except ZeroDivisionError:
                    zero_error()
                except TypeError:
                    negative_error()
                except ValueError:
                    error_msj()
                    print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el radio.')
            
                else:                  
                    break
                
            time.sleep(1)
            print('\nEl radio del cilindro es de:', R, 'cm y la altura es de:' , Z,'cm\n') 
            break
    
##################
def input_N_M():
    global N, M
    opcion = True
    while opcion == True:
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
                        zero_error()
                    elif err == 1:
                        print('El valor tiene que ser mayor a 1')
                except TypeError:
                    negative_error()
                except ValueError:
                    error_msj()
                    print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el número de nodos en dirección r.')
                else:
                    opcion = False
                    M = N
                    break
            time.sleep(0.5)
            print('\n\nEl sistema se dividirá en:', N, 'nodos en la dirección r y z, dando un total de:',N*M, 'nodos\n')
            time.sleep(1)
            break
        
        elif opcion == '0':
            while True:
                N = input('¿Cuantos nodos quieres en la dirección r?\n')
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
                        zero_error()
                    elif err == 1:
                        print('El valor tiene que ser mayor a 1')
                except TypeError:
                    negative_error()             
                except ValueError:
                    error_msj()
                    print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el número de nodos en dirección r.')
                else:
                    opcion = False
                    while True:
                        M = input('¿Cuantos nodos quieres en la dirección z?\n')
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
                                zero_error()
                            elif err == 1:
                                print('El valor tiene que ser mayor a 1')
                        except TypeError:
                            negative_error()
                        except ValueError:
                            error_msj()
                            print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el número de nodos en dirección z.')
                        else:
                            break
                    print('El sistema se dividirá en:', N, 'nodos en la dirección r y',M, 'nodos en la dirección z dando un total de:',N*M, 'nodos\n')
                    time.sleep(1)
                    opcion ='a*2'
                    break
        else:
            opcion_invalida()

#########
def show_deltat_tab():
    opcion = True
    while opcion == True:
        print()
        inp_opcion = input('\n¿Quieres ver una tabla con los valores de delta t? ' + options)
        if inp_opcion == '1':
            print(df_deltat)
            opcion = False
        elif inp_opcion == '0':
            opcion = False
            pass
        else:
            opcion_invalida()

def save_deltat_tab():
    path_file_deltat = folder_tablas + r'\deltat_'
    opcion = True
    while opcion == True:
        inp_opcion = input('\n\n¿Quieres guardar la tabla de delta t? ' + options)
        if inp_opcion == '1':

            df_deltat.to_csv(path_file_deltat+dia+'.csv',encoding='utf-8')
            print('\nSe ha creado un archivo de estas tabla en el directorio: ', folder_tablas + '\\')
            opcion = False
        elif inp_opcion == '0':
            opcion = False
            pass
        else:
            opcion_invalida()

##########
        
def input_mat_prop():
    print('\nBién, ahora en necesario que definas las propiedades del material. Es importante que las captures en unidades mks e ingresando solo valores numericos. ')
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
            zero_error()   
        except TypeError:
            negative_error()
        except ValueError:
            error_msj()
            print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. \nPor favor ingresa nuevamente la constante de conductividad del material..')
                
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
                    zero_error()
                except TypeError:
                    negative_error()
                except ValueError:
                    error_msj()
                    print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. \nPor favor ingresa nuevamente la densidad del material.')
            
                else:
                    while True:
                        cp = input('\nIngresa el valor del cp del material. Es importante que sus unidades sean: [J/kgK] : ')
                        try:
                            cp = float(cp)
                            if cp < 0:
                                raise TypeError
                            elif N == 0:
                                raise ZeroDivisionError
                        except ZeroDivisionError:
                            zero_error()   
                        except TypeError:
                            negative_error()
                        except ValueError:
                            error_msj()
                            print('\nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. \nPor favor ingresa nuevamente el valor del cp del material.')
                                
                        else:
                            break
                    alpha = k / (rho * cp)
                    time.sleep(1)
                    print('\nLa constante de conductividad térmica (k) es:',k,'[W/mK] \nLa densidad del material ($rho$) es:',rho,'[kg/m^3], \nEl cp del material es:',cp,'[J/kgK], \nY la difusividad termica es:',alpha,'(alpha) [m^2/s]\n') 
                    break
            break
    return k, rho, cp, alpha
#################
def show_error():
    err_r_e = ((R - r_e_d[0][-1]) / R)
    if err_r_e < 0:
        err_r_e = err_r_e * -1
    print('El error en el radio externo es de:',err_r_e,'%')
    err_A_e = ((A_e_c - s_A_e) / A_e_c)*100
    if err_A_e < 0:
        err_A_e = err_A_e * -1
    print('El error en el área externa es de:',err_A_e,'%')
    err_A_t = ((A_T_c - np.sum(A_T_d[0])) / A_T_c) *100
    if err_A_t < 0:
        err_A_t = err_A_t * -1
    print('El error en el área de la tapa es de:',err_A_t,'%')
    err_Vol =((V_c - np.sum(Vol_d)) / V_c) * 100
    if err_Vol < 0:
        err_Vol = err_Vol * -1
    print('El error del volumen es de:',err_Vol,'%\n')
    time.sleep(1)
################
    
def show_tables():
    opcion = True
    while opcion == True:
        menu = input('\n¿Quieres ver alguna tabla de las dimenciones de la discretizacion?' + options)
        if menu == '1':
            opcion = False
            print(opcion)
            opcion1 = True
            while opcion1 == True:
                opcion2 = input('¿Para que dato quieres que se muestre la tabla? \n1.- Todos \n2.- Radio externo \n3.- Área interna \n4.- Área externa \n5.- Área de las tapas  \n6.- Volumen\n' )
                if opcion2 == '1':
                    opcion1 = False
                    print('\nTabla Radio externo [cm]\n',df_r_e,'\n')
                    time.sleep(1)
                    print('\nTabla Área interna [cm^2]\n',df_A_i,'\n')
                    time.sleep(1)
                    print('\nTabla Área externa [cm^2]\n',df_A_e,'\n')
                    time.sleep(1)
                    print('\nTabla Área de las tapas [cm^2]\n',df_A_T,'\n')
                    time.sleep(1)
                    print('\nTabla Volumen de nodos [cm^3]\n',df_Vol,'\n')
                    time.sleep(1)
                elif opcion2 == '2':
                    opcion1 = False
                    print('\nTabla Radio externo [cm]\n',df_r_e)
                    time.sleep(1)
                elif opcion2 == '3':
                    opcion1 = False
                    print('\nTabla Área interna [cm^2]\n',df_A_i)
                    time.sleep(1)
                elif opcion2 == '4':
                    opcion1 = False
                    print('\nTabla Área externa [cm^2]\n',df_A_e)
                    time.sleep(1)
                elif opcion2 == '5':
                    opcion1 = False
                    print('\nTabla Área de las tapas [cm^2]\n',df_A_T)
                    time.sleep(1)
                elif opcion2 == '6':
                    opcion1 = False
                    print('\nTabla Volumen de nodos [cm^3]\n',df_Vol)
                    time.sleep(1)
                else:
                    error_msj()
                    print('\nPor favor selecciona una opción válida')
                    time.sleep(1)
        elif menu == '0':
            pass
            opcion = False
        else:
            opcion_invalida()  
            
def save_tables():
    
    path_file_tab = folder_tablas + r'\disc_'
    opcion = True
    while opcion == True:
        menu = input('\n¿Quieres guardar alguna tabla de las dimenciones de la discretización?' + options)
    
        if menu == '1':
            opcion = False
            print(opcion)
            opcion1 = True
            while opcion1 == True:
                opcion2 = input('¿Para que dato quieres guardar la información de la tabla? \n1.- Todos \n2.- Radio externo \n3.- Área interna \n4.- Área externa \n5.- Área de las tapas  \n6.- Volumen\n' )
                if opcion2 == '1':
                    opcion1 = False
                    df_r_e.to_csv(path_file_tab+'r_e_'+dia+'.csv',encoding='utf-8')
                    df_A_i.to_csv(path_file_tab+'A_i_'+dia+'.csv',encoding='utf-8')
                    df_A_e.to_csv(path_file_tab+'A_e_'+dia+'.csv',encoding='utf-8')
                    df_A_T.to_csv(path_file_tab+'A_t_'+dia+'.csv',encoding='utf-8')
                    df_Vol.to_csv(path_file_tab+'Vol_'+dia+'.csv',encoding='utf-8')
                    print('\nSe ha creado un archivo de esta tabla en el directorio: ', folder_tablas + '\\')
                elif opcion2 == '2':
                    opcion1 = False
                    df_r_e.to_csv(path_file_tab+'r_e_'+dia+'.csv',encoding='utf-8')
                    print('\nSe ha creado un archivo de esta tabla en el directorio: ', folder_tablas + '\\')
                elif opcion2 == '3':
                    opcion1 = False
                    df_A_i.to_csv(path_file_tab,encoding='utf-8')
                    print('\nSe ha creado un archivo de esta tabla en el directorio: ', folder_tablas + '\\')
                elif opcion2 == '4':
                    opcion1 = False
                    df_A_e.to_csv(path_file_tab,encoding='utf-8')
                    print('\nSe ha creado un archivo de esta tabla en el directorio: ', folder_tablas + '\\')
                elif opcion2 == '5':
                    opcion1 = False
                    df_A_T.to_csv(path_file_tab,encoding='utf-8')
                    print('\nSe ha creado un archivo de esta tabla en el directorio: ', folder_tablas + '\\')
                elif opcion2 == '6':
                    opcion1 = False
                    df_Vol.to_csv(path_file_tab,encoding='utf-8')
                    print('\nSe ha creado un archivo de esta tabla en el directorio: ', folder_tablas + '\\')
                else:
                    error_msj()
                    print('\nPor favor selecciona una opción válida')
        elif menu == '0':
            pass
            opcion = False
        else:
            opcion_invalida()  
##################

def check_float(tiempo):
    punto = '.'
    inp_t = input('dato')
    try:
        for i in inp_t:
            if punto in inp_t:
                test = float(inp_t)
                flotante = 'flotante'
            else:
                flotante = 'entero'
    except ValueError:
        flotante = 'string'
    if flotante == 'flotante':
        s_float = True
        print('es un flotante')
    elif flotante == 'entero':
        print('es entero')
    elif flotante == 'string':
        print('es string')
            
            
##################
def find_time_value():
    global times
    global idx
    global near_times
    global t_fin
    times = []
    idx = []
    near_times = []
    t_sol = []
    t = 0
    punto = '.'
    test_0 = False
    flotante = ' '
    
    while True:
        cuantas = input('\n¿Para cuantos tiempos deseas ver la información (tablas y mapeo de temperaturas)? ')
        try:
            try:
                for i in cuantas:
                    if punto in cuantas:
                        test = float(cuantas)
                        flotante = 'flotante'
            except ValueError:
                        flotante = 'string'
            cuantas = int(cuantas)
            if cuantas < 0:
                raise TypeError
            if cuantas == 0:
                test_0 = True
                raise ValueError
        except TypeError:
            negative_error()
        except ValueError:
            if test_0 == True:
                error_msj()
                print('El valor no puede ser cero')
            elif flotante == 'flotante':
                error_msj()
                print('Ingresa solo numeros Enteros')
            else:
                error_msj()
                print('Tu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el número de tiempos de los que requieres ver la información.')
                         
        else:
            break
        pass
    
    values = list(range(1,cuantas+1))
    for i in values:
        while True:
            tiempo = input('\nIngresa el valor ' + str(i)+': ')
            try:
                tiempo = float(tiempo)
                if tiempo < 0:
                    raise TypeError
            except TypeError:
                negative_error()
            except ValueError:
                error_msj()
                print('Tu tipo de dato no es valido \nDebes ingresar solo caracteres numericos. Por favor ingresa nuevamente el tiempo del que requieres la informacón.')
            else:
                times.append(tiempo)
                break
            pass
    times.sort()
    print('\nSe mostraran las graficas de temperatura a los tiempos más cercanos a: ',times,'segundos\n')
        
    t_fin = max(times)
    
    while t < t_fin:
        t = t + deltat
        t_sol.append(t)
        t_sol.append(t)
    array = np.asarray(t_sol)
    
    for tiempo in times:
        idx.append(np.abs(array - tiempo).argmin())
    for i in idx:
        near_times.append(t_sol[i])
    dots()
# =============================================================================
#     for i in idx:
#         near_times.append(round(t_sol[i]))
#     print('Los valores más cercanos a los tiempos que solicitas son:',near_times,'segundos\n')
#     dots()
# 
# =============================================================================

###################
def time_count():
    global p_t
    opcion = True
    while opcion == True:
        t_c = input('\n\n¿Quieres que imprima un conteo del tiempo en la pantalla? ' + options)
        if t_c == '1':
            p_t = True
            opcion = False
            
        elif t_c == '0':
            p_t = False
            opcion = False
        else:
            opcion_invalida()
            

####### Condiciones de frontera ###########

def input_condiciones_frontera(lado):            
    opcion_1 = True

    while opcion_1 == True:
        es_conocida_T_superficie_lado = input('\n¿La temperatura de la superficie ' + lado + ' es conocida?' + options)

        if es_conocida_T_superficie_lado == '1':
            while True:
                T_conocida_lado = input('Teclea la Temperatura en °C: ')
                try:
                    T_conocida_lado = float(T_conocida_lado)
                except ValueError:
                    err_valor_numerico()
                else:
                    s_T_conocida_lado = True
                    T_conocida_lado = T_conocida_lado + kelvin
                    T_lims_list.append(T_conocida_lado)
                    break
                                        
            h_convectivo_lado = 0
            T_fluido_conv_lado = 0
            h_contacto_lado = 0
            T_otra_sup_lado = 0
            h_radiacion_lado = 0
            T_alrrededores_lado = 0
            q_lado = 0
            opcion_1 = False
            
        elif es_conocida_T_superficie_lado == '0':
            T_conocida_lado = 0
            s_T_conocida_lado = False
            opcion_2 = True
            while   opcion_2 == True:

                opcion_s_2 = input('¿La frontera ', lado , 'está en contacto con otra superficie?'+ options +'\n')

                if opcion_s_2 == '1':
                    opcion_2 = True
                    while True:
                        h_contacto_lado = input('Teclea el coeficientede contacto en [W/m2]: ')
                        try:
                            h_contacto_lado = float(h_contacto_lado)
                        except ValueError:
                            err_valor_numerico()
                        else:
                            while True:    
                                T_otra_sup_lado = input('Teclea la temperatura de la otra superficie en [°C]: ')
                                try:
                                    T_otra_sup_lado = float(T_otra_sup_lado)
                                except ValueError:
                                    err_valor_numerico()
                                else:
                                    T_otra_sup_lado = T_otra_sup_lado + kelvin
                                    T_lims_list.append(T_otra_sup_lado)
                                    break
                    
                            h_convectivo_lado = 0
                            T_fluido_conv_lado = 0
                            h_radiacion_lado = 0
                            T_alrrededores_lado = 0
                            q_lado = 0
                            break
                        
                    opcion_2 = False
                    opcion_1 = False
                
                elif opcion_s_2 == '0':
                    opcion_2 = True
                    opcion_2_1 = True         
                    while opcion_2_1 == True:
                        opcion_s_2 = input('¿La frontera de la derecha está aislada?' + options+'\n')
                        if opcion_s_2 == '1':
                            
                            h_convectivo_lado = 0
                            T_fluido_conv_lado = 0
                            h_radiacion_lado = 0
                            T_alrrededores_lado = 0
                            h_contacto_lado = 0
                            T_otra_sup_lado = 0
                            q_lado = 0
                            
                            opcion_2_1 = False                                             
                            opcion_1 = False

                        elif opcion_s_2 == '0':
                            h_contacto_lado = 0
                            T_otra_sup_lado = 0
                            
                            while True:
                                q_lado = input('¿Flux de calor en la frontera de la derecha en [W/m^2]? Si es nulo, teclea 0\n')
                                try:
                                    q_lado = float(q_lado)
                                except ValueError:
                                    err_valor_numerico()
                                else:
                                    break
                            pass
                        
                            while True:
                                h_convectivo_lado = input('¿Cual es el coeficiente convectivo del fluido en [W/m2]?\n')
                                try:
                                    h_convectivo_lado = float(h_convectivo_lado)
                                except ValueError:
                                    err_valor_numerico()
                                else:
                                    break                               
                                pass

                            while True:
                                T_fluido_conv_lado = input('Cual es la temperatura del fluido en [°C]?\n')
                                try:
                                    T_fluido_conv_lado = float(T_fluido_conv_lado)
                                except ValueError:
                                    err_valor_numerico()
                                else:
                                    T_fluido_conv_lado = T_fluido_conv_lado + kelvin
                                    T_lims_list.append(T_fluido_conv_lado)
                                    break                               
                                pass

                            while True:
                                h_radiacion_lado = input('¿Cual es el coeficiente de radiación en [W/m^2]?\n')
                                try:
                                    h_radiacion_lado = float(h_radiacion_lado)
                                except ValueError:
                                    err_valor_numerico()
                                else:
                                    break
                                pass

                            while True:
                                T_alrrededores_lado = input('Cual es la temperatura de los alrrededores  en [°C]?\n')
                                try:
                                    T_alrrededores_lado = float(T_alrrededores_lado)
                                except ValueError:
                                    err_valor_numerico()
                                else:
                                    T_alrrededores_lado = T_alrrededores_lado + kelvin
                                    T_lims_list.append(T_alrrededores_lado)
                                    break                               
                            opcion_2_1 = False
                        else:
                            opcion_invalida()                                                                
                        opcion_2 = False
                        opcion_1 = False 
                else:
                    opcion_invalida()  
                opcion_1 = False
        else:
            opcion_invalida()
    return  T_conocida_lado, s_T_conocida_lado, h_convectivo_lado, h_contacto_lado, h_radiacion_lado, T_fluido_conv_lado, T_otra_sup_lado, T_alrrededores_lado, q_lado


##################
   
input_r_z()
input_N_M()

g = 0

start = time.time()

A_T_c = np.pi * R **2
V_c = A_T_c * Z
A_e_c = 2 * np.pi * R * Z

# discretizar

Nr =np.linspace(0,R,N)
deltar = (R/100)/(N-1)

Nz = np.linspace(0,Z,M)
deltaz= (Z/100)/(M-1)

m = np.linspace(1,M,M)
n = np.linspace(1,N,N)

###

r_e = np.zeros((M,N))
for j in range(M):
    for i in range(N):
        if i == 0:
            r_e[j][i] = (0.5 * deltar)
        elif i == N-1:
            r_e[j][i] = (N-1)*deltar
        elif 0 < i < N-1:
             r_e[j][i] = r_e[j][i-1] + deltar

r_e_d = r_e * 100

r_i = np.zeros((M,N))             
for j in range(M):
    for i in range(N):
        if i == 0:
            r_i[j][i] = 0
        else:
            r_i[j][i] = r_e[j][i-1]
r_i_d = r_i * 100

A_e = np.zeros((M,N))
for j in range (M):
    for i in range(N):
        if j == 0 or j == M-1:
            A_e[j][i] = np.pi * r_e[j][i] * deltaz 
        else: 
            A_e[j][i] = 2 * np.pi * r_e[j][i] * deltaz 
A_e_d = A_e * 100 ** 2

s_A_e = 0
for j in range(M):
    s_A_e += A_e_d[j][-1]

A_i = np.zeros((M,N))
for j in range (M):
    for i in range(N):
        if i == 0:
            A_i[j][0] = 0
        else:
            A_i[j][i] = A_e[j][i-1]
A_i_d = A_i * 100 ** 2


A_T = np.zeros((M,N))
for j in range (M):
    for i in range(N):
        A_T[j][i] =np.pi*(r_e[j][i] ** 2) - np.pi * (r_i[j][i] ** 2)
A_T_d = A_T * 100 ** 2 
        
Vol = np.zeros((M,N))
for j in range(M):
    for i in range(N):
        if j == 0 or j == M-1:
            Vol[j][i] = A_T[j][i] * 0.5 * deltaz
        else:
            Vol[j][i] = A_T[j][i] * deltaz
Vol_d = Vol * 100 ** 3

show_error()     


#############
df_r_e = pd.DataFrame(r_e_d, index = m, columns = n) 
df_r_i =pd.DataFrame(r_i_d, index = m, columns = n)
df_A_i =pd.DataFrame(A_i_d, index = m, columns = n)
df_A_e = pd.DataFrame(A_e_d, index = m, columns = n)
df_A_T = pd.DataFrame(A_T_d, index = m, columns = n) 
df_Vol = pd.DataFrame(Vol_d, index = m, columns = n)

show_tables()
save_tables()
k, rho, cp, alpha = input_mat_prop()

T_conocida_u, s_T_conocida_u, h_convectivo_u, h_contacto_u, h_radiacion_u, T_fluido_conv_u, T_otra_sup_u, T_alrrededores_u, q_u = input_condiciones_frontera('superior')

T_conocida_r, s_T_conocida_r, h_convectivo_r, h_contacto_r, h_radiacion_r, T_fluido_conv_r, T_otra_sup_r, T_alrrededores_r, q_r = input_condiciones_frontera('derecha')

T_conocida_l, s_T_conocida_l, h_convectivo_l, h_contacto_l, h_radiacion_l, T_fluido_conv_l, T_otra_sup_l, T_alrrededores_l, q_l = input_condiciones_frontera('inferior')
        
########## Criterios de estabilidad ##########
deltat_list = np.zeros((M,N))
deltat_minlist = []
print('\nBuscando delta t crítico')
dots()
for j in range (M):
    for i in range(N):
        
            ########## ESQUINAS ##########
            ### Nodo N,1 ###
        if j == 0 and i == N-1:
            deltat =( 1 / (
            ( alpha * A_i[0][-1] / (Vol[0][-1] * deltar )) + (alpha * A_T[0][-1] / (Vol[0][-1] * deltaz )) + 
            (h_convectivo_u * A_T[0][-1] / (Vol[0][-1] * rho * cp )) + (h_convectivo_r * A_e[0][-1] / (Vol[0][-1] * rho * cp )) +
            (h_contacto_u * A_T[0][-1] / (Vol[0][-1] * rho * cp )) + (h_contacto_r * A_e[0][-1] / (Vol[0][-1] * rho * cp )) + 
            (h_radiacion_u * A_T[0][-1] / (Vol[0][-1] * rho * cp )) + (h_radiacion_r * A_e[0][-1] / (Vol[0][-1] * rho * cp )) 
            ))
            deltat_list[0][N-1] = deltat

            ### Nodo N,M ###
        elif j == M-1 and i == N-1:
            deltat =( 1 / (
            ( alpha * A_i[-1][-1] / (Vol[-1][-1] * deltar )) + (alpha * A_T[-1][-1] / (Vol[-1][-1] * deltaz )) + 
            (h_convectivo_r * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) + (h_convectivo_r * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) +
            (h_contacto_r * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) + (h_contacto_r * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) + 
            (h_radiacion_r * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) + (h_radiacion_r * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) 
            ))
            deltat_list[-1][-1] = deltat

            ### Nodo 1,M ###
        elif j == M-1 and i == 0:    
            deltat =( 1 / (
            ( alpha * A_e[-1][0] / (Vol[-1][0] * deltar )) + (alpha * A_T[-1][0] / (Vol[-1][0] * deltaz )) + 
            (h_convectivo_r * A_T[-1][0] / (Vol[-1][0] * rho * cp )) + 
            (h_contacto_r * A_T[-1][0] / (Vol[-1][0] * rho * cp )) + 
            (h_radiacion_r * A_T[-1][0] / (Vol[-1][0] * rho * cp ))   
            ))
            deltat_list[-1][0] = deltat
            
        elif j == 0 and i == 0:
            ### Nodo 1,1 ###
            deltat =( 1 / (
            ( alpha * A_e[0][0] / (Vol[0][0] * deltar )) + (alpha * A_T[0][0] / (Vol[0][0] * deltaz )) + 
            (h_convectivo_u * A_T[0][0] / (Vol[0][0] * rho * cp )) + 
            (h_contacto_u * A_T[0][0] / (Vol[0][0] * rho * cp )) + 
            (h_radiacion_u * A_T[0][0] / (Vol[0][0] * rho * cp ))   
            ))
            deltat_list[0][0] = deltat
            ##############################

            ########## INTERNOS ##########
        elif 0 < j < M-1 and 0 < i < N-1:
            deltat =( 1 / (
            2 * ( alpha * A_T[j][i] / (Vol[j][i] * deltaz )) + 2 * (alpha * A_e[j][i] / (Vol[j][i] * deltar ))))
            deltat_list[j][i] = deltat
            ##############################

            ########## FRONTERA ##########
            ### SUPERIOR ###
            ### 2 <= i <= N-1 ; j = 1 ###
        elif j == 0 and 0 < i < N-1:    
            deltat = ( 1 / (
            ( alpha * A_e[0][i] / (Vol[0][i] * deltar )) + (alpha * A_T[0][i] / (Vol[0][i] * deltaz )) + (alpha * A_i[0][i] / (Vol[0][i] * deltar )) +
            (h_convectivo_u * A_T[0][i] / (Vol[0][i] * rho * cp )) + 
            (h_contacto_u * A_T[0][i] / (Vol[0][i] * rho * cp )) + 
            (h_radiacion_u * A_T[0][i] / (Vol[0][i] * rho * cp ))   
            ))
            deltat_list[0][i] = deltat

            ### DERECHA ###
            ### i = N ; 2 <= j <= M-1 ###
        elif i == N-1 and 0 < j < M-1:
            deltat =( 1 / (
            ( alpha * A_i[j][-1] / (Vol[j][-1] * deltar )) + (alpha * A_T[j][-1] / (Vol[j][-1] * deltaz )) + (alpha * A_T[j][-1] / (Vol[j][-1] * deltaz )) +
            (h_convectivo_r * A_e[j][-1] / (Vol[j][-1] * rho * cp )) + 
            (h_contacto_r * A_e[j][-1] / (Vol[j][-1] * rho * cp )) + 
            (h_radiacion_r * A_e[j][-1] / (Vol[j][-1] * rho * cp ))   
            ))
            deltat_list[j][-1] = deltat

            ### INFERIOR ###
            ### 2 <= i <= M-1 ; j = M ###
        elif j == M-1 and 0 < i < N-1:    
            deltat =( 1 / (
            ( alpha * A_e[-1][i] / (Vol[-1][i] * deltar )) + (alpha * A_T[-1][i] / (Vol[-1][i] * deltaz )) + (alpha * A_i[-1][i] / (Vol[-1][i] * deltar )) +
            (h_convectivo_r * A_e[-1][i] / (Vol[-1][i] * rho * cp )) + 
            (h_contacto_r * A_e[-1][i] / (Vol[-1][i] * rho * cp )) + 
            (h_radiacion_r * A_e[-1][i] / (Vol[-1][i] * rho * cp ))   
            ))
            deltat_list[-1][i] = deltat

            ### IZQUIERDA ###
            ### i = 1 ; 2 <= j <= M-1 ###
        if 0 < j < M-1 and i == 0:
            deltat =( 1 / (
            ( alpha * A_T[j][0] / (Vol[j][0] * deltaz )) + (alpha * A_e[j][0] / (Vol[j][0] * deltar )) + (alpha * A_T[j][0] / (Vol[j][0] * deltaz )) 
            ))
            deltat_list[j][0] = deltat
        deltat_minlist.append(deltat)
        
deltat =  deltat_list.min()      
min_delta_t = np.where(deltat_list == deltat_list.min())               
print('\nEl "delta t" crítico (max) es:',deltat_list.min(),'s', 'y se encuentra en el/los nodo(s): i =',deltat_minlist.index(deltat_list.min()))
df_deltat = pd.DataFrame(deltat_list,index = m, columns = n)
df_deltat.index.name = 'Posición i / j'

show_deltat_tab()
save_deltat_tab()
0
change_d_t_otra_sup = False
while change_d_t_otra_sup == False:
    change_deltat = input('\nEl valor del delta t es de: ' + str(deltat) + ' ¿quieres elegir un delta t diferente?'+ options + '\n')
    if change_deltat =='1':
        while True:
            new_deltat = float(input('¿Cual es el valor del delta t? Recuerda que el valor tiene que ser menor a: ' + str(deltat) + '\n'))
            try:
                new_deltat = float(new_deltat)
                
                if new_deltat < 0:
                    sw_err = 1
                    raise TypeError
                elif new_deltat == 0:
                    zero_error()
                    sw_err = 2
                    raise TypeError
                elif new_deltat > deltat:
                    sw_err = 3
                    raise TypeError
                    
            except ValueError:
                print(' ***ERROR*** \nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos.')
            
            except TypeError:
                if sw_err == 1:
                    negative_error()
                elif sw_err == 2:
                    zero_error
                elif sw_err == 3:
                    error_msj()
                    print('El valor tiene que ser menor a:', deltat, 's')
            
            else:
                change_d_t_otra_sup == True
                deltat = new_deltat
                print('\nEl delta t que has elegido es:', deltat,' s')  
                break
        break    
    elif change_deltat == '0':
        change_d_t_otra_sup == True
        print('El delta t es de:', deltat)
        break
    else:
        opcion_invalida()
        


################################################################################
dots()
print('\nAhora es tiempo de calcular las temperaturas')
dots()

t = 0

while True:
    T_inc = input('¿Cual es la temperatura inicial de tu cilindro? ingresa el valor en [°C]\n')
    try:
        T_inc = float(T_inc)
    except ValueError:
        print(' ***ERROR*** \nTu tipo de dato no es vàlido \nDebes ingresar solo caracteres numericos.')
    else:
        break
    
T_inc_k = T_inc + kelvin
T_lims_list.append(T_inc_k)

for i in range(len(T_lims_list)):
    T_lims_list[i] = T_lims_list[i] - kelvin

T_t = np.ones((M,N)) * T_inc_k        

find_time_value()

T_min_max = []

if s_T_conocida_u == True and s_T_conocida_l == True and s_T_conocida_r == True:
    if T_conocida_u == T_conocida_l == T_conocida_r:
        T_t[0] = T_conocida_u
        T_min_max.append(T_conocida_u)
        T_t[-1] = T_conocida_l
        T_min_max.append(T_conocida_l)
        for j in range(1,M-1):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
        
    elif T_conocida_u == T_conocida_r and T_conocida_l != T_conocida_r:
        T_t[0] = T_conocida_u
        T_min_max.append(T_conocida_u)
        T_t[-1][0:N-1] = T_conocida_l
        T_min_max.append(T_conocida_l)
        for j in range(M-1):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
        T_t[-1][-1] = T_inc_k
        
        T_t[-1][-1] = (T_t[-1][-1] * ( 1 -
                    (alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) -
                    (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz )))
                    +
                    (alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) * ( T_t[-1][-2]) +
                    (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz ))  * (T_t[-2][-1])
    )
        
    elif T_conocida_r == T_conocida_l and T_conocida_u != T_conocida_r:
        T_t[0][0:N-1] = T_conocida_u
        T_min_max.append(T_conocida_u)
        T_t[-1] = T_conocida_l
        T_min_max.append(T_conocida_l)
        for j in range(1,M-1):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
        
        T_t[0][-1] = (T_t[0][-1] * (1 -
                    (alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) -
                    (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz )))
                    +
                    (alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) * ( T_t[0][-2]) +
                    (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz ))  * (T_t[1][-1])
    )
        
    else:
        T_t[0][0:N-1] = T_conocida_u
        T_min_max.append(T_conocida_u)
        T_t[-1][0:N-1] = T_conocida_l
        T_min_max.append(T_conocida_l)
        for j in range(1,M-1):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
        
        T_t[0][-1] = (T_t[0][-1] * (1 -
                    (alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) -
                    (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz )))
                    +
                    (alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) * ( T_t[0][-2]) +
                    (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz ))  * (T_t[1][-1])
    )
    
    
        T_t[-1][-1] = (T_t[-1][-1] * ( 1 -
                    (alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) -
                    (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz )))
                    +
                    (alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) * ( T_t[-1][-2]) +
                    (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz ))  * (T_t[-2][-1])
    )
    
elif s_T_conocida_u == True and s_T_conocida_r == True and s_T_conocida_r == False:
    if T_conocida_u == T_conocida_r:
        T_t[0] = T_conocida_u
        T_min_max.append(T_conocida_u)
        for j in range(M):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
    else:
        T_t[0][0:N-1] = T_conocida_u
        T_min_max.append(T_conocida_u)
        for j in range(1,M):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
    
        T_t[0][-1] = (T_t[0][-1] * (1 -
                    (alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) -
                    (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz )))
                    +
                    (alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) * ( T_t[0][-2]) +
                    (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz ))  * (T_t[1][-1])
    )

elif s_T_conocida_u == True and s_T_conocida_r == False and s_T_conocida_r == True:
    T_t[0] = T_conocida_u
    T_min_max.append(T_conocida_u)
    T_t[-1] = T_conocida_l
    T_min_max.append(T_conocida_l)

elif s_T_conocida_u == True and s_T_conocida_r == False and s_T_conocida_r == False:
    T_t[0] = T_conocida_u
    T_min_max.append(T_conocida_u)

elif s_T_conocida_u == False and s_T_conocida_r == True and s_T_conocida_r == True:
    if T_conocida_r == T_conocida_l:
        T_t[-1] = T_conocida_l
        T_min_max.append(T_conocida_l)
        for j in range(M-1):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
    
    else:
        T_t[-1][0:N-1] = T_conocida_l
        T_min_max.append(T_conocida_l)
        for j in range(M-1):
            T_t[j][-1] = T_conocida_r
        T_min_max.append(T_conocida_r)
    
        T_t[-1][-1] = (T_t[-1][-1] * ( 1 -
                    (alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) -
                    (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz )))
                    +
                    (alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) * ( T_t[-1][-2]) +
                    (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz ))  * (T_t[-2][-1])
    )

elif s_T_conocida_u == False and s_T_conocida_r == True and s_T_conocida_r == False:
    for j in range(1,M):
        T_t[j][-1] = T_conocida_r
    T_min_max.append(T_conocida_r)

elif s_T_conocida_u == False and s_T_conocida_r == False and s_T_conocida_r == True:
    T_t[-1] = T_conocida_l
    T_min_max.append(T_conocida_l)

else:
    pass


print('Esta es la distribucion de temperaturas al tiempo t = 0 en kelvin \n\n',pd.DataFrame(T_t))

print('Esta es la distribucion de temperaturas al tiempo t = 0 en celcius \n\n',pd.DataFrame(T_t - kelvin))
plt.show()
plt.imshow(T_t)
input('\nPara continuar presiona "ENTER"')

time_count()
########### ECUACIONES ##########

T_t_1_list = T_t.copy()
T_otra_supol = [T_t]
t_otra_supol = [t]
t_fin = max(times)
T_index = []
dct_T = {}
ax_t = []
T_tab = []

time.sleep(1)

nodos_i = list(range(1,N+1))
nodos_j = list(range(1,M+1))

if len(nodos_i) > 20:
    nodos_i = range(20)
if len(nodos_j) > 20:
    nodos_j = range(20)

while t < t_fin:

    for j in range (M):
        for i in range(N):

            
                ########## ESQUINAS ##########
                ### Sup derecha ###
                ### Nodo N,1 ###
            if j == 0 and i == N-1:
                if s_T_conocida_u == True and T_conocida_u == T_conocida_r:
                    T_t_1_list[0][-1] = T_conocida_u
                else:
                    T_t_1_list[0][-1] = ( T_t[0][-1] * ( 1 - 
                    ( alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) - (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz )) - 
                    (h_convectivo_u * deltat * A_T[0][-1] / (Vol[0][-1] * rho * cp )) - (h_convectivo_r * deltat * A_e[0][-1] / (Vol[0][-1] * rho * cp )) -
                    (h_contacto_u * deltat * A_T[0][-1] / (Vol[0][-1] * rho * cp )) - (h_contacto_r * deltat * A_e[0][-1] / (Vol[0][-1] * rho * cp )) - 
                    (h_radiacion_u * deltat * A_T[0][-1] / (Vol[0][-1] * rho * cp )) - (h_radiacion_r * deltat * A_e[0][-1] / (Vol[0][-1] * rho * cp )) 
                    ) +
                    ( alpha * deltat * A_i[0][-1] / (Vol[0][-1] * deltar )) * ( T_t[0][-2]) + (alpha * deltat * A_T[0][-1] / (Vol[0][-1] * deltaz ))  * (T_t[1][-1]) + 
                    (h_convectivo_u * deltat * A_T[0][-1] / (Vol[0][-1] * rho * cp )) * (T_fluido_conv_u) + (h_convectivo_r * deltat * A_e[0][-1] / (Vol[0][-1] * rho * cp )) * (T_fluido_conv_r) +
                    (h_contacto_u * deltat * A_T[0][-1] / (Vol[0][-1] * rho * cp )) * (T_otra_sup_u) + (h_contacto_r * deltat * A_e[0][-1] / (Vol[0][-1] * rho * cp )) * (T_otra_sup_r) + 
                    (h_radiacion_u * deltat * A_T[0][-1] / (Vol[0][-1] * rho * cp )) * (T_alrrededores_u) + (h_radiacion_r * deltat * A_e[0][-1] / (Vol[0][-1] * rho * cp )) * (T_alrrededores_r)  +
                    ((q_u * deltat * A_T[0][-1]) / (rho * Vol[0][-1] * cp)) + ((q_r * deltat * A_e[0][-1]) / (rho * Vol[0][-1] * cp)) +
                    (g * deltat)/(rho * cp)
                    )
                    

                ### Inf Derecha ###
                ### Nodo N,M ###
            elif j == M-1 and i == N-1:
                if s_T_conocida_r == True and T_conocida_l == T_conocida_r:
                    T_t_1_list[-1][-1] = T_conocida_l
                else:
                    T_t_1_list[-1][-1] = (
                    T_t[-1][-1] * ( 1 -
                    ( alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) - (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz )) - 
                    (h_convectivo_r * deltat * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) - (h_convectivo_r * deltat * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) -
                    (h_contacto_r * deltat * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) - (h_contacto_r * deltat * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) - 
                    (h_radiacion_r * deltat * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) - (h_radiacion_r * deltat * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) 
                    ) +
                    ( alpha * deltat * A_i[-1][-1] / (Vol[-1][-1] * deltar )) * ( T_t[-1][-2]) + (alpha * deltat * A_T[-1][-1] / (Vol[-1][-1] * deltaz ))  * (T_t[-2][-1]) + 
                    (h_convectivo_r * deltat * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) * (T_fluido_conv_r) + (h_convectivo_r * deltat * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) * (T_fluido_conv_r) +
                    (h_contacto_r * deltat * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) * (T_otra_sup_r) + (h_contacto_r * deltat * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) * (T_otra_sup_r) + 
                    (h_radiacion_r * deltat * A_T[-1][-1] / (Vol[-1][-1] * rho * cp )) * (T_alrrededores_r) + (h_radiacion_r * deltat * A_e[-1][-1] / (Vol[-1][-1] * rho * cp )) * (T_alrrededores_r) +
                    ((q_r * deltat * A_T[-1][-1]) / (rho * Vol[-1][-1] * cp)) + ((q_r * deltat * A_e[-1][-1]) / (rho * Vol[-1][-1] * cp)) +
                    (g * deltat)/(rho * cp)       
                    )      
                    

                ### Inf Izquierda ###
                ### Nodo 1,M ###
            elif j == M-1 and i == 0:
                if s_T_conocida_r == True:
                    T_t_1_list[-1][0] = T_conocida_l
                else:    
                    T_t_1_lirst[-1][0] = (
                    T_t[-1][0] * ( 1 -
                    ( alpha * deltat * A_e[-1][0] / (Vol[-1][0] * deltar )) - (alpha * deltat * A_T[-1][0] / (Vol[-1][0] * deltaz )) - 
                    (h_convectivo_r * deltat * A_T[-1][0] / (Vol[-1][0] * rho * cp )) - 
                    (h_contacto_r * deltat * A_T[-1][0] / (Vol[-1][0] * rho * cp )) - 
                    (h_radiacion_r * deltat * A_T[-1][0] / (Vol[-1][0] * rho * cp ))
                    ) +
                    ( alpha * deltat * A_e[-1][0] / (Vol[-1][0] * deltar )) * ( T_t[-1][1]) + (alpha * deltat * A_T[-1][0] / (Vol[-1][0] * deltaz ))  * (T_t[-2][0]) + 
                    (h_convectivo_r * deltat * A_T[-1][0] / (Vol[-1][0] * rho * cp )) * (T_fluido_conv_r) +
                    (h_contacto_r * deltat * A_T[-1][0] / (Vol[-1][0] * rho * cp )) * (T_otra_sup_r) + 
                    (h_radiacion_r * deltat * A_T[-1][0] / (Vol[-1][0] * rho * cp )) * (T_alrrederores_r) +
                    ((q_r * deltat * A_T[-1][0]) / (rho * Vol[-1][0] * cp)) +
                    (g * deltat)/(rho * cp)  
                    )  
                    
                
                ### Sup Izquierda ###
                ### Nodo 1,1 ###
            elif j == 0 and i == 0:
                if s_T_conocida_u == True:
                    T_t_1_list[0][0] = T_conocida_u
                else:
                    T_t_1_list[0][0] = (
                    T_t[0][0] * ( 1 -
                    ( alpha * deltat * A_e[0][0] / (Vol[0][0] * deltar )) - (alpha * deltat * A_T[0][0] / (Vol[0][0] * deltaz )) - 
                    (h_convectivo_u * deltat * A_T[0][0] / (Vol[0][0] * rho * cp )) - 
                    (h_contacto_u * deltat * A_T[0][0] / (Vol[0][0] * rho * cp )) - 
                    (h_radiacion_u * deltat * A_T[0][0] / (Vol[0][0] * rho * cp ))   
                    ) +
                    ( alpha * deltat * A_e[0][0] / (Vol[0][0] * deltar )) * ( T_t[0][1]) + (alpha * deltat * A_T[0][0] / (Vol[0][0] * deltaz ))  * (T_t[1][0]) + 
                    (h_convectivo_u * deltat * A_T[0][0] / (Vol[0][0] * rho * cp )) * (T_fluido_conv_u) +
                    (h_contacto_u * deltat * A_T[0][0] / (Vol[0][0] * rho * cp )) * (T_otra_sup_u) + 
                    (h_radiacion_u * deltat * A_T[0][0] / (Vol[0][0] * rho * cp )) * (T_alrrededores_u)   +
                    ((q_u * deltat * A_T[0][0]) / (rho * Vol[0][0] * cp)) +
                    (g * deltat)/(rho * cp)
                    )
                    
                ##############################


                ########## INTERNOS ##########
            elif 0 < j < M-1 and 0 < i < N-1:
                T_t_1_list[j][i] = (
                T_t[j][i] * ( 1 - 
                ( alpha * deltat * A_T[j][i] / (Vol[j][i] * deltaz )) - ( alpha * deltat * A_e[j][i] / (Vol[j][i] * deltar )) - (alpha * deltat * A_T[j][i] / (Vol[j][i] * deltaz )) - (alpha * deltat * A_i[j][i] / (Vol[j][i] * deltar ))
                ) +
                (( alpha * deltat * A_T[j][i] / (Vol[j][i] * deltaz )) * ( T_t[j-1][i])) + ((alpha * deltat * A_e[j][i] / (Vol[j][i] * deltar )) * ( T_t[j][i+1])) +  
                (( alpha * deltat * A_T[j][i] / (Vol[j][i] * deltaz )) * ( T_t[j+1][i])) + ((alpha * deltat * A_i[j][i] / (Vol[j][i] * deltar )) * ( T_t[j][i-1])) + 
                ((g * deltat)/(rho * cp))
                )
                
                ##############################

                ########## FRONTERA ##########
                ### SUPERIOR ###
                ### 2 <= i <= N-1 ; j = 1 ###
            elif j == 0 and 0 < i < N-1:
                if s_T_conocida_u == True:
                    for i in range(1,N-1):
                        T_t_1_list[0][i] = T_conocida_u
                else:
                    T_t_1_list[0][i] = (
                    T_t[0][i] * ( 1 -
                    ( alpha * deltat * A_e[0][i] / (Vol[0][i] * deltar )) - (alpha * deltat * A_T[0][i] / (Vol[0][i] * deltaz )) - (alpha * deltat * A_i[0][i] / (Vol[0][i] * deltar )) -
                    (h_convectivo_u * deltat * A_T[0][i] / (Vol[0][i] * rho * cp )) - 
                    (h_contacto_u * deltat * A_T[0][i] / (Vol[0][i] * rho * cp )) - 
                    (h_radiacion_u * deltat * A_T[0][i] / (Vol[0][i] * rho * cp ))   
                    ) +
                    ( alpha * deltat * A_e[0][i] / (Vol[0][i] * deltar )) * ( T_t[0][i+1]) + (alpha * deltat * A_T[0][i] / (Vol[0][i] * deltaz ))  * (T_t[1][i]) + (alpha * deltat * A_i[0][i] / (Vol[0][i] * deltar )) * (T_t[0][i-1]) +
                    (h_convectivo_u * deltat * A_T[0][i] / (Vol[0][i] * rho * cp )) * (T_fluido_conv_u) +
                    (h_contacto_u * deltat * A_T[0][i] / (Vol[0][i] * rho * cp )) * (T_otra_sup_u) +  
                    (h_radiacion_u * deltat * A_T[0][i] / (Vol[0][i] * rho * cp )) * (T_alrrededores_u) +
                    ((q_u * deltat * A_T[0][i]) / (rho * Vol[0][i] * cp)) +
                    (g * deltat)/(rho * cp)
                    )
                    

                ### DERECHA ###
                ### i = N ; 2 <= j <= M-1 ###
            elif i == N-1 and 0 < j < M-1:
                if s_T_conocida_r == True:
                    for j in range(1,M-1):
                        T_t_1_list[j][-1] = T_conocida_r
                else:
                    T_t_1_list[j][-1] = (
                    T_t[j][-1] * ( 1 -
                    ( alpha * deltat * A_i[j][-1] / (Vol[j][-1] * deltar )) - (alpha * deltat * A_T[j][-1] / (Vol[j][-1] * deltaz )) - (alpha * deltat * A_T[j][-1] / (Vol[j][-1] * deltaz )) -
                    (h_convectivo_r * deltat * A_e[j][-1] / (Vol[j][-1] * rho * cp )) - 
                    (h_contacto_r * deltat * A_e[j][-1] / (Vol[j][-1] * rho * cp )) - 
                    (h_radiacion_r * deltat * A_e[j][-1] / (Vol[j][-1] * rho * cp ))   
                    ) +
                    ( alpha * deltat * A_i[j][-1] / (Vol[j][-1] * deltar )) * ( T_t[j][i-1]) + (alpha * deltat * A_T[j][-1] / (Vol[j][-1] * deltaz ))  * (T_t[j-1][i]) + (alpha * deltat * A_T[j][-1] / (Vol[j][-1] * deltaz )) * (T_t[j+1][i]) +
                    (h_convectivo_r * deltat * A_e[j][-1] / (Vol[j][-1] * rho * cp )) * (T_fluido_conv_r) +
                    (h_contacto_r * deltat * A_e[j][-1] / (Vol[j][-1] * rho * cp )) * (T_otra_sup_r) +  
                    (h_radiacion_r * deltat * A_e[j][-1] / (Vol[j][-1] * rho * cp )) * (T_alrrededores_r) +
                    ((q_r * deltat * A_e[j][-1]) / (rho * Vol[j][-1] * cp)) +
                    (g * deltat)/(rho * cp)
                    )
                    

                ### INFERIOR ###
                ### 2 <= i <= M-1 ; j = M ###
            elif j == M-1 and 0 < i < N-1:
                if s_T_conocida_r == True:
                    for i in range(1,N-1):
                        T_t_1_list[-1][i] = T_conocida_u
                else:
                    T_t_1_list[-1][i] = (
                    T_t[-1][ir] * ( 1 -
                    ( alpha * deltat * A_e[-1][i] / (Vol[-1][i] * deltar )) - (alpha * deltat * A_T[-1][i] / (Vol[-1][i] * deltaz )) - (alpha * deltat * A_i[-1][i] / (Vol[-1][i] * deltar )) -
                    (h_convectivo_r * deltat * A_e[-1][i] / (Vol[-1][i] * rho * cp )) - 
                    (h_contacto_r * deltat * A_e[-1][i] / (Vol[-1][i] * rho * cp )) - 
                    (h_radiacion_r * deltat * A_e[-1][i] / (Vol[-1][i] * rho * cp ))   
                    ) +
                    ( alpha * deltat * A_e[-1][i] / (Vol[-1][i] * deltar )) * ( T_t[-1][i+1]) + (alpha * deltat * A_T[-1][i] / (Vol[-1][i] * deltaz ))  * (T_t[-2][i]) + (alpha * deltat * A_i[-1][i] / (Vol[-1][i] * deltar )) * (T_t[-1][i-1]) +
                    (h_convectivo_r * deltat * A_T[-1][i] / (Vol[-1][i] * rho * cp )) * (T_fluido_conv_r) +
                    (h_contacto_r * deltat * A_T[-1][i] / (Vol[-1][i] * rho * cp )) * (T_otra_sup_r) +  
                    (h_radiacion_r * deltat * A_T[-1][i] / (Vol[-1][i] * rho * cp )) * (T_alrrederores_r) +
                    ((q_r * deltat * A_T[-1][i]) / (rho * Vol[-1][i] * cp)) +
                    (g * deltat)/(rho * cp)
                    )

                ### IZQUIERDA ###
                ### i = 1 ; 2 <= j <= M-1 ###
            if 0 < j < M-1 and i == 0:
                T_t_1_list[j][0] = (
                T_t[j][0] * ( 1 -
                ( alpha * deltat * A_T[j][0] / (Vol[j][0] * deltaz )) - (alpha * deltat * A_e[j][0] / (Vol[j][0] * deltar )) - (alpha * deltat * A_T[j][0] / (Vol[j][0] * deltaz )) 
                ) +
                ( alpha * deltat * A_T[j][0] / (Vol[j][0] * deltaz )) * ( T_t[j-1][0]) + (alpha * deltat * A_T[j][0] / (Vol[j][0] * deltaz ))  * (T_t[j+1][0]) + (alpha * deltat * A_e[j][0] / (Vol[j][0] * deltar )) * (T_t[j][i+1]) + 
                (g * deltat)/(rho * cp)
                )
                
                
    T_t = T_t_1_list.copy()
    T_otra_supol.append(T_t)
    T_otra_supol_arr = np.array(T_otra_supol)
    T_otra_supol_arr = T_otra_supol_arr - kelvin
    t = t + deltat
    t_otra_supol.append(t)
        
    
    for i in range(N):
        ax_t.append(str(round(float(r_e_d[0][i]),3)))
        ay_t = [round(i*deltaz*100,3) for i in range(M)]
    
    if p_t == True:
        print('Tiempo actual =',t,'s')          
            
    if t in near_times: 
        T_index.append(t_otra_supol.index(t))
        T_tab.append(T_otra_supol[t_otra_supol.index(t)] - kelvin)
        
        path_file_T = folder_tablas + r'\T_t_' +str(i)+'_'+dia+'.csv'        
        dct_T['T_t_%s' % t_otra_supol.index(t)] = T_otra_supol[t_otra_supol.index(t)] - kelvin

        
        print('\nDisrtibución de temperatura al tiempo T_t = ',str(t_otra_supol[-1]),'\n',pd.DataFrame(T_otra_supol[t_otra_supol.index(t)] - kelvin ))
        
        loading_text('GENERANDO MAPEO...')
        
        time.sleep(1)

        plt.show(block=False)
        fig, ax = plt.subplots()
        im = ax.imshow(T_otra_supol_arr[t_otra_supol.index(t)], cmap='hot', vmin = T_inc - 20, vmax = max(T_lims_list) + 50)#,origin='down')
        cbar = plt.colorbar(im)
        cbar.ax.set_xlabel('°C')
        cbar.ax.set_ylabel('°C', rotation = 360)
        plt.xlabel('L [cm] ')
        plt.ylabel('h [cm] ')
        ax.set_xticks(nodos_i)
        ax.set_yticks(nodos_j)         
        #ax.set_xticklabels(ax_t, rotation = 45)
        #ax.set_yticklabels(ay_t, rotation = 45 ) 
        title_gph = 't = ' + str(round(t_otra_supol[-1],1)) + ' s'
        plt.title(title_gph.format(4))
        fig.tight_layout()
        plt.savefig(folder_imgs +r'\t_' + str(t_otra_supol[-1]) + '_s_'+dia+'.png',transparent = False)
        plt.show()
        print('\nLas imagenes han sido guardadas en el directorio: ', folder_imgs +'\\')
    else:
        pass
    
df_T_t = pd.DataFrame(T_t, index = m, columns = n)    
        
for i in dct_T.keys():
    dia = date.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    dia = str(dia)    
    path_file_T = folder_tablas + r'\T_t_' +str(i)+'_'+dia+'.csv' 
    pd.DataFrame(dct_T[i]).to_csv(path_file_T,encoding='utf-8')

################################################################################
################################################################################
################################################################################
################################################################################
################################################################################


Dl = 2.3e-14 #[m^2/s]
Db = 2.3e-14
g = 2.43 #[J/m^2]
d = 0.00001 #[m]
Vm = 17 #[m^3/mol]
a_ltt = 3
a_gb = 4
R = 8.314 # [J / mol k]

#### Latice
neck_g_lattice = np.zeros((len(times),M,N))
shrk_lattice_arr = np.zeros_like(neck_g_lattice)
a_arr = np.ones((M,N))
a = 1e-3/2 #[m]
l0 = 2 * a
a_arr = a_arr * a
a_arr_new = np.zeros_like(neck_g_lattice)
l0_arr = np.ones((M,N)) * l0 
dl_arr = np.zeros((len(times),M,N))
new_l = np.zeros((len(times),M,N))
shrk_perc = np.zeros_like(neck_g_lattice)

for tab in range(len(neck_g_lattice)):
    for j in range(M):
        for i in range(N):
            neck_g_lattice[tab][j][i] = ( ((16 * Dl * g * Vm * a) / (R * (T_tab[tab][j][i] + kelvin )) ) *  near_times[tab]) ** (1 / 4) 
            
            shrk_lattice_arr[tab][j][i] = (((Dl * g * Vm) / (R * (T_tab[tab][j][i] + kelvin) * a ** 3) ) ** (0.5)) * near_times[tab] ** 0.5

for tab in range(len(neck_g_lattice)):
    for j in range(M):
        for i in range(N):
            a_arr_new[tab][j][i] = (( (neck_g_lattice[tab][j][i]) ** 0.5)/(4 * shrk_lattice_arr[tab][j][i])) ** 0.5
            
for tab in range(len(dl_arr)):
    for j in range(M):
        for i in range(N):
            dl_arr[tab][j][i] = shrk_lattice_arr[tab][j][i] * l0_arr[j][i]
            
for tab in range(len(new_l)):
    for j in range(M):
        for i in range(N):
            new_l[tab][j][i] = l0_arr[j][i] - dl_arr[tab][j][i] 
            
for tab in range(len(shrk_perc)):
    for j in range(M):
        for i in range(N):
            shrk_perc[tab][j][i] = ((l0 - new_l[tab][j][i])/(l0)) * 100 



### grain boundary 
neck_g_gb = np.zeros((len(times),M,N))
shrk_gb_arr = np.zeros_like(neck_g_gb)

for i in range(len(neck_g_lattice)):
    for z in range(M):
        for r in range(N):
            neck_g_gb[i][z][r] = (( (48 * Db * g * d * Vm * a_gb**2) / (R * T_tab[i][z][r]) )) * near_times[i]
            
            shrk_gb_arr[i][z][r] = ((3 * Db * g * d * Vm) / (4 * R * T_tab[i][z][r]) * a_gb ** 4 ) ** (1/3) * near_times[i] ** (1/3)








end = time.time()
print('El tiempo de ejecucion del programa fue de',end - start,' s')  
