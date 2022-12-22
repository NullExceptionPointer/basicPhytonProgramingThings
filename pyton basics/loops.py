nombres = ['lucas', 'isaac', 'soto']

contador = 0
while contador < 4:
    print(contador)
    contador += 1


#esto se parece a un foreach
# la forma en la que funciona es la siguiente, teniendo un objeto el cual es iterable, como se si es iterable porque uso, iter() y este devuelve el iterador,
#una vez tengo el iterador yo puedo darle a next(iterador)
#y me da el siguiente elemento ya que iterador guarda el estado de quien sigue.
for name in nombres:
    print(name)

#para simular el for clasico se usa range()
#range(stop)
#range(start, stop)
#range(start, stop, step)
for i in range(0,10,1):
    print(i)