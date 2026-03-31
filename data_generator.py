import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_data(days=180):
    start_date = datetime.now() - timedelta(days=days)
    dates = pd.date_range(start_date, periods=days, freq='D')
    
    # Simulate daily MB additions
    photos = np.random.normal(150, 50, days).clip(0)
    videos = np.random.normal(300, 100, days).clip(0)
    docs = np.random.normal(10, 5, days).clip(0)
    
    df = pd.DataFrame({
        'date': dates,
        'photos_mb': photos,
        'videos_mb': videos,
        'docs_mb': docs
    })
    
    df['total_mb_added'] = df['photos_mb'] + df['videos_mb'] + df['docs_mb']
    df['cumulative_mb'] = df['total_mb_added'].cumsum()
    
    df.to_csv('storage_history.csv', index=False)
    print("✅ Created: storage_history.csv")

if __name__ == "__main__":
    generate_synthetic_data()