'''Faça um programa que receba quantos números terá no cálculo da média
e retorne a média deles. 
    Exemplo: "Quantos números: 10" -> (n1+n2+...+n10)/10
            "Quantos números: 5" -> (n1+n2+n3+...+n5)/5
            DICA: podemos usar estruturas de repetição... tipo o for...
            e definir o range... :)'''

def calcular_media():
    qtd_numeros = int(input("Digite quantos numeros que deseja fazer a media: "))
    contador = 0
    soma = 0
    while contador < qtd_numeros:
        soma += float(input("Digite o número: "))
    return soma/qtd_numeros