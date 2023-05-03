// osnovni tipovi
// fiksno polje
// obraditi sting na razini literala
// osnovni pointeri
// console IO
#include <iostream>
#include <array>


// ALL KINDS OF DECLARATIONS
// Most used declarations
using namespace std;

// Basic types
// Function
// Templates    
// Constexpr
// Type alias
// Type name
// Enum
// Namespace
// Auto
// Struct
// Class
// Union


char ch;
string s;

auto count = 1;

const double pi = 3.1415926535897;

extern int error_number;

const char* name = "Njal";
const char* season[] = { "spring", "summer", "fall", "winter" };

//vector<string> people{ name, "Skarphedin", "Gunnar" };

struct Date { int d, m, y; };

int day(Date* p) { return p->d; }

double sqrt(double);

template<class T> T abs(T a) { return a<0 ? -a : a; }

constexpr int fac(int n) { return (n<2) ? 1 : n*fac(n-1); }		// possible compile-time evaluation
constexpr double zz{ pi*fac(7) };								// compile-time initialization

//using Cmplx = std::complex<double>;		// type alias

struct User;							// type name

enum class Beer { Carlsberg, Tuborg, Thor };

namespace NS { int a; }

// auto
// template<class T> void f1(vector<T>& arg)
// {
// 	for (vector<T>::iterator p = arg.begin(); p != arg.end(); ++p)
// 		∗p = 7;
// 	for (auto p = arg.begin(); p != arg.end(); ++p)
// 		∗p = 7;
// }	

// void f(vector<int>& v)
// {
// 	for (const auto& x : v) { // x is a const int&
// 							  // ...
// 	}
// }

void test_bool()
{
	bool b1 = 7;		// 7!=0, so b becomes true
	//bool b2{ 7 };		// ERROR : narrowing (§2.2.2, §10.5)
	int i1 = true;		// i1 becomes 1
	int i2{ true };		// i2 becomes 1

	// In arithmetic and logical expressions, bools are converted to ints; integer arithmetic and logical
	// operations are performed on the converted values.If the result needs to be converted back to bool,
	// a 0 is converted to false and a nonzero value is converted to true.For example :
	bool a = true;
	bool b = true;
	bool x = a + b;     // a+b is 2, so x becomes true
	bool y = a || b;    // a||b is 1, so y becomes true ("||" means "or")
	bool z = a - b;     // a-b is 0, so z becomes false
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// char
void test_char()
{
	char c = 255;					// 255 is ‘‘all ones,’ ’ hexadecimal 0xFF
	int	 i = c;
	char c2 = 'x';				// assigns 120 (ASCII for 'x')
	char ascii = u8'x';		// use UTF-8 encoding

	//const wchar_t * wstr_bad = L"\UD840DC8A";			// ERROR, invalid character
	const wchar_t * wstr_good = L"\U0002008A";		// Okay, UCN is valid code point

	signed char sc = -160;
	unsigned char uc = sc;		// uc == 116 (because 256-160==116)
	std::cout << uc;								// print 't'

	char count[256];		    // assume 8-bit chars
	++count[sc];				// likely disaster: out-of-range access
	++count[uc];				// OK

	auto s1 = "folder\\file";			// implementation character set string
	auto s2 = R"(folder\file)";			// implementation character raw set string
	auto s3 = u8"folder\\file";			// UTF-8 string
	auto s4 = u8R"(folder\file)";		// UTF-8 raw str ing
	auto s5 = u"folder\\file";			// UTF-16 string
	auto s6 = uR"(folder\file)";		// UTF-16 raw str ing
	auto s7 = U"folder\\file";			// UTF-32 string
	auto s8 = UR"(folder\file)";		// UTF-32 raw str ing
}

void test_int()
{
	char	myChar = 0;			// -128 to +127
	short 	myShort = 0;		// -32768 to +32767
	int		myInt = 0;			// -2^31 to +2^31-1
	long	myLong = 0;			// -2^31 to +2^31-1
	long long myL2 = 0;		// -2^63 to +2^63-1

	signed char		myCharSigned = 0;			// -128 to +127
	signed short	myShortSigned = 0;		// -32768 to +32767
	signed int		myIntSigned = 0;			// -2^31 to +2^31-1
	signed long		myLongSigned = 0;			// -2^31 to +2^31-1
	signed long long myL2Signed = 0;		// -2^63 to +2^63-1

	unsigned char		myCharUnsigned = 0;			// 0 to 255
	unsigned short		myShortUnsigned = 0;		// 0 to 65535
	unsigned int		myIntUnsigned = 0;			// 0 to 2^32-1
	unsigned long		myLongUnsigned = 0;			// 0 to 2^32-1
	unsigned long long 	myL2Unsigned = 0;		// 0 to 2^64-1

	int8_t	myInt8	= 0;	// 8 bits
	int16_t myInt16 = 0;	// 16 bits
	int32_t myInt32 = 0;	// 32 bits
	int64_t myInt64 = 0;	// 64 bits

	std::cout	<< sizeof(myChar)		// 1 byte (per definition)
				<< sizeof(myShort)		// 2
				<< sizeof(myInt)		// 4
				<< sizeof(myLong)		// 4
				<< sizeof(myL2);		// 8

	// numerički literali
	int i = 10;
	long l = 10L;
	unsigned long ul = 10UL;

	int myOct = 062;			// octal notation (0)
	int myHex = 0x32;			// hexadecimal notation (0x)
	int myBin = 0b0011'0010;	// binary notation (0b)
    }

int test_real()
{
	float f = 1.23F;
	double d = 1.23;
	long double ld = 1.23L;

    // TODO - dodati osnovni output preko std::cout

	return 0;
}

void standard_cpp_arrays()
{

}

void stl_arrays()
{
	std::array<double, 100> data;
	std::array<double, 10>  values{ 0.5, 1.0, 1.5, 2.0 };

	values.fill(3.1415926);

	// pristup s operatorom [] - NO BOUNDS CHECKING
	values[4] = values[3] + 2.0*values[1];

	// pristup s at() - obavlja se bounds checking
	values.at(4) = values.at(3) + 2.0*values.at(1);

	// ima i size() funkciju
	double total{};
	for (size_t i{}; i < values.size(); ++i)
	{
		total += values[i];
	}

	// možemo koristiti i ranged for petlju
	double total2{};
	for (auto& value : values)
		total2 += value;
}
