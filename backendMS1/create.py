import sqlite3

def tambahmobil(Database, carname, carbrand, carmodel, carprice):
    try:
        with sqlite3.connect(Database) as koneksidb:
            kursor = koneksidb.cursor()
            #insert ke table ah ah ahh
            kursor.execute(""" INSERT INTO tbcarsweb (carname, carbrand, carmodel, carprice) VALUES (?, ?, ?, ?) """, (carname, carbrand, carmodel, carprice))
            koneksidb.commit()
            return kursor.lastrowid #id dari db yang sudah di masukan
    except sqlite3.OperationalError as e:#tahan error anjeng
        print("ketololanmu adalah", e)
        return -1
        
