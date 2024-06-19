import sqlite3
import pandas as pd

from model.mod_classes import Stock, Stocks


def get_connexion():
    conn = sqlite3.connect('./data/stocks.dbf')
    return conn


def fermer_connexion(conn):
    conn.close()


def get_curseur(conn):
    curseur = conn.cursor()
    return curseur


def create_table():

    cde_ddl = '''create table if not exists STOCK (
    id integer primary key autoincrement,
    symbol text,
    company text,
    price float,
    date text,
    comment text,
    prev_close float,
    avg_volume float)
    '''
    conn = get_connexion()
    curseur = get_curseur(conn)
    curseur.execute(cde_ddl)
    fermer_connexion(conn)


def create(stock: Stock):
    cde_ins = 'insert into STOCK(symbol, company, price, date, comment, prev_close, avg_volume) values (?,?,?,?,?,?,?)'
    conn = get_connexion()
    curseur = get_curseur(conn)
    curseur.execute(cde_ins, [stock.symbol, stock.company, stock.price, stock.date, stock.comment, stock.prev_close,
                              stock.avg_volume])
    conn.commit()
    fermer_connexion(conn)


def create(stocks: Stocks):
    create_table()
    cde_ins = 'insert into STOCK(symbol, company, price, date, comment, prev_close, avg_volume) values (?,?,?,?,?,?,?)'
    conn = get_connexion()
    curseur = get_curseur(conn)

    for stock in stocks.listing:
        curseur.execute(cde_ins, [stock.symbol, stock.company, stock.price, stock.date, stock.comment, stock.prev_close,
                                  stock.avg_volume])
    conn.commit()
    fermer_connexion(conn)

#add read_all et read by_symbol
