from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.predict import predict_winner

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MatchInput(BaseModel):
    team1: str
    team2: str
    venue: str
    toss_winner: str
    toss_decision: str


@app.get("/")
def home():
    return {"message": "Cricket Winner Prediction API Running"}


@app.post("/predict")
def predict(match: MatchInput):

    result = predict_winner(match.dict())

    return result