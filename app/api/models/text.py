from pydantic import BaseModel
from typing import List

class Entity(BaseModel):
    text: str
    label: str
    start: int
    end: int

class TextRequest(BaseModel):
    text: str

class TextResponse(BaseModel):
    entities: List[Entity]
    sentences: str
