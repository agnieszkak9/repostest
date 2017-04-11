/*
 * zadanie_1.cxx
 *
 *
 *
 */

#include<iostream>
using namespace std;
int main(int argc, char **argv)
{
    cout << "Podaj słowo\n";
    string slowo;
    cin >> slowo;
    int x = slowo.length();
    cout << "Podany wyraz napisany wspak\n";
    for (int i = x; i >= 0; i--){
        cout << slowo[i];
    }
return 0;
}
