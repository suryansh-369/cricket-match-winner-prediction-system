# 🏏 Cricket Match Winner Prediction System

## 📌 Project Overview

This project is an end-to-end Machine Learning system that predicts the winner of a cricket match using historical international match data.

The system leverages custom feature engineering techniques, a Logistic Regression model, a FastAPI backend, and an interactive web frontend to provide real-time match winner predictions.

The project demonstrates the complete machine learning workflow from data collection to deployment-ready inference.

---

## 🚀 Features

* Historical cricket match analysis
* Team performance feature engineering
* Head-to-head statistics
* Venue-specific performance metrics
* Toss impact analysis
* Machine Learning winner prediction
* Confidence score generation
* REST API using FastAPI
* Interactive frontend interface
* Model serialization using Joblib

---

## 🛠️ Tech Stack

### Machine Learning

* Python
* Pandas
* NumPy
* Scikit-learn
* Logistic Regression

### Backend

* FastAPI
* Pydantic
* Uvicorn

### Frontend

* HTML
* CSS
* JavaScript

### Model Management

* Joblib

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
Cricket_WC_Model/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── models/
│   └── best_model.pkl
│
├── frontend/
│   └── index.html
│
├── notebooks/
│   ├── Data_Extraction.ipynb
│   ├── EDA.ipynb
│   ├── Feature_Engineering.ipynb
│   └── Model_Training.ipynb
│
├── src/
│   ├── feature_engineering.py
│   ├── train.py
│   ├── predict.py
│   └── app.py
│
├── Screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📊 Feature Engineering

The model uses cricket-specific engineered features rather than raw match information.

### Team Performance Features

* Matches Played
* Win Rate
* Recent Form (Last 5 Matches)

### Venue Features

* Matches Played At Venue
* Venue Win Rate

### Head-to-Head Features

* Team 1 Head-to-Head Wins
* Team 2 Head-to-Head Wins

### Toss Features

* Team 1 Won Toss
* Team 2 Won Toss
* Toss Decision

These features help capture team strength, momentum, venue familiarity, and historical matchup performance.

---

## 🤖 Machine Learning Model

### Algorithm

Logistic Regression

### Why Logistic Regression?

* Fast training and inference
* Interpretable probabilities
* Strong baseline for classification problems
* Works effectively with engineered statistical features

### Model Output

The model predicts:

* Winning Team
* Prediction Confidence Score

Example:

```json
{
    "winner": "Australia",
    "confidence": 0.7476
}
```

---

## 🌐 API Endpoints

### Health Check

```http
GET /
```

Response:

```json
{
    "message": "Cricket Winner Prediction API Running"
}
```

---

### Predict Winner

```http
POST /predict
```

Request Body:

```json
{
    "team1": "India",
    "team2": "Australia",
    "venue": "Dubai",
    "toss_winner": "India",
    "toss_decision": "bat"
}
```

Response:

```json
{
    "winner": "Australia",
    "confidence": 0.7476
}
```

---

## 💻 Frontend Application

The project includes a simple web interface where users can:

* Enter participating teams
* Select venue information
* Provide toss details
* Generate winner predictions instantly

The frontend communicates directly with the FastAPI backend through REST API calls.

---

## 📈 Workflow

```text
Historical Match Data
          ↓
Data Cleaning
          ↓
Feature Engineering
          ↓
Model Training
          ↓
Model Serialization
          ↓
FastAPI Backend
          ↓
Frontend Interface
          ↓
Winner Prediction
```

---

## ▶️ Running the Project

### Clone Repository

```bash
git clone <repository-url>
cd Cricket_WC_Model
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train Model

```bash
python src/train.py
```

### Run API

```bash
python -m uvicorn src.app:app --reload
```

### Open API Documentation

```text
http://127.0.0.1:8000/docs
```

---

## 🎯 Future Improvements

* Random Forest and XGBoost experimentation
* Team ranking integration
* Player-level statistics
* World Cup-specific predictions
* Docker containerization
* AWS deployment
* CI/CD pipeline
* MLflow experiment tracking

---

## 👨‍💻 Author

Godalla Suryansh

Aspiring Machine Learning Engineer focused on building end-to-end machine learning systems, MLOps pipelines, and production-ready AI applications.

