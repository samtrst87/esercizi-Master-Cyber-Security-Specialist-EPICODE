
/* RICHIESTA
Lo scopo di oggi sarà realizzare due programmi in C , scriva un programma che esegua l'operazione di moltiplicazione tra due numeri inseriti dall'utente. 
Opzionale: 2 - Si scriva un programma in linguaggio C che legga due valori interi e visualizzi la loro media aritmetica. 
*/

/* Ho utilizzato  i Switch per creare una scelta dell'operazione in modo da unificare i due esercizi
*/ 
#include <stdio.h>

int main(){

int scelta;
printf("\nDigita 1 per selezionare l'operazione moltiplicazione tra due numeri");
printf("\nDigita 2 per selezionare la media aritmetica tra due numeri");
printf("\n ");
scanf("%d", &scelta);
switch (scelta)
{
    case 1:
    int input1, input2, moltiplicazione;

    printf("Calcolo della moltiplicazione!");

    printf("\nInserisci il primo numero: ");
    scanf("%d", &input1);

    printf("\nInserisci un secondo numero: ");
    scanf("%d", &input2);

    moltiplicazione = input1 * input2;
    printf("\nIl risultato della moltiplicazione e': %d", moltiplicazione);
    break;

    case 2:
    float input3, input4, media;

        printf("\nInserisci il primo numero: ");
    scanf("%f", &input3);

    printf("\nInserisci un secondo numero: ");
    scanf("%f", &input4);

    media = (input3 + input4)/2;
    printf("\nLa media dei due numeri e': %f", media);
    break;

    default:
    printf("\nHai selezionato un opzione non valida, che insolenza!");
    break;
}
return 0;
}