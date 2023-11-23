def contar_letras(texto): #define a função de contar letras e define um texto como parametro
    contagem_letras ={} #inicia um dicionario vazio
    for letra in texto: #para cada letra no texto recebido
        if letra.isalpha():  # Verifica se é uma letra do alfabeto
            if letra.lower() in contagem_letras: #deixa as letras todas iguais minusculas e ve se a letra ja ta no dicionario
                contagem_letras[letra.lower()] += 1 #se a letra ja tove no dicionario adiciona 1 
            else: #se a letra nao tive no dicionario
                contagem_letras[letra.lower()] = 1 # adiciona a letra e conta 1
    return contagem_letras #retorna o dicionario final

# Exemplo de uso da função
resultado = contar_letras("Hello World")
print(resultado)