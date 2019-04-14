// Zad 02 - Inheritance.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <complex>
#include <iostream>

using std::cout;
using std::complex;

class CComplex {
public:
	double _re, _im;
	CComplex(double inRe) : _re(inRe), _im(0.0) {}
};

class Base {
public:
	void g(int) { cout << "Base::g(int)\n"; }

	virtual void f( int ) { cout << "Base::f(int)\n"; }
	virtual void f( double ) { cout << "Base::f(double)\n"; }
};

class Derived : public Base {
public:
	void g(double) { cout << "Derived::g(double)\n"; }

//	void f(double a) { cout << "Derived::f(double)\n"; }
	void f(CComplex) { cout << "Derived::f(complex)\n"; }
};

int _tmain(int argc, _TCHAR* argv[])
{
	Derived	d;
	Base 	*pb = new Derived;

	d.f(1);			
	d.f(1.0);
	d.g(1);
	d.g(1.0);

	cout << std::endl;

	pb->f(1);
	pb->f(1.0);
	pb->g(1);
	pb->g(1.0);

	return 0;
}

