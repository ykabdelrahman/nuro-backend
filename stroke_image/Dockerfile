FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y wget unzip && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Download model from GitHub Releases
RUN wget -O stroke_image_v2.keras.zip \
    "https://github.com/ykabdelrahman/nuro-backend/releases/download/v1.0-models/stroke_image_v2.keras.zip" \
    && unzip stroke_image_v2.keras.zip \
    && rm stroke_image_v2.keras.zip

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]