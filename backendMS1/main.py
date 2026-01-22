from fastapi import FastAPI, Request, HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from read import bacamobilanjay
from delete import hapusberdasarid
from create import tambahmobil
from update import updaterecord 
from searchname import caripakenama
from byrand import caripakebrand
from bymodel import carimodel


from pathlib import Path
#konverrsi path ke base dir
BASE_DIR = Path(__file__).resolve().parent
# naik satu level, ribet  karena python dibuat sama monyet
DB1 = BASE_DIR.parent / "databases" / "carsweb1.db"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allow all origins (OK for dev)
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],
)
@app.post("/cars/fetch")
def fetch_cars(payload: dict = {}):
    # you could handle filtering here if you want
    return bacamobilanjay(DB1)


@app.post("/cars/delete")
async def hapusid(request : Request):
    data = await request.json()
    if "id" not in data:
        raise HTTPException(status_code=400, detail="diperlukan id tolol")

    hasilreq = hapusberdasarid(data["id"], DB1)

    if hasilreq == 0:
        raise HTTPException(status_code=404, detail="tolol start no 1")
    if hasilreq == -1 :
        raise HTTPException(status_code=500, detail="benerin back end nya tod")

    return {
        "success": True,
        "dataterhapus": data["id"]

    }

@app.post("/cars/update")
async def update_mobil(request: Request):
    data = await request.json()

    required = ["id","carname", "carbrand", "carmodel", "carprice"]
    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} belum di input anjing")
    result = updaterecord(
        DB1,
        data["id"],
        data["carname"],
        data["carbrand"],
        data["carmodel"],
        data["carprice"]
    )
    if result == 0:
        raise HTTPException(status_code=404, detail="ID tidak ditemukan")
    if result == -1:
        raise HTTPException(status_code=500, detail="Database error")

    return {
        "success": True,
        "dataterubah": data["id"]
    }


@app.post("/cars/create")
async def create_car(request: Request):
    data = await request.json()

    required = ["carname", "carbrand", "carmodel", "carprice"]
    for field in required:
        if field not in data:
            raise HTTPException(status_code=400, detail=f"{field} belum di input anjing")

    new_id = tambahmobil(
        DB1,
        data["carname"],
        data["carbrand"],
        data["carmodel"],
        data["carprice"]
    )

    if new_id == -1:
        raise HTTPException(status_code=500, detail="database error")

    return {
        "success": True,
        "id": new_id
    }

@app.post("/cars/search/name")
async def caridengannama(request : Request):
    data = await request.json()
    if "carname" not in data:
        raise HTTPException(status_code=400, detail="isi namanya anjeng")

    results = caripakenama(DB1, data["carname"])
    return results

@app.post("/cars/search/model")
async def caridenganmodel(request : Request):
    data = await request.json()
    if "carmodel" not in data:
        raise HTTPException(status_code=400, detail="isi namanya anjeng")

    results = carimodel(DB1, data["carmodel"])
    return results

@app.post("/cars/search/brand")
async def caridenganbrand(request : Request):
    data = await request.json()
    if "carbrand" not in data:
        raise HTTPException(status_code=400, detail="isi namanya anjeng")

    results = caripakebrand(DB1, data["carbrand"])
    return results
