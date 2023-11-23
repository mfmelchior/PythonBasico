print('***************************************************************************************')
print('Olá, digite uma temperatura em Celsius que irei converter para Fahrenheit e vice-versa!')
print('***************************************************************************************')
while True:
    t = float(input('Digite a temperatura: ')) #pede a temperatura
    u = input('Digite a unidade original (Celsius(C) ou Fahrenheit(F)): ') # qual unidade original

    if u.lower() == 'f': #deixa a unidade minuscula e ve se é f
        r= (t-32)* (5/9) #se for f faz a conta de Fahrenheit para celsius
        print(f'A temperatura em Celsius é {r}°C') #retorna o valor em celsius
        break #encerra o laço
    elif u.lower() == 'c': #deixa a unidade minuscula e ve se é c
        r = (t * 9/5) + 32  #se for f faz a conta de celsius para Fahrenheit
        print(f'A temperatura em Fahrenheit é {r}°F') #retorna o valor em Fahrenheit
        break #encerra o laço
    else: #se colocar algo inválido
        print('Inválido') # mostra que foi inválido
        continue # continua o laço
