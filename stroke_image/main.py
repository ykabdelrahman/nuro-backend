from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI(title="Stroke Image Detection API", version="1.0.0")

@app.get("/")
def root():
    """Root endpoint to verify the API is running"""
    return {"message": "Stroke Image Detection API is running", "status": "online"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    """Placeholder for image prediction logic"""
    return JSONResponse(content={
        "message": "Image received. Please ensure the .keras model is uploaded to process predictions.",
        "filename": file.filename
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
