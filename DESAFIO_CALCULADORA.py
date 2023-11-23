# calculadora
import math #importa  a biblioteca de matemática

a= float(input('Digite o primeiro número:  ')) #pede o valor de a 
op = input('Digite a operação (+, -, /, *);  ') #pede a operação desejada
b= float(input('Digite o segundo número:  ')) #pede o valor de b

if op == '+': # se a operação for soma
    r= a+b #soma a e b
    print(r) #print resultado
elif op == '-': # se a operação for subtração
    r= a-b #subtrai a e b
    print(r) #print resultado
elif op == '/': # se a operação for  divisao
    r=a/b #divide a e b
    print(r) #print resultado
elif op == '*': # se a operação for multiplicacao
    r = a*b # multiplica a e b
    print(r) #print resultado
else: #se colocar uma operação invalida
    print ('Operação inválida') # diz que é operação inválida
    