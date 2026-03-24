#Usando un programa que hayas escrito y que tenga una función, guardá esa función en un archivo separado. Importá la función en tu archivo principal y llamala usando cada uno de estos enfoques:
#import nombre_módulo
#from nombre_módulo import nombre_función
#from nombre_módulo import nombre_función as nf
#import nombre_módulo as nm
#from nombre_módulo import *

import printing_models
diseños_no_imprimidos = ['coche', 'avión', 'barco']
modelos_completados = []

printing_models.imprimir_modelos(diseños_no_imprimidos, modelos_completados)
printing_models.mostrar_modelos_completados(modelos_completados)

from printing_models import imprimir_modelos, mostrar_modelos_completados
diseños_no_imprimidos = ['coche', 'avión', 'barco']
modelos_completados = []
imprimir_modelos(diseños_no_imprimidos, modelos_completados)
mostrar_modelos_completados(modelos_completados)

from printing_models import imprimir_modelos as im, mostrar_modelos_completados as mmc
diseños_no_imprimidos = ['coche', 'avión', 'barco']
modelos_completados = []
im(diseños_no_imprimidos, modelos_completados)
mmc(modelos_completados)

import printing_models as pm
diseños_no_imprimidos = ['coche', 'avión', 'barco']
modelos_completados = []
pm.imprimir_modelos(diseños_no_imprimidos, modelos_completados)
pm.mostrar_modelos_completados(modelos_completados)

from printing_models import *
diseños_no_imprimidos = ['coche', 'avión', 'barco']
modelos_completados = []
imprimir_modelos(diseños_no_imprimidos, modelos_completados)
mostrar_modelos_completados(modelos_completados)