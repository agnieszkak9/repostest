#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  hello.py
#  
#  

ROK_TERAZ = 2017

def main(args):
    imie = input("Jak masz na imię? ")
    print("Witaj", imie)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
