import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import datetime as date
import os 
import mensajes_error, inputs, mostrar_datos


mensajes_error.loading_text('Este es un programa que calcúla la distribución de temperatura en un cilindro. \n\nPara iniciar es necesario que definas las dimenciones del cilindro y el número de nodos en cada dirección.\n')
