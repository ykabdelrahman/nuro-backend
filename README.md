# NURO Backend - Stroke Detection & AI Suite

A comprehensive AI ecosystem deployed via Docker & Dokploy for stroke early detection, risk assessment, and patient education.

## 🚀 Deployment Status
Deployed at [Dokploy](https://nuro-chatbot.baselembaby.cloud) on VPS.

| Service | Public URL | Purpose |
| :--- | :--- | :--- |
| **Chatbot** | `https://nuro-chatbot.baselembaby.cloud` | AI Medical Assistant (GPT-4o-mini) |
| **Stroke QA** | `https://nuro-qa.baselembaby.cloud` | ML Stroke Risk Prediction |
| **Stroke Image** | `https://nuro-image.baselembaby.cloud` | Image-based Detection |

---

## 🏗️ Architecture
The system is orchestrated using **Docker Compose** with three independent microservices:
1.  **Chatbot**: FastAPI + LangGraph + LangChain.
2.  **Stroke QA**: FastAPI + Scikit-Learn (Random Forest/XGBoost).
3.  **Stroke Image**: FastAPI + TensorFlow/Keras.

---

## 📚 API Integration Guide (For Mobile App)

### 🤖 1. Chatbot API
**Endpoint**: `POST /chat/stream`
**Type**: Server-Sent Events (Streaming)

**Request Body:**
```json
{
  "query": "What should I do if I see FAST symptoms?",
  "messages": []
}
```

---

### 📊 2. Stroke Risk Prediction (QA)
**Endpoint**: `POST /predict`
**Type**: REST JSON

**Request Body:**
```json
{
  "gender": "Male",
  "age": 67.0,
  "hypertension": 0,
  "heart_disease": 1,
  "ever_married": "Yes",
  "work_type": "Private",
  "Residence_type": "Urban",
  "avg_glucose_level": 228.69,
  "bmi": 36.6,
  "smoking_status": "formerly smoked"
}
```
**Success Response:**
```json
{
  "stroke_probability": 85.3,
  "risk_category": "High Risk",
  "prediction_timestamp": "..."
}
```

---

### 🖼️ 3. Stroke Image Detection
**Endpoint**: `POST /predict`
**Type**: Multipart Form Data

**Request:** `file: <IMAGE_FILE>`

**Success Response:**
```json
{
  "message": "Image received. Processing...",
  "status": "online"
}
```

---

## 🛠️ Maintenance & Local Development

### 1. Environment Variables
The chatbot requires an `.env` file or Dokploy environment variable:
`OPENAI_API_KEY=your_key_here`

### 2. Local Run
```bash
docker-compose up --build
```
- Chatbot: `http://localhost:8001`
- Stroke QA: `http://localhost:8002`
- Stroke Image: `http://localhost:8003`

### 3. Adding New Features
Modify the respective folders (`chatbot/`, `stroke_QA/`, `stroke_image/`) and push to `main`. Dokploy will handle the redeployment.

---

## ⚠️ Important Configuration
- **LFS**: Git LFS was removed for budget reasons. Large model files (`.keras`) should be uploaded directly to Git if under 100MB or handled via dedicated storage.
- **Root Paths**: Each service now provides a detailed root `/` endpoint to confirm status and list available parameters.

---
© 2024 NURO AI Team
