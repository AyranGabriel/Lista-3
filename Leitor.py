#******************************************************************************
#                               Leitor Voraz.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;

maior_paginas_lida = 0
dias = 0
paginas = 0
total_paginas = 0
lista = []

#Tenho que transformacar em string para aceitar mais de um valor;
total_paginas = int(input())

while(dias!=7):
    paginas = int(input())
    lista.append(paginas)
    dias+=1

for i in range(len(lista)):
    if (lista[i]-lista[i-1])>maior_paginas_lida:
        maior_paginas_lida = (lista[i]-lista[i-1])

print(max(lista))
print(maior_paginas_lida)