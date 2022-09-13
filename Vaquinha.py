#******************************************************************************
#                               Vaquinha para Valqu�ria.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;

n = 1
lista = []
while(n>=0):
    n = float(input())
    if(n>=0):
        lista.append(n)

soma = sum(lista)
soma = float(soma)
if (len(lista)>0):
    media = soma/(len(lista))
elif (len(lista)==0):
    media = 0

print("%.2f" % soma)
print("%.2f" % media)