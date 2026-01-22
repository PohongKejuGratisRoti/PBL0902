import sqlite3

komandosql = "DELETE FROM tbcarsweb WHERE id = ?"

def hapusberdasarid(id, Database):
    try:
        with sqlite3.connect(Database) as koneksi:
            kursor = koneksi.cursor()
            kursor.execute(komandosql, (id,))
            koneksi.commit()
            
            return kursor.rowcount
    except sqlite3.OperationalError as errortolol:
        print(errortolol)
        return -1

