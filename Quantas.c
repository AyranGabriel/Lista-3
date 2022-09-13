#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
/******************************************************************************
                        Quantas vezes x apareceu.
                Irei definir void para retornar vazio.
******************************************************************************/
int main(void){
    
	// Declaracao das variaveis
	int n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,x;
	int total;
	
	total = 0;
	n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,x = 0;
	
    scanf("%d",&n1);
    scanf("%d",&n2);
    scanf("%d",&n3);
    scanf("%d",&n4);
    scanf("%d",&n5);
    scanf("%d",&n6);
    scanf("%d",&n7);
    scanf("%d",&n8);
    scanf("%d",&n9);
    scanf("%d",&n10);
    scanf("%d",&x);
    
    if((n1 <= 1000 && n1 >= 0) &&
    (n2 <= 1000 && n2 >= 0) &&
    (n3 <= 1000 && n3 >= 0) &&
    (n4 <= 1000 && n4 >= 0) &&
    (n5 <= 1000 && n5 >= 0) &&
    (n6 <= 1000 && n6 >= 0) &&
    (n7 <= 1000 && n7 >= 0) &&
    (n8 <= 1000 && n8 >= 0) &&
    (n9 <= 1000 && n9 >= 0) &&
    (n10 <= 1000 && n10 >= 0)){
        if(x == n1){
            total+=1;
        }
        if(x == n2){
            total+=1;
        }
        if(x == n3){
            total+=1;
        }
        if(x == n4){
            total+=1;
        }
        if(x == n5){
            total+=1;
        }
        if(x == n6){
            total+=1;
        }
        if(x == n7){
            total+=1;
        }
        if(x == n8){
            total+=1;
        }
        if(x == n9){
            total+=1;
        }
        if(x == n10){
            total+=1;
        }
    }
    printf("%d",total);
}