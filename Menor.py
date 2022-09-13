#******************************************************************************
#                               Menor Valor e Posicao.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;

tamanho = 0
numeros = 0
lista = []
num = 0
num2 = num+1
tamanho = int(input())

if(tamanho>1 and tamanho<1000):
    while(len(lista)<tamanho):
        lista = input().split(" ")

valores = []
for val in lista:
    valores.append(int(val))

final = len(lista)

posicao = valores.index(min(valores))
print("Menor valor: {}".format(min(valores)))
print("Posicao: {}".format(posicao))