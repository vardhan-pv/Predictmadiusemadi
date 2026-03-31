import pandas as pd
import pickle
import os

if not os.path.exists('storage_history.csv'):
    print("Error: Run data_generator.py first!")
else:
    df = pd.read_csv('storage_history.csv', parse_dates=['date'])

    def train_trend_model(df):
        models = {}
        for cat in ['photos_mb', 'videos_mb', 'docs_mb']:
            # Calculate 14-day moving average for prediction
            models[cat] = float(df[cat].tail(14).mean())
        return models

    trend_models = train_trend_model(df)
    with open('trend_models.pkl', 'wb') as f:
        pickle.dump(trend_models, f)
        
    print("✅ Models trained and saved to trend_models.pkl")