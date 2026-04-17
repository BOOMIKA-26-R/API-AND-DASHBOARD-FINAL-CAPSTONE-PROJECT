import pandas as pd
import numpy as np
import joblib
from fastapi import FastAPI
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
import time

app = FastAPI()
MODEL_PATH = "model.pkl"

def get_processed_data():

    raw_data = {
        "timestamp": [pd.Timestamp.now()],
        "category": [np.random.choice(["Retail", "Tech", "Health"])],
        "value": [np.random.choice([10.5, np.nan, 25.3])], 
    }
    df = pd.DataFrame(raw_data)
    

    df["value"] = df["value"].fillna(df["value"].mean() if not df.empty else 0)
    

    le = LabelEncoder()
    df["cat_idx"] = le.fit_transform(df["category"])
    return df


@app.on_event("startup")
def train_model():
    # Simulate initial training (Tasks 6, 7, 17)
    X = np.random.rand(100, 1)
    y = X.flatten() * 10
    model = RandomForestRegressor().fit(X, y)
    joblib.dump(model, MODEL_PATH)


@app.get("/predict")
def predict(input_val: float):
    # Task 15: Monitor latency
    start_time = time.time()
    
    model = joblib.load(MODEL_PATH)
    pred = model.predict([[input_val]])
    
    latency = time.time() - start_time
    return {"prediction": pred[0], "latency_ms": latency * 1000}

@app.get("/")
def home():
    return {"status": "API is running"}
