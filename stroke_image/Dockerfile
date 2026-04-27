FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Download model before copying app code so model is cached independently
RUN wget -O stroke_image_v2.keras \
    "https://github.com/ykabdelrahman/nuro-backend/releases/download/v1.0-models/stroke_image_v2.keras.zip"

RUN echo "cache-bust-v3"
COPY . .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
