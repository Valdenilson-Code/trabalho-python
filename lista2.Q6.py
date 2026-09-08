# Desenvolva um programa que solicite ao usuário um número inteiro e exiba a tabuada desse número, de 1 até 10.

#solicitado um número inteiro ao usuário
numero = int (input("Digite um numero inteiro : "))

#repete a operaçao do 1 até o 10
for i in range(1,11):
    
    #calcula a multiplicação
    resultado = numero * i

    #exibe o resultado da tabuada 
    print(f"{numero} x {i} = {resultado}")