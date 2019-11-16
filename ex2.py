'''Faça um programa que receba dois inputs, uma palavra/frase
e uma letra. O programa deve retornar quantas vezes a letra apareceu
na palavra/frase. Dica: contagem de valores .count('valor')'''

def contar_letra():
    palavra = input("Digite um palavra")
    letra = input("Digite a letra que deseja contar na palavra")
    return palavra.count(letra)

#JEITO MAIS COMPLETO COM VALIDAÇÃO PARA UMA LETRA
def contar_letra2():
    palavra = input("Digite um palavra")
    letra = input("Digite a letra que deseja contar na palavra")
    while len(letra) > 1:
        letra = input("Digite a letra que deseja contar na palavra")
    return palavra.count(letra)
print(contar_letra2())