from pydantic import BaseModel
from typing import List

class DetectRequest(BaseModel):
    image: str       # base64
    grid: str        # "3x3" | "4x4"
    target: str      # raw text (e.g. "cars")

class DetectResponse(BaseModel):
    cells: List[int]