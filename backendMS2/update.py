import sqlite3

# jangan lupa, nama tabel
komandosqlupdate = 'UPDATE tbcarsweb SET carname= ?, carbrand = ?, carmodel = ?, carprice = ? WHERE id = ?'

def updaterecord(database, id, carname, carbrand, carmodel, carprice):
    try:
        with sqlite3.connect(database) as koneksi:
            kursor = koneksi.cursor()
            kursor.execute(komandosqlupdate, (carname, carbrand, carmodel, carprice, id))
            koneksi.commit()
    except sqlite3.OperationalError as e:
        print("error tolol", e)



