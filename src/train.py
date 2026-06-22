#Loading the datasets
print("Model is loading")
import pandas as pd 
df = pd.read_csv("data/processed/matches_features_v1.csv")

#Seprating the data from target
print("Model is seprating the data")
X = df.drop(["winner","date"], axis=1)
y = df["winner"]

#Spliting the data for training , testing and valdation
print("Model is spliting for trian and test")
from sklearn.model_selection import train_test_split as tts 

split_idx = int(len(df) * 0.8)

X_train = X.iloc[:split_idx]
X_test = X.iloc[split_idx:]

y_train = y.iloc[:split_idx]
y_test = y.iloc[split_idx:]


#Preprocessig the Data
print("Model is preprocesing ")
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline

categorical_features = ["team1", "team2","venue","toss_decision","toss_winner"]

numerical_features = ["team1_matches_played",
                      "team1_win_rate",
                      "team1_form_5",

    "team2_matches_played",
    "team2_win_rate",
    "team2_form_5",

    "team1_h2h_wins",
    "team2_h2h_wins",

    "team1_venue_matches",
    "team1_venue_win_rate",

    "team2_venue_matches",
    "team2_venue_win_rate",

    "team1_won_toss",
    "team2_won_toss"
    ]

preprocessor = ColumnTransformer(
    transformers=[
        (
            "cat", OneHotEncoder(handle_unknown="ignore"),categorical_features,
            
        ),
        (
            "num", StandardScaler(), numerical_features
        )
    ],
    remainder="passthrough"
)

#Model Selection and fitting
print("Model is running")
from sklearn.linear_model import LogisticRegression

model = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("classifier",LogisticRegression(
        max_iter=1000,
        random_state=42
)
        )
    ]
)

# Model fitting and prediction
print("Model is fitting the train data")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Model is checking the metrics")
# Metrics checking 
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test,y_pred)

print("Accuracy :",accuracy)

# Model savinf in a pickle file 
print("Model is saving in the pickle file")
import joblib
import os

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/best_model.pkl"
)

print("Model saved successfully")