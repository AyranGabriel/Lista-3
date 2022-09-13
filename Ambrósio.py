#******************************************************************************
#                               Ambrosio Romantico.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;

n = 0
e = 0
lista = []

#Tenho que transformacar em string para aceitar mais de um valor;
n, e = input().split(" ")
n = int(n)
e = int(e)

if(n>=1 and n<=1000)and(e>=1 and e<=1000):
    while(len(lista)<n):
        lista = input().split(" ")

valores = []
verificador = 0
global verdadeiro
verdadeiro = 0

for val in lista:
    valores.append(int(val))
    
def checagem(numero):
    global verdadeiro
    verdadeiro = 0
    verificador = 0
    for verificador in range(len(valores)):
        if (valores[verificador]+valores[numero])==e:
            if(verificador!=numero):
                #print(verificador)
                #print(valores[numero])
                verdadeiro=1
                break
        else:
            verdadeiro=0
            #print(verificador)


#Aqui esta certo;
for i in range(len(valores)):
    if valores[i]<e and verdadeiro!= 1:
        checagem(i)

if verdadeiro == 1:
    print('SIM')
elif verdadeiro == 0:
    print('NAO')