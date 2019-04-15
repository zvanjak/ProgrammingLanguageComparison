// Cpp_HiLo_Game.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>

#include <stdio.h>
#include<stdlib.h>

#include<time.h>

int main()
{
	int broj, hilo, pom, min = 0, max = 1000, br_koraka = 0;
	srand((unsigned)(time(NULL)));

	printf("Zamislite broj od 1 do 1000.\n");
	printf("\n");
	printf("Upisite 1 ako je ispisani broj veci od zamisljenog, 0 ako je manji ili 5 ako je to zamisljeni broj.\n");
	printf("\n");
	broj = rand() % (1000 - 0 + 1) + 0;

	while (1)
	{
		printf("%d\n", broj);
		scanf("%d", &hilo);
		if (hilo == 1)
		{
			if (broj > min)min = broj;
			pom = (max - min) / 2;
			broj = pom + broj;
		}
		else if (hilo == 0)
		{
			if (broj < max)max = broj;
			pom = (max - min) / 2;
			broj = broj - pom;
		}
		else if (hilo == 5)
			break;

		else
		{
			br_koraka--;
			printf("Upisite ponovno.\n");
		}
		br_koraka++;
	}
	printf("Zamisljeni broj je %d. :)\n", broj);
	printf("Broj koraka: %d.\n", br_koraka);

	return 0;
}
