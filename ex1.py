'''Faça um programa que receba quatro número e mostre
a média entre os quatro.
    Dica: média = (n1 + n2 + n3 + n4)/4'''

def media():
    n1 = float(input("Digite o numero 1: "))
    n2 = float(input("Digite o numero 2: "))
    n3 = float(input("Digite o numero 3: "))
    n4 = float(input("Digite o numero 4: "))
    return (n1+n2+n3+n4)/4

def media2():
    i = 1
    soma = 0
    while i <= 4:
        soma += float(input("Digite um número: "))
        i += 1
    return soma/4