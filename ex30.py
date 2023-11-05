from random import randint
lista = {randint(1,1000) for _ in range(40)}
par = 0
impar = 0
for i in lista:
    if i % 2 == 0:
        par+=i
    else:
        impar+=i
print('par: ',par)
print('impar: ',impar)
print('valores: ', lista) 
