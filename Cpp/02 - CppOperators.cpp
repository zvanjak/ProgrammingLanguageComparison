// osnovni operatori


#include <vector>
#include <string>

using std::string;
using std::vector;

// konverzije
void conversions()
{
	double d = 1.0;
	char c = d;		// VS - warning C4244: 'initializing': conversion from 'double' to 'char'
					// possible loss of data
}

void conversions2()
{
	double d = 1.0;
	//char c {d};		// VS - error C2397: conversion from 'double' to 'char' requires a narrowing conversion
}

void bitwise_operators()
{
	int x = 5 & 4; // 101 & 100 = 100 (4) // and
	x = 5 | 4; // 101 | 100 = 101 (5) // or
	x = 5 ^ 4; // 101 ^ 100 = 001 (1) // xor
	x = 4 << 1; // 100 << 1 =1000 (8) // left shift
	x = 4 >> 1; // 100 >> 1 = 10 (2) // right shift
	x = ~4; // ~00000100 = 11111011 (-5) // invert
}

int f(int, int)
{
	return 0;
}

void prioriteti1()
{
	int a, b, c, d;
	int *pb, *pd;
	int x;
	int i;
	int p[5][5];

	a = b + c * d << 2 & 8;
	a & 077 != 3;
	a == b || a == c && c < 5;
	c = x != 0;
	0 <= i < 7;
	f(1, 2) + 3;
	a = -1 + +b -- - 5;
	a = b == c++;
	a = b = c = 0;
	p[4][2] *= * pb ? c : * pd * 2;
	a-b, c = d;
}

class A
{
public:
	int m;
};

void prioriteti2()
{
	A *pc;
	int *p;
	int a;
	int i;
	int *b;

	*p++;
	*--p;
	//++a--;      // ERROR - expression must be a modifiable lvalue
	(int*)pc->m;
	(*pc).m;
	//*b[i];        //  ERROR
}