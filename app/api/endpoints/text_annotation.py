from fastapi import APIRouter, HTTPException
from ..models.text import TextRequest, TextResponse
from ...crf_model.predict import predict_annotations

router = APIRouter()

@router.get("/")
async def accueil():
    return "Bienvenue Dans l'API de XelKoom-IA"

@router.post("/annotate-text", tags=["Text Annotation"])
async def annotate_text(request: TextRequest):
    annotated_text = predict_annotations(request.text)
    return {"annotated_text": annotated_text}
