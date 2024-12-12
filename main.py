from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import os

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Access CSV File
csv_path = os.path.join(os.getcwd(), "public", "all_hadiths_clean.csv")

def load_data():
    if not os.path.exists(csv_path):
        raise HTTPException(status_code=500, detail="CSV file not found.")
    return pd.read_csv(csv_path)

@app.get("/")
def read_root():
    return {"message": "API is working!"}

@app.get("/get_hadiths")
def get_hadiths():
    try:
        data = load_data()
        return {"hadiths": data.head(10).to_dict(orient="records")}  # Example: Return top 10 records
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
