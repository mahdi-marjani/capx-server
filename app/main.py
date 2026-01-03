from fastapi import FastAPI, HTTPException
import base64
import numpy as np
from PIL import Image
from io import BytesIO

from capx_core.detector import detect_cells
from .config import HOST, PORT
from .schemas import DetectRequest, DetectResponse

app = FastAPI(
    title="capx-server",
    description="AI backend for solving reCAPTCHA image challenges",
    version="0.1.0"
)


# =========================
# Helpers
# =========================

def decode_image(b64: str) -> np.ndarray:
    try:
        img_bytes = base64.b64decode(b64)
        img = Image.open(BytesIO(img_bytes)).convert("RGB")
        return np.asarray(img)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image data")


# =========================
# Routes
# =========================

@app.post("/detect", response_model=DetectResponse)
def detect(req: DetectRequest):
    if req.grid not in ("3x3", "4x4"):
        raise HTTPException(status_code=400, detail="Invalid grid type")

    image = decode_image(req.image)

    try:
        cells = detect_cells(
            image=image,
            grid=req.grid,
            target_text=req.target
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"cells": cells}


# =========================
# Local run (optional)
# =========================

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=True)
