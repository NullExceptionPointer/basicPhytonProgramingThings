my_hurra1 = 'Hip '*3 + ' ' + 'hurra'
print(my_hurra1)
my_hurra2 = f'{"Hip "*3} hurra'

#este ultimo caso se lo llama cadena de formato, que se identifica con la f al principio, lo que nos permite generar expresiones.
#la cadena de formato sirve para reemplazar la variable sobre la cadena.
print(my_hurra2)


#len() devuelve longitud de cadena.
print(len(my_hurra2))

#los corchetes me dejan elejir el caracter.
print(my_hurra2[0])

#a esto se lo conoce como notacion slicing
# my_hurra2[comienzo:final:pasos]
#se parece un for, no es inclusivo no cuenta el final.
print(my_hurra2[3:5])

#comienza del 0 pero termina en los ultimos 6
print(my_hurra2[:-6])

#podemos ir saltando de a 2 caracteres.
print(my_hurra2[::2])

