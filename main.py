from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import predict


app = FastAPI(title="To planet or not to planet")
origins = [
    "https://planetornotplanet-front.onrender.com"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(predict.router)

@app.get("/")
def root():
    return {"message": "API de predição online"}