import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "../models/model.pkl")

def load_model():
    """Carrega o modelo treinado."""
    return joblib.load(MODEL_PATH)

def run_model(model, df):
    """Executa a predição."""
    return model.predict(df)