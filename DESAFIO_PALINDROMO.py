def palindromo(palavra): #define a funcao palindromo que recebe como argumento uma palavra
    contra = palavra[::-1] # deixa a palavra ao contrario e nomeia como contra
    if contra == palavra: #se contra e palavra forem iguais
        print(f'{palavra} é um palíndromo!') #diz que é um palíndromo
    else: #se contra e a palavra não forem iguais
        print(f'{palavra} não é um palíndromo.') #diz que não é um palíndromo

palindromo('arara') #exemplo de uso da função
palindromo('cama') #exemplo de uso da função
palindromo(input('Digite uma palavra: ')) #chamando a função para o usuário escolher a palavra