#include "pch.h"

#include <vector>
#include <string>
#include <complex>

using namespace std;

char ch;
string s;

auto count = 1;

const double pi = 3.1415926535897;

extern int error_number;

const char* name = "Njal";
const char* season[] = { "spring", "summer", "fall", "winter" };

vector<string> people{ name, "Skarphedin", "Gunnar" };

struct Date { int d, m, y; };

int day(Date* p) { return p->d; }

double sqrt(double);

template<class T> T abs(T a) { return a<0 ? -a : a; }

constexpr int fac(int n) { return (n<2) ? 1 : n*fac(n-1); }		// possible compile-time evaluation
constexpr double zz{ pi*fac(7) };								// compile-time initialization

using Cmplx = std::complex<double>;		// type alias

struct User;							// type name

enum class Beer { Carlsberg, Tuborg, Thor };

namespace NS { int a; }

// auto
template<class T> void f1(vector<T>& arg)
{
	for (vector<T>::iterator p = arg.begin(); p != arg.end(); ++p)
		∗p = 7;
	for (auto p = arg.begin(); p != arg.end(); ++p)
		∗p = 7;
}	

void f(vector<int>& v)
{
	for (const auto& x : v) { // x is a const int&
							  // ...
	}
}

using namespace std;

////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// bool
bool greater(int a, int b) { return a > b; }

void test_bool()
{
	bool b1 = 7;		// 7!=0, so b becomes true
	bool b2{ 7 };		// error : narrowing (§2.2.2, §10.5)
	int i1 = true;		// i1 becomes 1
	int i2{ true };		// i2 becomes 1

	// In arithmetic and logical expressions, bools are converted to ints; integer arithmetic and logical
	// operations are performed on the converted values.If the result needs to be converted back to bool,
	// a 0 is converted to false and a nonzero value is converted to true.For example :
	bool a = true;
	bool b = true;
	bool x = a + b; // a+b is 2, so x becomes true
	bool y = a || b; // a||b is 1, so y becomes true ("||" means "or")
	bool z = a - b; // a-b is 0, so z becomes false
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// char
void test_char()
{
	char c = 255;			// 255 is ‘‘all ones,’ ’ hexadecimal 0xFF
	int	 i = c;
	char c2 = 'x';			// assigns 120 (ASCII for 'x')
	char ascii = u8'x';		// use UTF-8 encoding
	char uni = U'\UFADEBEEF';

	signed char sc = -160;
	unsigned char uc = sc;	// uc == 116 (because 256-160==116)
	cout << uc;				// print 't'

	char count[256];		// assume 8-bit chars
	++count[sc];			// likely disaster: out-of-range access
	++count[uc];			// OK
}


int main()
{
	char myChar = 0;		// -128 to +127
	short myShort = 0;		// -32768 to +32767
	int myInt = 0;			// -2^31 to +2^31-1
	long myLong = 0;		// -2^31 to +2^31-1
	long long myL2 = 0;		// -2^63 to +2^63-1

	signed char myChar = 0;			// -128 to +127
	signed short myShort = 0;		// -32768 to +32767
	signed int myInt = 0;			// -2^31 to +2^31-1
	signed long myLong = 0;			// -2^31 to +2^31-1
	signed long long myL2 = 0;		// -2^63 to +2^63-1

	unsigned char myChar = 0;		// 0 to 255
	unsigned short myShort = 0;		// 0 to 65535
	unsigned int myInt = 0;			// 0 to 2^32-1
	unsigned long myLong = 0;		// 0 to 2^32-1
	unsigned long long myL2 = 0;	// 0 to 2^64-1

	int8_t myInt8 = 0;		// 8 bits
	int16_t myInt16 = 0;	// 16 bits
	int32_t myInt32 = 0;	// 32 bits
	int64_t myInt64 = 0;	// 64 bits

	cout << sizeof(myChar) // 1 byte (per definition)
		<< sizeof(myShort) // 2
		<< sizeof(myInt) // 4
		<< sizeof(myLong) // 4
		<< sizeof(myL2); // 8

	// numerički literali
	int i = 10;
	long l = 10L;
	unsigned long ul = 10UL;

	int myOct = 062;			// octal notation (0)
	int myHex = 0x32;			// hexadecimal notation (0x)
	int myBin = 0b0011'0010;	// binary notation (0b)

	float f = 1.23F;
	double d = 1.23;
	long double ld = 1.23L;

	return 0;
}