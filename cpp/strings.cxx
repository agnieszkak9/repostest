/*
 * strings.cxx
 *
 * Copyright 2017 user <user@lap79>
 */


#include <iostream>
#include <string>

using namespace std;

int main(int argc, char **argv)
{
	string tekst, szyfrogram, oszyfrowany;
    cout << "Podaj tekst do zaszyfrowania: " << endl;
    cin >> tekst;
    cout << tekst << endl << "Rozmiar: " << tekst.size() << endl;
    szyfrogram.resize(tekst.size());
    for(unsigned int i =0; i < tekst.size(); i++) {
        cout << tekst[i] << " ";
        szyfrogram[i] = zakodowany_znak;
    }
	return 0;
}

