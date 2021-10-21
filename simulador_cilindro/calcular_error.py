import numpy as np


radio = 10
altura = 10
num_nodos_en_r = 5
num_nodos_en_z = 5

area_tapa_cilindro = np.pi * radio **2
volumen_cilindro = area_tapa_cilindro * altura
area_externa_cilindro = 2 * np.pi * radio * altura

# discretizar

posicion_nodos_en_r = np.linspace(0,radio,num_nodos_en_r)
delta_r = (radio / 100)/(num_nodos_en_r - 1) # convierte el valor a metros

posicion_nodos_en_z = np.linspace(0,altura,num_nodos_en_z)
delta_z= (altura/100)/(num_nodos_en_z-1) # convierte el valor a metros

#m = np.linspace(1,num_nodos_en_z,num_nodos_en_z)
#n = np.linspace(1,num_nodos_en_r,num_nodos_en_r)

###

radio_externo = np.zeros((num_nodos_en_z,num_nodos_en_r))



def calcular_radio_externo(num_nodos_en_r):
    radios_externos = np.linspace(1,num_nodos_en_r,num_nodos_en_r)
    radios_externos[0] =  (0.5 * delta_r)
    radios_externos[-1] = (num_nodos_en_r - 1) * delta_r
    radios_externos[1:num_nodos_en_r -1] = (radios_externos[1:num_nodos_en_r -1] - 1) * delta_r + 0.5 * delta_r
    print( radios_externos)
    return radios_externos


def calcular_radio_interno(num_nodos_en_r):
    radios_internos = np.linspace(1,num_nodos_en_r,num_nodos_en_r)
    radios_internos[0] =  0
    radios_internos[1:] = ((radios_internos[1:] - 1) - 0.5) * delta_r 
    print(radios_internos)
    return radios_internos


def calcular_area_externa(num_nodos_en_r):
    areas_externas = np.linspace(1,num_nodos_en_r,num_nodos_en_r)
    radios_externos = calcular_radio_externo(num_nodos_en_r)
    #np.pi * * delta_z
    
    pass

calcular_radio_externo(5)
calcular_radio_interno(5)
    
#     matriz_radio_interno = np.zeros((num_nodos_en_z,num_nodos_en_r))  
               
# for j in range(num_nodos_en_z):
#     for i in range(num_nodos_en_r):
#         if i == 0:
#             radio_interno[j][i] = 0
#         else:
#             radio_interno[j][i] = radio_externo[j][i-1]
# radio_interno_d = radio_interno * 100

# area_externa = np.zeros((num_nodos_en_z,num_nodos_en_r))
# for j in range (num_nodos_en_z):
#     for i in range(num_nodos_en_r):
#         if j == 0 or j == num_nodos_en_z-1:
#             area_externa[j][i] = np.pi * radio_externo[j][i] * delta_z 
#         else: 
#             area_externa[j][i] = 2 * np.pi * radio_externo[j][i] * delta_z 
# area_externa_d = area_externa * 100 ** 2

# s_area_externa = 0
# for j in range(num_nodos_en_z):
#     s_area_externa += area_externa_d[j][-1]

# A_i = np.zeros((num_nodos_en_z,num_nodos_en_r))
# for j in range (num_nodos_en_z):
#     for i in range(num_nodos_en_r):
#         if i == 0:
#             A_i[j][0] = 0
#         else:
#             A_i[j][i] = area_externa[j][i-1]
# A_i_d = A_i * 100 ** 2


# A_T = np.zeros((num_nodos_en_z,num_nodos_en_r))
# for j in range (num_nodos_en_z):
#     for i in range(num_nodos_en_r):
#         A_T[j][i] =np.pi*(radio_externo[j][i] ** 2) - np.pi * (radio_interno[j][i] ** 2)
# A_T_d = A_T * 100 ** 2 
        
# Vol = np.zeros((num_nodos_en_z,num_nodos_en_r))
# for j in range(num_nodos_en_z):
#     for i in range(num_nodos_en_r):
#         if j == 0 or j == num_nodos_en_z-1:
#             Vol[j][i] = A_T[j][i] * 0.5 * delta_z
#         else:
#             Vol[j][i] = A_T[j][i] * delta_z
# Vol_d = Vol * 100 ** 3
    
    
