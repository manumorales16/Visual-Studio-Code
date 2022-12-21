"""
  3 maneras de redondear números en Python

  @author parzibyte
"""
# Si usas ceil y floor importa a math
import math

numero = 1.4
redondeado = round(numero)
redondeado_abajo = math.floor(numero)
redondeado_arriba = math.ceil(numero)
print("Redondeado con round: {}".format(redondeado))
print("Redondeado con floor (hacia abajo): {}".format(redondeado_abajo))
print("Redondeado con ceil (hacia arriba): {}".format(redondeado_arriba))

# Otro ejemplo con round
numero = 1.5
redondeado = round(numero)
print("round(1.5): {}".format(redondeado))