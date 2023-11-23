import random #importa biblioteca random
numero_aleatorio = random.randint(1, 100) #gera um numero aleatorio

while True:
    chute = int(input('Tente adivinhar o número sorteado entre 1 e 100: ')) #pede o seu chute
    if chute > numero_aleatorio: #se o chute for maior que o numero aleatorio
        print('O número sorteado é menor. Tente novamente') #da uma dica
        continue #continua o laço
    elif chute < numero_aleatorio: # se o chute for menor que o numero gerado
        print('O número sorteado é maior. Tente novamente') #da uma dica
        continue #continua o laço
    elif chute == numero_aleatorio: #se o chute for o mesmo do numero gerado aleatorio
        print('Parabéns! Você acertou o número sorteado!') #print parabens
        break #encerra o laço