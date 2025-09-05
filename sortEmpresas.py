import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def sort_empresas(empresas: pd.DataFrame, preferences: pd.DataFrame):
    feature_columns = ['puntualidad', 'estadoCarga', 'precio', 'atencion', 'clasificacionComentario']
    empresas_vec = empresas[feature_columns].to_numpy()
    preferences_vec = preferences[feature_columns].to_numpy()[0]
    similarities = cosine_similarity(empresas_vec, [preferences_vec]).flatten()
    print(similarities)
    empresas['similarity'] = similarities
    empresas = empresas.sort_values(by='similarity', ascending=False)
    result = empresas["empresa.razonSocial"].to_list()
    return result
    