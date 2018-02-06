#ifndef LISTA_HPP
#define LISTA_HPP

struct ELEMENT {
    int wartosc;
    ELEMENT *nastepny; 
};

class Lista {
    private:   //hermatyzacja danych
        ELEMENT *head;
        ELEMENT *tail;
    public:    // interfejs publiczny klasy - API klasy
        Lista(); //konstruktor
        ~Lista(); //dekonstruktor
        void Dodaj(int);
        void Wyswietl();
        bool Usun();
};
#endif
