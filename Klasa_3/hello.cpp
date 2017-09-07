/*
 * hello.cpp
 * 
 * 
 */

using namespace std;
#include <iostream>
#define ROK_TERAZ 2017

int main(int argc, char **argv)
{
    string imie;
    int wiek;
	cout << "Cześć, jak masz na imię?" << endl;
    cin >> imie; 
    cout << "Witaj " << imie << endl;
    cout << "Ile masz lat?" << endl;
    cin >> wiek;
    cout << "Urodziłeś/aś się w " << ROK_TERAZ - wiek << endl;
    
	return 0;
}

