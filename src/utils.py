import json
import pandas as pd

def load_json(path: str):
    with open(path, 'r') as f:
        return json.load(f)

def preprocess(data: list):
    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df