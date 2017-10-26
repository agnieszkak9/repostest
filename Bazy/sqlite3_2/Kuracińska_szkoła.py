#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3

def wyniki(dane):
    
    for rekord in dane:
        print(tuple(rekord))

def kw_a(cur):
    cur.execute ("""
            SELECT Imie, Nazwisko, Klasa
            FROM tbUczniowie, tbKlasy
            WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
            AND Klasa LIKE '1A'
    """)
    wyniki(cur.fetchall())
    
def kw_b(cur):
    cur.execute ("""
            SELECT MAX(EgzHum)
            FROM tbUczniowie
    """)
    wyniki(cur.fetchall())
    
def kw_c(cur):
    cur.execute ("""
            SELECT AVG(EgzMat)
            FROM tbUczniowie, tbKlasy
            WHERE tbUczniowie.KlasaID = tbKlasy.IDKlasy
            AND Klasa LIKE '1A'
    """)
    wyniki(cur.fetchall())
    
def kw_d(cur):
    cur.execute ("""
            SELECT Imie, Nazwisko, Ocena
            FROM tbUczniowie, tbOceny
            WHERE tbOceny.UczenID = tbUczniowie.IDUcznia
            AND Nazwisko LIKE 'Nowak'
    """)
    wyniki(cur.fetchall())
    
def kw_e(cur):
    cur.execute ("""
            SELECT AVG(Ocena)
            FROM tbPrzedmioty, tbOceny
            WHERE tbOceny.PrzedmiotID = tbPrzedmioty.IDPrzedmiotu
            AND Przedmiot LIKE 'Fizyka'
            AND Datad > '2012-10-01'
            AND Datad < '2012-10-31'
    """)
    wyniki(cur.fetchall())

def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor()  # utworzenie kursora
    kw_a(cur)
    kw_b(cur)
    kw_c(cur)
    kw_d(cur)
    kw_e(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
