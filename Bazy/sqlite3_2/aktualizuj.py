#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  baza_sql.py

import sqlite3

def wyniki(cur):
    wyniki = cur.fetchall()
    for row in wyniki:
        print(tuple(row))

def dodaj(cur):
    cur.execute ("""
        INSERT INTO tbKlasy
        VALUES (?, ?, ?, ?)
    """, [None, '1B', 2017, 2020])
    
def aktualizuj(cur):
    cur.execute ("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE klasa = ? AND roknaboru = ?
    """, ['1D', '1B', 2017])


def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor()  # utworzenie kursora
    con.row_factory = squlite3.Row
    #dodaj(cur)
    aktualizuj(cur)
    con.commit() 
    wyniki(cur.execute('SELECT * FROM tbKlasy'))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
