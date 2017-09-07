#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello.py
#  
#  

ROK_TERAZ = 2017
ROK_PYTHON = 1991

def parzyste(n):
    ile = list(range(0, n+1, 2))
    print (ile)
    return len(ile)

def main(args):
    imie = input("Jak masz na imię? ")
    print("Witaj", imie)
    wiek = int(input("Ile masz lat? "))
    rok_urodzenia = ROK_TERAZ - wiek
    print("Urodziłeś/aś sie w " , rok_urodzenia)
    if ROK_PYTHON > rok_urodzenia:
        print("Jesteś ode mnie starszy!")
    elif ROK_PYTHON < rok_urodzenia:
        print ("Jesteś ode mnie młodszy!")
    elif ROK_PYTHON == rok_urodzenia:
        print("Jesteśmy w tym samym wieku!") 
        
    n = int(input("Podaj liczbe naturalną: "))
    print('Ilość parzystych: ', parzyste(n))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
