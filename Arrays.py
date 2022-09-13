#******************************************************************************
#                               Arrays de pares e �mpares.
#*****************************************************************************/
#*-* coding: utf-8 *-*

#Definindo variaveis;
contador = 0
n = 0
contador_impar=0
contador_par=0

lista = []
par = []
impar = []
par_comeca = 0
impar_comeca = 0

#Mudar para 
while(contador<15):

    n = int(input())
    lista.append(n)
    contador+=1

for i in range(len(lista)):
    #Colocando cada numero na sua repectiva lista;
    if (lista[i]%2) == 0:
        par.append(lista[i])
        if len(par)==5 and len(impar)<5:
            par_comeca = 1
    else:
        impar.append(lista[i])
        if len(impar)==5 and len(par)<5:
            impar_comeca = 1

#Primeiro Loop(par);
if len(par)!=0 and len(impar)!=0:
    #Se o par comecar;
    if par_comeca == 1:
        if len(par)>=5:
            for i in range(5):
                print("par[{}] = {}".format(i ,par[i]))
                contador_par+=1
        elif len(par)<5:
            for i in range(len(par)):
                print("par[{}] = {}".format(i ,par[i]))
                contador_par+=1
    #Se o par comecar:
    if impar_comeca != 1:
        if len(par)>=5 and contador_par==5:
            if len(impar)>=5:
                for i in range(5):
                    print("impar[{}] = {}".format(i ,impar[i]))
                    contador_impar+=1
            elif len(impar)<5:
                for i in range(len(impar)):
                    print("impar[{}] = {}".format(i ,impar[i]))
        #Condicao do len(par) ser menor que 5;
        if len(par)<5 and contador_par<5:
            if len(impar)>=5:
                for i in range(5):
                    print("impar[{}] = {}".format(i ,impar[i]))
                    contador_impar+=1
            elif len(impar)<5:
                for i in range(len(impar)):
                    print("impar[{}] = {}".format(i ,impar[i]))
#Condicao que nao existe impar;
if len(impar)==0:
    loop=0
    for i in range(len(par)):
        if loop == 5:
            loop=0
        print("par[{}] = {}".format(loop ,par[i]))
        loop+=1


            
#Primeiro Loop(impar);
if len(impar)!=0 and len(par)!=0:
    #Condicao do len(par) ser maior ou igual a 5;
    if impar_comeca == 1:
        if len(par)>=5:
            if len(impar)>=5:
                for i in range(5):
                    print("impar[{}] = {}".format(i ,impar[i]))
                    contador_impar+=1
            elif len(impar)<5:
                for i in range(len(impar)):
                    print("impar[{}] = {}".format(i ,impar[i]))
        #Condicao do len(par) ser menor que 5;
        if len(par)<5:
            if len(impar)>=5:
                for i in range(5):
                    print("impar[{}] = {}".format(i ,impar[i]))
                    contador_impar+=1
            elif len(impar)<5:
                for i in range(len(impar)):
                    print("impar[{}] = {}".format(i ,impar[i]))

    #Se o impar comeca:
    if par_comeca != 1:
        if contador_impar == 5:
            if len(par)>=5:
                for i in range(5):
                    print("par[{}] = {}".format(i ,par[i]))
                    contador_par+=1
            elif len(par)<5:
                for i in range(len(par)):
                    print("par[{}] = {}".format(i ,par[i]))
                    contador_par+=1
#Condicao que nao existe par;
if len(par)==0:
    loop=0
    for i in range(len(impar)):
        if loop == 5:
            loop=0
        print("impar[{}] = {}".format(loop ,impar[i]))
        loop+=1


#Segundo LOOP;
#Condicao para o impar continuar.
if len(impar)!=0 and len(par)!=0:
    if len(impar)>=5 and contador_impar==5 and len(impar)>=10:
        loop=0
        for i in range(5,10):
            print("impar[{}] = {}".format(loop ,impar[i]))
            loop+=1
    if len(impar)>=5 and contador_impar==5 and len(impar)<10:
        loop=0
        for i in range(5,len(impar)):
            print("impar[{}] = {}".format(loop ,impar[i]))
            loop+=1
#Condicao para o par continuar.
if len(par)!=0 and len(impar)!=0:
    if len(par)>=5 and contador_par==5 and len(par)>=10:
        loop=0
        for i in range(5,10):
            print("par[{}] = {}".format(loop ,par[i]))
            loop+=1
    if len(par)>=5 and contador_par==5 and len(par)<10:
        loop=0
        for i in range(5,len(par)):
            print("par[{}] = {}".format(loop ,par[i]))
            loop+=1

#Terceiro Loop;(Se os pares ou impares forem maiores que 10);
    #Par
    if len(par)>10 and len(impar)!=0:
        loop=0
        for i in range(10,len(par)):
            print("par[{}] = {}".format(loop ,par[i]))
            loop+=1
    #Impar
    if len(impar)>10 and len(par)!=0:
        loop=0
        for i in range(10,len(impar)):
            print("impar[{}] = {}".format(loop ,impar[i]))
            loop+=1