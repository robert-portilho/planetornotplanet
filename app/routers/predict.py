from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib
from pathlib import Path


router = APIRouter(prefix="/predict", tags=["Prediction"], include_in_schema=True)


# 🔹 Modelo de entrada — define os parâmetros esperados
class PredictionInput(BaseModel):
    koi_duration: float = Field(..., description="Duração do trânsito")
    koi_ror: float = Field(..., description="Razão raio planeta/estrela")
    koi_srho: float = Field(..., description="Densidade estelar")
    koi_dicco_msky: float = Field(..., description="Correlação de deslocamento medido no céu")
    koi_dikco_msky: float = Field(..., description="Correlação de deslocamento intrínseco no céu")


@router.post("")
def predict(input_data: PredictionInput):
    """
    Recebe parâmetros numéricos no corpo da requisição e retorna a probabilidade de classificação.
    """

    try:

        model_path = Path(__file__).resolve().parent.parent / "models" / "final_model.joblib"
        # 🔸 Carrega o modelo
        model = joblib.load(model_path)
        


        # 🔸 Cria um DataFrame com os dados recebidos
        obs = pd.DataFrame([{
            "koi_duration": input_data.koi_duration,
            "koi_ror": input_data.koi_ror,
            "koi_srho": input_data.koi_srho,
            "koi_dicco_msky": input_data.koi_dicco_msky,
            "koi_dikco_msky": input_data.koi_dikco_msky
        }])

        # 🔸 Faz a previsão (probabilidade)
        result = model.predict_proba(obs)[:, 1]
        print(result)

        return {"prediction_probability": float(result[0])}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
