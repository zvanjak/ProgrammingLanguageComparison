#include <iostream>

#include "hedley.h"

#include "declarations.h"

void CppBasics();
void CppOperators();
void CppStatements();
void CppFunctions();
void CppClasses();
void CppExceptions();
void CppStrings();
void CppFiles();
void Templates();
void DataContainers();
void Algorithms();

int main ()
{
    const wchar_t * wstr_good = L"\U0002008A";
    std::wstring b = L"🇺🇸🇷🇺🇸🇦";

    std::cout << "Hello " << wstr_good << " World!\n";
    std::wcout << "Hello " << b << " World!\n";
}