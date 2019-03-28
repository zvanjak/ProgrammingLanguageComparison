// Zad 04 - Krizic-kruzic za 2 igraca.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<stdio.h>


#define KRIZIC 3*'X'
#define KRUZIC 3*'O'

int _tmain(int argc, _TCHAR* argv[])
{
	int i, j, brojac=0, x, y, k, zbroj1, zbroj2, zbroj3, zbroj4, zastavica=0;
	char matrica[3][3];
	
	printf("Igrate igru krizic-kruzic! Potrebno je unijeti koordinate polja u koje zelite staviti svoj znak. Prvi igrac ima znak krizic(X) a drugi kruzic(O). Indeksi redaka i stupaca se krecu od 0 do 2. Pobjednik je onaj koji uspije staviti 3 znaka u isti redak, isti stupac ili dijagonalno prije protivnika. Sretno!\n");
	for(i=0; i<3; i++){
		for(j=0; j<3; j++){
			matrica[i][j]='-';
			printf("%c", matrica[i][j]);
		}
		printf("\n");
	}
	printf("\n");

	while(1){
		printf("Krizic, unesite koordinate! X\n");
		printf("\n");
		k=0;
		do{	
			if(k) printf("Pogresne koordinate, unesite ponovno.\n"); 
			scanf("%d %d", &x, &y);
			k++;
		}while(x<0 && x>2 || x>2 && y>2 || matrica[x][y]!='-');
		
		for(i=0; i<3; i++){
			matrica[x][y]='X';
			for(j=0; j<3; j++){
				printf ("%c", matrica[i][j]);
			}
		printf("\n");
		}

		if(brojac>3) {
			i=0;
			zbroj3=0;
			zbroj4=0;
			while(i<3){
				zbroj1=0;
				zbroj2=0;
				for(j=0; j<3; j++){
					zbroj1=zbroj1+matrica[i][j];
					zbroj2=zbroj2+matrica[j][i];
					if(i==0) zbroj3=zbroj3+matrica[j][j];
					if(i+j==2) zbroj4=zbroj4+matrica[i][j];
				}
		
				if(zbroj1==KRIZIC || zbroj2==KRIZIC || zbroj3==KRIZIC || zbroj4==KRIZIC) {
					printf("Pobjednik je krizic! X\n");
					printf("\n");
					zastavica++;
					break;
				}
				i++;
			}
		}
		if(zastavica) break;
		brojac++;
		if(brojac==9) break;

		printf("Kruzic, unesite koordinate! O\n");
		printf("\n");
		k=0;
		do{	
			if(k) printf("Pogresne koordinate, unesite ponovno.\n"); 
			scanf("%d %d", &x, &y);
			k++;
		}while(x<0 && x>2 || x>2 && y>2 || matrica[x][y]!='-');
		
		matrica[x][y]='O';
		for(i=0; i<3; i++){
			for(j=0; j<3; j++){		
				printf("%c", matrica[i][j]);
			}
		printf("\n");
		}
	
		if(brojac>4){
			i=0;
			zbroj3=0;
			zbroj4=0;
			while(i<3){
				zbroj1=0;
				zbroj2=0;
				for(j=0; j<3; j++){
					zbroj1=zbroj1+matrica[i][j];
					zbroj2=zbroj2+matrica[j][i];
					if(i==0) zbroj3=zbroj3+matrica[j][j];
					if(i+j==2) zbroj4=zbroj4+matrica[i][j];
				}
		
				if(zbroj1==KRUZIC || zbroj2==KRUZIC || zbroj3==KRUZIC || zbroj4==KRUZIC) {
					printf("Pobjednik je kruzic! O\n");
					zastavica++;
					break;
				}
				i++;
			}
		}
		if (zastavica) break;
		brojac++;
	}	
	if(zastavica==0) printf("Nerijeseno!\n");
	return 0;
}