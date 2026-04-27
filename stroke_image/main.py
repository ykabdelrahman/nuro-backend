from contextlib import asynccontextmanager
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import numpy as np
from PIL import Image
import io
import uvicorn
import traceback

MODEL_VERSION = "v4"
model = None
model_error = None


def _load_model():
    global model, model_error
    try:
        import tensorflow as tf
        model = tf.keras.models.load_model("stroke_image_v2.keras")
    except Exception as e:
        model_error = traceback.format_exc()


@asynccontextmanager
async def lifespan(app: FastAPI):
    _load_model()
    yield


app = FastAPI(title="Stroke Image Detection API", version="1.0.0", lifespan=lifespan)


def preprocess_image(image_bytes):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image) / 255.0
    image = np.expand_dims(image, axis=0)
    return image


@app.get("/")
def root():
    return {
        "service": "Stroke Image Detection API",
        "description": "AI-based imaging interpretation for stroke detection.",
        "status": "online",
        "model_loaded": model is not None,
        "model_error": model_error,
        "version": MODEL_VERSION,
        "endpoints": {
            "root": "/",
            "predict_image": "/predict [POST] (requires multipart/form-data)"
        },
        "docs": "/docs"
    }


@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    if model is None:
        return JSONResponse(status_code=503, content={
            "error": "Model not loaded",
            "detail": model_error,
            "status": "failed"
        })
    try:
        image_bytes = await file.read()
        image = preprocess_image(image_bytes)

        prediction = model.predict(image)
        probability = float(prediction[0][0]) * 100

        if probability >= 50:
            result = "Stroke Detected"
            risk = "High Risk"
        else:
            result = "No Stroke Detected"
            risk = "Low Risk"

        return JSONResponse(content={
            "result": result,
            "risk_category": risk,
            "stroke_probability": round(probability, 2),
            "filename": file.filename,
            "status": "success"
        })
    except Exception as e:
        return JSONResponse(status_code=500, content={
            "error": str(e),
            "status": "failed"
        })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
