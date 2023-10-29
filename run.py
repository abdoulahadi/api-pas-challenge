from fastapi import FastAPI
from app.api.endpoints import text_annotation, pdf_annotation
from app.config.settings import settings
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug
)

# Configurez le middleware CORS pour autoriser les requêtes OPTIONS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Vous pouvez spécifier ici les origines autorisées
    allow_methods=["*"],  # Autoriser toutes les méthodes, y compris OPTIONS
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

app.include_router(text_annotation.router)
app.include_router(pdf_annotation.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
