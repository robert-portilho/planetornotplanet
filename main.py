from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.routers import predict


app = FastAPI(title="To planet or not to planet")
origins = [
    "https://planetornotplanet-front.onrender.com"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
app.include_router(predict.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.mount("/static", StaticFiles(directory="static"), name="static")

# Rota raiz -> index.html
@app.get("/")
async def root():
    return FileResponse("static/index.html")