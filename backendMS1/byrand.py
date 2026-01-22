import sqlite3
from typing import List, Dict

def caripakebrand(datatbase, carbrand:str) -> List[Dict]:
    try:
        with sqlite3.connect(datatbase) as koneksidb:
            koneksidb.row_factory = sqlite3.Row
            kursor = koneksidb.cursor()

            kursor.execute(
                "SELECT * FROM tbcarsweb WHERE carbrand LIKE ?", (f"%{carbrand}%",)
            )
            baris = kursor.fetchall()

            return [dict(row) for row in baris]
    except sqlite3.OperationalError as e:
        print("database tolol error lagi",e)
        return []

