import sqlite3



def bacamobilanjay(FILEDB):
    koneksidb = sqlite3.connect(FILEDB)
    koneksidb.row_factory = sqlite3.Row
    rows = koneksidb.execute("SELECT * FROM TBCarsweb").fetchall()
    koneksidb.close()
    return [dict(row) for row in rows]


