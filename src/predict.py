import joblib

from .feature_engineering import create_features

model = joblib.load("models/best_model.pkl")


def predict_winner(input_data):

    features_df = create_features(input_data)

    winner = model.predict(features_df)[0]

    confidence = model.predict_proba(features_df).max()

    return {
        "winner": winner,
        "confidence": float(confidence)
    }

