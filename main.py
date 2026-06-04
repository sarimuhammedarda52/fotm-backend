from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# CORS Ayarları (Ön yüzün sunucuya erişebilmesi için)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GirisModel(BaseModel):
    username: str
    password: str

OPERATOR_VERILERI = {
    "mehmet.c": {"password": "fotmmehmet", "name": "Mehmet Ceran", "photo": "mehmetceran.jpg"},
    "ilker.k": {"password": "fotmilker", "name": "Ilker Kurtini", "photo": "ilkerkurtini.jpg"},
    "arda.s": {"password": "fotmarda", "name": "Muhammed Arda Sarı", "photo": "muhammedardasari.jpg"},
    "emirhan.s": {"password": "fotmemirhan", "name": "Emirhan Şenel", "photo": "emirhansenel.jpg"},
    "mustafa.d": {"password": "fotmmustafa", "name": "Mustafa Can Demir", "photo": "mustafacandemir.jpg"},
    "kariyer.k": {"password": "1234", "name": "Kariyer", "photo": "1.png"},
    "serkan.m": {"password": "123456", "name": "Serkan Mutlu", "photo": "11.png"},
    "huseyin.c": {"password": "fotmhuseyin", "name": "Hüseyin Çiftçi", "photo": "11.png"},
    "rumeysa.d": {"password": "fotmrumeysa", "name": "Rümeysa Doğancal", "photo": "11.png"},
    "mehmet.t": {"password": "fotmmehmett", "name": "Mehmet Torun", "photo": "11.png"},
    "memin.y": {"password": "fotmemin", "name": "Muhammed Emin Yıldırım", "photo": "11.png"},
    "anil.h": {"password": "fotmanil", "name": "Anıl Harmanlı", "photo": "11.png"},
    "mert.b": {"password": "fotmmert", "name": "Mert Başak", "photo": "11.png"},
    "ahmetcan.f": {"password": "fotmahmet", "name": "Ahmet Can Fındık", "photo": "11.png"},
    "ebrar.o": {"password": "fotmebrar", "name": "Ebrar Oturak", "photo": "11.png"},
    "cinar.a": {"password": "fotmcinar", "name": "Çınar Aktaş", "photo": "11.png"},
    "rabia.t": {"password": "fotmrabia", "name": "Rabia Tepe", "photo": "11.png"},
    "medine.a": {"password": "fotmmedine", "name": "Medine Akkaş", "photo": "11.png"},
    "ecrin.y": {"password": "fotmecrin", "name": "Ecrin İlkim Yılmaz", "photo": "11.png"},
    "ayberk.b": {"password": "fotmayberk", "name": "Ayberk Batır", "photo": "11.png"},
    "menes.b": {"password": "fotmenes", "name": "Muhammed Enes Bıyık", "photo": "11.png"},
    "yakup.t": {"password": "fotmyakup", "name": "Yakup Turan", "photo": "11.png"},
    "emel.d": {"password": "fotmemel", "name": "Emel Dalga", "photo": "11.png"},
    "semanur.k": {"password": "fotmsema", "name": "Semanur Kuvan", "photo": "11.png"},
    "nisanur.e": {"password": "fotmnisa", "name": "Nisa Nur Erdem", "photo": "11.png"},
    
}

@app.get("/")
async def root():
    return {"mesaj": "FOT-M İmalat Yürütme Sistemleri Sunucusu Aktif", "durum": "OK"}

@app.post("/api/login")
async def login(user_data: GirisModel):
    username = user_data.username
    password = user_data.password

    if username in OPERATOR_VERILERI:
        operator = OPERATOR_VERILERI[username]
        if operator["password"] == password:
            return JSONResponse(content={
                "status": "success",
                "username": username,
                "name": operator["name"],
                "photo": operator["photo"]
            }, status_code=200)
        else:
            raise HTTPException(status_code=401, detail="Hatali kullanici adi veya sifre.")
    else:
        raise HTTPException(status_code=401, detail="Hatali kullanici adi veya sifre.")
