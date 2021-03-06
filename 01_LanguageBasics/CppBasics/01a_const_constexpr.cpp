// Theme_1_02_Operatori_i_izrazi.cpp : Defines the entry point for the console application.
//

#include "pch.h"

#include <vector>
#include <string>

using std::string;
using std::vector;

constexpr double square(double x) { return x * x; }

void konstante()
{
	const int dmv = 17; 		// dmv is a named constant
	int var = 17; 				// var is not a constant
	
	constexpr double max1 = 1.4 * square(dmv); 	// OK if square(17) is a constant expression
	constexpr double max2 = 1.4 * square(var); 	// error : var is not a constant expression
	const double max3 = 1.4 * square(var);			// OK, may be evaluated at run tim  
			
	double sum(const vector<double>&); 		// sum will not modify its argument (§2.2.5)
	vector<double> v {1.2, 3.4, 4.5}; 			// v is not a constant
	const double s1 = sum(v); 					// OK: evaluated at run time
	constexpr double s2 = sum(v);				// error : sum(v) not constant expression 
}

// constexpr
int x1 = 7;
constexpr int x2 = 7;
constexpr int x3 = x1;		// error : initializer is not a constant expression
constexpr int x4 = x2;		// OK

void f()
{
	constexpr int y3 = x1;	// error : initializer is not a constant expression
	constexpr int y4 = x2;	// OK
							// ...
}

// const i constexpr
const int x		= 7;
const string s	= "asdf";
const int y		= sqrt(x);

constexpr int xx	= x;		// OK
constexpr string ss = s;		// error : s is not a constant expression			(string nije "literal type"!)
constexpr int yy	= y;		// error : sqrt(x) is not a constant expression		(sqrt nije constexpr funkcije)

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
	char c {d};		// VS - error C2397: conversion from 'double' to 'char' 
					// requires a narrowing conversion
}
