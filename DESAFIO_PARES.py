def soma_pares(lista): #define a função chamada soma_pares que recebe como argumento uma lista
    pares=[] #inicia uma lista sem elementos para os numeros pares
    impares=[] #inicia uma lista sem elementos para os numeros impares
    for numero in lista:
        if numero % 2 == 0: #se o numero da lista for dividido por 2 e o resto for zero
            pares.append(numero) #entao adiciona esse nuemro a lista de pares
        else: #se o numero da lista for dividido por 2 e o resto nao for zero
            impares.append(numero)  #entao adiciona esse nuemro a lista de impares
    soma = sum(pares) #soma os elemtnso da lista de pares
    print(soma) #print da soma dos numeros da lista de pares

soma_pares([1,2,3,4,5,6,7,8,9,10]) #exemplo de chamada da função