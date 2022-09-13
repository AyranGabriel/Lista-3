#******************************************************************************
#                               Monitorando A Glicose.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;

numero = -1
lista = []

#Loop;

while(numero != 0):
    numero = int(input())
    lista.append(numero)

soma_da_lista = sum(lista)
media = soma_da_lista/(len(lista)-1)

if(media<110):
    print('Glicose Normal')
elif(media>=200):
    print('Glicose Muito Alta')
else:
    print('Glicose Alterada')