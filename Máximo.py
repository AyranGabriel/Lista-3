#******************************************************************************
#                               M�ximo e M�nimo.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;

lista = []
n=0
numeros=0

#Tenho que transformacar em string para aceitar mais de um valor;
n = int(input())

while(len(lista)!=n):
    numeros = int(input())
    if numeros>0 and numeros<=1000:
        lista.append(int(numeros))

print("Maior: %d apareceu %d vezes" %(max(lista), lista.count(max(lista))))
print("Menor: %d apareceu %d vezes" %(min(lista), lista.count(min(lista))))