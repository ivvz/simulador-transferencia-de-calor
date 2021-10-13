import mensajes_error, checar_valores
KELVIN = 273

def input_condiciones_frontera(lado):
    condiciones_frontera = dict()

    while True:
        Temp_superficie_lado_conocida = mensajes_error.preguntar_con_opciones('\n¿La temperatura de la superficie ' + lado + ' es conocida?')
   
        if Temp_superficie_lado_conocida == '1':
            condiciones_frontera = set_temperatura_superficial(lado)
            break
        
        elif Temp_superficie_lado_conocida == '0':
            
            condiciones_frontera['T_conocida_lado'] = 0
            #condiciones_frontera['s_T_conocida_lado'] = False
            
            frontera_en_contacto = mensajes_error.preguntar_con_opciones('¿La frontera ' + lado + ' está en contacto con otra superficie?')
            if frontera_en_contacto == '1':
                set_frontera_en_contacto(lado)
                
            elif frontera_en_contacto == '0':
                
                condiciones_frontera['h_contacto_lado'] = 0
                condiciones_frontera['T_otra_sup_lado'] = 0
                condiciones_frontera['q_lado'] = set_flux(lado) 
                condiciones_frontera['h_convectivo_lado'] = set_coef_convectivo()
                condiciones_frontera['T_fluido_conv_lado'] = set_coef_convectivo()
                condiciones_frontera['h_radiacion_lado'] = set_temp_fluido_convectivo()
                condiciones_frontera['T_alrrededores_lado'] = set_temp_alrrededores()
                condiciones_frontera['temp_superficie_conocida'] = False
                break
            else:
                mensajes_error.opcion_invalida()
        else:
            mensajes_error.opcion_invalida()
                
                
    return condiciones_frontera
    



    
def set_temperatura_superficial(lado):
    
    condiciones_frontera = dict()
    
    while True:
        
        T_conocida_lado = input('Ingresa la Temperatura en °C: ')
        if checar_valores.verificar_valor_numerico(T_conocida_lado):
            condiciones_frontera['T_conocida_lado'] = float(T_conocida_lado) + KELVIN
            condiciones_frontera['h_convectivo_lado'] = 0
            condiciones_frontera['T_fluido_conv_lado'] = 0
            condiciones_frontera['h_contacto_lado'] = 0
            condiciones_frontera['T_otra_superficie_lado'] = 0
            condiciones_frontera['h_radiacion_lado'] = 0
            condiciones_frontera['T_alrrededores_lado'] = 0
            condiciones_frontera['q_lado'] = 0
            condiciones_frontera['temp_superficie_conocida'] = False
            #T_lims_list.append(T_conocida_lado)
            return condiciones_frontera
            break
        else:
            pass

def set_frontera_en_contacto(lado):
    condiciones_frontera = dict()
    while True:
        
        h_contacto_lado = input('Teclea el coeficientede contacto en [W/m2]: ')
        if checar_valores.verificar_valor_numerico(h_contacto_lado):
            condiciones_frontera['h_convectivo_lado'] = float(h_contacto_lado)
            T_otra_superficie_lado = input('Teclea la temperatura de la otra superficie en [°C]: ')
            if checar_valores.verificar_valor_numerico(T_otra_superficie_lado):
                condiciones_frontera['T_otra_superficie_lado'] = float(T_otra_superficie_lado) + KELVIN
                #T_lims_list.append(T_otra_sup_lado)
                condiciones_frontera['h_convectivo_lado'] = 0
                condiciones_frontera['T_fluido_conv_lado'] = 0
                condiciones_frontera['h_contacto_lado'] = 0
                condiciones_frontera['T_otra_superficie_lado'] = 0
                condiciones_frontera['T_alrrededores_lado'] = 0
                condiciones_frontera['q_lado'] = 0
                condiciones_frontera['temp_superficie_conocida'] = False
                break
            else:
                pass
        else:
            pass                        
        
def set_flux(lado):
     q_lado = input('¿Flux de calor en la frontera ' + lado +   ' en [W/m^2]? Si es nulo, teclea 0\n')
     if checar_valores.verificar_valor_numerico(q_lado):
         return float(q_lado)
     else:
         pass
    
def set_coef_convectivo():
    while True:
        h_convectivo_lado = input('¿Cual es el coeficiente convectivo del fluido en [W/m2]?\n')
        if checar_valores.verificar_valor_numerico(h_convectivo_lado):
            return float(h_convectivo_lado)
        else:
            pass



def set_temp_fluido_convectivo():
    while True:
        T_fluido_conv_lado = input('Cual es la temperatura del fluido en [°C]?\n')
        if checar_valores.verificar_valor_numerico(T_fluido_conv_lado):
            #T_lims_list.append(T_fluido_conv_lado)
            return float(T_fluido_conv_lado) + KELVIN
        else:
            pass


def set_coef_radiacion():
    while True:
        h_radiacion_lado = input('¿Cual es el coeficiente de radiación en [W/m^2]?\n')
        if checar_valores.verificar_valor_numerico(h_radiacion_lado):
            #T_lims_list.append(T_fluido_conv_lado)
            return float(h_radiacion_lado) 
        else:
            pass

def set_temp_alrrededores():
    while True:
        T_alrrededores_lado = input('Cual es la temperatura de los alrrededores  en [°C]?\n')
        if checar_valores.verificar_valor_numerico(T_alrrededores_lado):
            #T_lims_list.append(T_alrrededores_lado)
            return float(T_alrrededores_lado) + KELVIN 
        else:
            pass

    
 
               