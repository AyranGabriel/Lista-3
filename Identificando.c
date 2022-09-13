#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
/******************************************************************************
                        Identificando chas.
                Irei definir void para retornar vazio.
******************************************************************************/
int main(void){
    
	// Declaracao das variaveis
	int tipo,A,B,C,D,E;
	int reposta,total;
	
	reposta,total=0;
	tipo=0;
	
    scanf("%d",&tipo);
    scanf("%d",&A);
    scanf("%d",&B);
    scanf("%d",&C);
    scanf("%d",&D);
    scanf("%d",&E);
    
    //Definindo o tipo de cha;
    if(tipo >= 1 && tipo <= 4){
        if(tipo == 1){
            reposta = 1;
        }
        if(tipo == 2){
            reposta = 2;
        }
        if(tipo == 3){
            reposta = 3;
        }
        if(tipo == 4){
            reposta = 4;
        }
    }
    
    //Quem ganhou;
    if((A >= 1 && A <= 4) && 
    (B >= 1 && B <= 4) && 
    (C >= 1 && C <= 4) && 
    (D >= 1 && D <= 4) &&
    (E >= 1 && E <= 4)){
        //Definindo condicao para 'A';
        if(A == reposta){
            total+=1;
        }
        if(B == reposta){
            total+=1;
        }
        if(C == reposta){
            total+=1;
        }
        if(D == reposta){
            total+=1;
        }
        if(E == reposta){
            total+=1;
        }
    }
    
    //Quantos ganharam;
	printf("%d",total);
}