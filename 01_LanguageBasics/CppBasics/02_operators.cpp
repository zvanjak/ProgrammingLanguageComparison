#include "stdafx.h"


void bitwise_operators()
{
	int x = 5 & 4; // 101 & 100 = 100 (4) // and
	x = 5 | 4; // 101 | 100 = 101 (5) // or
	x = 5 ^ 4; // 101 ^ 100 = 001 (1) // xor
	x = 4 << 1; // 100 << 1 =1000 (8) // left shift
	x = 4 >> 1; // 100 >> 1 = 10 (2) // right shift
	x = ~4; // ~00000100 = 11111011 (-5) // invert
}
