// Zad 04a - Krizic-kruzic za 2 igraca.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <stdio.h>

void	Ispisi(int polja[]);
void	UnesiKoordinate(int polja[], int KoIgra);
int		ProvjeriNiz(int polja[], int KoIgra);

const int	PraznoPolje = 0;
const int	Krizic = 1;
const int	Kruzic = 2;

int _tmain(int argc, _TCHAR* argv[])
{
	int		polja[3][3] = { PraznoPolje };			// inicijaliziramo cijelo polje

	printf("\nIgra križiæ-kružiæ\n");

	Ispisi(polja[0]);

	while(1) {
		// igra Križiæ
		printf("\nKrižiæ - unesi koordinate: ");
		UnesiKoordinate(polja[0], Krizic);

		Ispisi(polja[0]);

		if( ProvjeriNiz(polja[0], Krizic) == 1 ) {
			printf("Pobjednik je Križiæ!!!");
			break;
		}

		// igra Kružiæ
		printf("\nKružiæ - unesi koordinate: ");
		UnesiKoordinate(polja[0], Kruzic);

		Ispisi(polja[0]);

		if( ProvjeriNiz(polja[0], Kruzic) == 1 ) {
			printf("Pobjednik je Kružiæ!!!");
			break;
		}
	}

	return 0;
}

void Ispisi(int polja[])
{
	for(int i=0; i<3; i++) {
		printf("\n-------");
		printf("\n|");

		for( int j=0; j<3; j++)  
		{
			if( polja[i*3+j] == Krizic ) printf("X|");
			else if( polja[i*3+j] == Kruzic ) printf("*|");
			else printf(" |");
		}
	}
	printf("\n-------");
}

void UnesiKoordinate(int polja[], int KoIgra)
{
	int x, y, flag;

	do {
		flag = 0;
		scanf("%d %d", &x, &y);

		if( x < 0 || x > 2 || y < 0 || y > 2 || polja[x*3 + y] != PraznoPolje ) {
			printf("\nUnesene krive koordinate. Pokušaj ponovo: ");
			flag = 1;
		}
	} while( flag == 1 );

	polja[x*3+y] = KoIgra;
}

// funkcija provjerava da li za igraèa definiranog parametrom KoIgra postoje tri u nizu
int ProvjeriNiz(int polja[], int KoIgra)
{
	// najprije provjerimo za tri vodoravno
	if( polja[0] == KoIgra && polja[1] == KoIgra && polja[2] == KoIgra ) return 1;
	if( polja[3] == KoIgra && polja[4] == KoIgra && polja[5] == KoIgra ) return 1;
	if( polja[6] == KoIgra && polja[7] == KoIgra && polja[8] == KoIgra ) return 1;

	// pa za tri okomito
	if( polja[0] == KoIgra && polja[3] == KoIgra && polja[6] == KoIgra ) return 1;
	if( polja[1] == KoIgra && polja[4] == KoIgra && polja[7] == KoIgra ) return 1;
	if( polja[2] == KoIgra && polja[5] == KoIgra && polja[8] == KoIgra ) return 1;

	// i na kraju dvije dijagonale
	if( polja[0] == KoIgra && polja[4] == KoIgra && polja[8] == KoIgra ) return 1;
	if( polja[2] == KoIgra && polja[4] == KoIgra && polja[6] == KoIgra ) return 1;

	return 0;
}