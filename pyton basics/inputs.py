#funcion inputs sirve para tomar datos de entrada.
# podemops ver que incluso podemos mostrarle un mensaje
nombre = input('Cual es tu nombre: ')
print(len(nombre))

print(f'Tu nombre es {nombre}')

#podemos ver que aunbque le pedimos un numero, este lo guarda como una cadena, entonces puede generar errores.
numero = input('Ingrese un numero: ')
print(numero)
print(type(numero))

#para poder tenerlo como un numero hay que castearlo.
numero = int (input('Ingrese un numero: '))
print(numero)
print(type(numero))
