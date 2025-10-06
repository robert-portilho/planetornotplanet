from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import predict

app = FastAPI(title="To planet or not to planet")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # origem do seu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(predict.router)

@app.get("/")
def root():
    return {"message": "API de predição online"}