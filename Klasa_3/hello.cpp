/*
 * hello.cpp
 * 
 * 
 */

using namespace std;
#include <iostream>
#define ROK_TERAZ 2017
#define ROK_CPP 1983

int parzyste (int n ){

    int i;
    for (i = 0; i <= n; i += 2)
    cout << i << " ";
    return i / 2;
}

int main(int argc, char **argv)
{
    string imie;
    int wiek, rok_urodzenia;
	cout << "Cześć, jak masz na imię?" << endl;
    cin >> imie; 
    cout << "Witaj " << imie << endl;
    cout << "Ile masz lat?" << endl;
    cin >> wiek;
    rok_urodzenia = ROK_TERAZ - wiek;
    cout << "Urodziłeś/aś się w " << rok_urodzenia << endl;
    if (ROK_CPP > rok_urodzenia){
        cout << "Jesteś ode mnie starszy!" << endl;}
    else if (ROK_CPP < rok_urodzenia){
        cout << "Jesteś ode mnie młodszy!" << endl;}
    else if (ROK_CPP == rok_urodzenia){
        cout << "Jesteśmy w tym samym wieku!" << endl;}
        
    int n;
    cout << "Podaj liczbę naturalną: ";
    cin >> n;
    parzyste(n);
    cout << endl;
    cout << "Ilość parzystych: ";
    
	return 0;
}

