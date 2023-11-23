
while True: #inicia o laço
    nome = input('Digite seu nome: ') #pede o nome
    genero = input('Digite M para genero masculino e F para genero feminino: ') #pede o genero
    if genero.lower() == 'm': #se o genero for m 
        print('----------------------------------------------------------')
        print(f'******Olá, {nome}! Seja bem-vindo ao meu portifólio******') #saudação masculina
        print('----------------------------------------------------------')
        break #encerra o laço
    elif genero.lower() == 'f': #se o genero for f 
        print('----------------------------------------------------------')
        print(f'******Olá, {nome}! Seja bem-vindo ao meu portifólio******') #saudação feminina
        print('----------------------------------------------------------')
        break #encerra o laço
    else: #se digitar qlq outra coisa no genero 
        print('Genero invalido') #genero invalido
        continue #continua o laço
    