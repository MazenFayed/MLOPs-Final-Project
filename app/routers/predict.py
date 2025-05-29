from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import joblib
import pathlib
from app.utils.preprocess import extract_landmarks

ROOT = pathlib.Path(__file__).resolve().parents[2]
MODEL = joblib.load(ROOT / "app" / "models" / "lgbm.pkl")

router = APIRouter(prefix="/predict", tags=["predict"])

@router.post("/predict")
async def predict_gesture(file: UploadFile = File(...)):
    if file.content_type not in ("image/jpeg", "image/png"):
        raise HTTPException(status_code=400, detail="File must be a photo extension (.jpg, .jpeg, .png)")

    img_bytes = await file.read()
    img = cv2.imdecode(np.frombuffer(img_bytes, np.uint8), cv2.IMREAD_COLOR)
    if img is None:
        raise HTTPException(status_code=400, detail="Could not resolve image")

    print("[INFO] Image:", img.shape)

    feats = extract_landmarks(img)
    if feats is None:
        raise HTTPException(status_code=422, detail="No hand detected")

    print("[INFO] Feature:", feats.shape)

    try:
        pred = MODEL.predict([feats])[0]
    except Exception as e:
        # Log the exception but don't expose internal error details
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Server Error")

    return JSONResponse({"class": str(pred)})
