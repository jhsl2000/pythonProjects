from random import randrange
numero_rand =(randrange(100))
print(randrange(100))


numero_1 = input('Guess the number: ')



numero_1 = int(numero_1)

#adicionar codigo para fornecer dicas

if (numero_1 != numero_rand):
    print('Numero errado')