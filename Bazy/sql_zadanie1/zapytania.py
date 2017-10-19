#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3

def kw_c(cur):
    cur.execute ("""
        SELECT siedziba, SUM(placa) AS pensje FROM dzial, pracownicy
        WHERE dzial.id = pracownicy.id_dzial
        GROUP BY siedziba 
        ORDER BY pensje ASC
    """)
    
    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(tuple(rekord))

def kw_d(cur):
    parametr = input('Podaj nazwę działu: ')
    # parametr2 = input('Kobiety czy mężczyźni? ')
    cur.execute ("""
        SELECT dzial.id, dzial.nazwa, nazwisko, imie FROM dzial, pracownicy 
        WHERE dzial.id = pracownicy.id_dzial
        AND dzial.nazwa = ?
        AND imie NOT LIKE '%a' 
    """, (parametr,))
    
    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(tuple(rekord))

def kw_e(cur):
    cur.execute ("""
        SELECT nazwisko, stanowisko, placa * premia.premia FROM pracownicy, premia
        WHERE  premia.id = pracownicy.stanowisko
    """)
    
    wyniki = cur.fetchall()
    for rekord in wyniki:
        print(tuple(rekord))

def main(args):
    con = sqlite3.connect('pracownicy.sqlite3')
    cur = con.cursor()  # utworzenie kursora
    #kw_c(cur)
    #kw_d(cur)
    kw_e(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
