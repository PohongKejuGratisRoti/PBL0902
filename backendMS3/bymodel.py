import sqlite3
from typing import List, Dict

def carimodel(database, carmodel:str) -> List[Dict]:
    try:
        with sqlite3.connect(database) as koneksidb:
            koneksidb.row_factory = sqlite3.Row
            kursor = koneksidb.cursor()

            kursor.execute(
                "SELECT * FROM tbcarsweb WHERE carmodel LIKE ?", (f"%{carmodel}%",)
            )
            baris = kursor.fetchall()

            return [dict(row) for row in baris]
    except sqlite3.OperationalError as e:
        print("database tolol error lagi",e)
        return []

