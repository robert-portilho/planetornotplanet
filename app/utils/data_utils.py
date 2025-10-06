import pandas as pd

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Executa o pré-processamento necessário antes da predição."""
    # Exemplo genérico:
    df = df.fillna(0)
    # df = df.drop(columns=["coluna_inutil"]) etc.
    return df
