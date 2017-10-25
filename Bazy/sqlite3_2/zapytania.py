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
    
def kw_c(cur)
    
def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor()  # utworzenie kursora
    kw_a(cur)
    kw_b(cur)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
