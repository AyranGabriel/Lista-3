#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
/******************************************************************************
                        Intervalo fechado crescente.
                Irei definir void para retornar vazio.
******************************************************************************/
int main(void){
    
	// Declaracao das variaveis
	int A,B;
	int Intervalo;
	
	A,B,Intervalo = 0;
	
    scanf("%d",&A);
    scanf("%d",&B);
    
    if(A <= B){
        for(Intervalo = A;Intervalo <= B;Intervalo++){
	    printf("%d\n",Intervalo);
        }
    }
}