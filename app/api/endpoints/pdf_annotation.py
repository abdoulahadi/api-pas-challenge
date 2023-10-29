from fastapi import APIRouter, HTTPException, UploadFile, File
from ..models.text import TextResponse
from ...crf_model.predict import predict_annotations
import fitz  # Importez la bibliothèque PyMuPDF pour travailler avec les PDF

router = APIRouter()

@router.post("/annotate-pdf", tags=["PDF Annotation"])
async def annotate_pdf(pdf_file: UploadFile):
    try:
        # Vérifiez que le fichier est bien un PDF
        if not pdf_file.filename.endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Le fichier n'est pas un PDF.")

        # Lisez le contenu du PDF
        pdf_content = pdf_file.file.read()

        # Utilisez PyMuPDF pour extraire le texte du PDF
        pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
        text = ""
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            text += page.get_text()

        # Appelez la fonction de prédiction pour annoter le texte extrait
        annotated_text = predict_annotations(text)

        return {"annotated_text": annotated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'annotation du PDF : {str(e)}")
