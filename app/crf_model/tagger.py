import pycrfsuite  # Importez pycrfsuite
from app.config.settings import settings

def initialize_tagger():
    tagger = pycrfsuite.Tagger()
    tagger.open(settings.crf_model_path)  # Chargez votre modèle CRF préalablement entraîné en spécifiant le chemin
    return tagger
