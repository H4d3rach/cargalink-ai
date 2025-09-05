from sentence_transformers import SentenceTransformer
import pandas as pd
import torch
import logging

class Chatbot:
    def __init__(self) -> None:
        self.logger = logging.getLogger("Chatbot")
        self.model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')
        self.logger.info(f"El modelo del chatbot fue cargado")
        self.emmbedingsDF = self.get_embeddings()
        self.logger.info(f"Los embeddings fueron extraidos")
    
    def get_response(self, question: str) -> tuple[str, bool]:
        question_emb = self.model.encode(question).tolist()
        similarities = self.model.similarity(question_emb, self.emmbedingsDF["embeddings"].tolist())
        index_max = torch.argmax(similarities).item()
        max_similarity = similarities[0, index_max].item()
        if max_similarity < 0.77:
            self.logger.info(f"Similitud maxima ('{max_similarity}') menor a el umbral de 0.77")
            exceeds_threshold = False
            return ("No entendí la pregunta, ¿puede redactarla de otra forma?", exceeds_threshold)
        response = self.emmbedingsDF.loc[index_max, "answers"]
        self.logger.info(f"Similitud maxima ('{max_similarity}') mayor al umbral, respuesta: '{response}'")
        exceeds_threshold = True
        return (response, exceeds_threshold)

    def get_embeddings(self):
        df = pd.read_csv("files/respondidas.csv")
        df = df[~df['Respuesta'].isin(["no", "pregunta invalida"])]
        questions = df["Temática"].tolist()
        answers = df["Respuesta"].tolist()
        section = df["Título"].tolist()
        embeddings = self.model.encode(questions).tolist()
        embeddings_dict = {"embeddings": embeddings, "answers": answers, "section": section}
        return pd.DataFrame(embeddings_dict)