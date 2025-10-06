from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd
from app.services.model_service import load_model, run_model
from app.utils.data_utils import preprocess_data
import json

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
async def predict(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="O arquivo deve ser um CSV.")

    try:
        # Lê o arquivo em memória
        df = pd.read_csv(file.file)
        df_preprocessed = preprocess_data(df)

        #model = load_model()
        #predictions = run_model(model, df_preprocessed)
        # Simulação de previsões para exemplo de exoplabetas (Name, Period, Radius, Mass, Magnitude, Classification)
        prediction = {
            "Name": "Test-33D",
            "Period": 289.9,
            "Radius": 2.4,
            "Mass": 36.0,
            "Magnitude": 11.5,
            "Classification": "PLANET"
        }
        

        return prediction

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
