# src/analysis.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def process_data(trades, sentiment):

    # ---------------- CLEAN ----------------
    trades['Timestamp'] = pd.to_numeric(trades['Timestamp'], errors='coerce')
    trades = trades.dropna(subset=['Timestamp'])

    trades['Timestamp'] = pd.to_datetime(
        trades['Timestamp'].astype('int64'),
        unit='ms',
        errors='coerce'
    )

    sentiment['date'] = pd.to_datetime(sentiment['date'], errors='coerce')

    trades = trades.dropna(subset=['Timestamp', 'Closed PnL'])
    sentiment = sentiment.dropna(subset=['date'])

    trades['date'] = trades['Timestamp'].dt.date
    sentiment['date'] = sentiment['date'].dt.date

    data = pd.merge(trades, sentiment, on='date', how='inner')

    # ---------------- FEATURES ----------------
    data['profit'] = data['Closed PnL']

    data['Execution Price'] = pd.to_numeric(data['Execution Price'], errors='coerce')
    data['Size USD'] = pd.to_numeric(data['Size USD'], errors='coerce')

    data = data.dropna(subset=['Execution Price', 'Size USD'])

    data['is_buy'] = data['Side'].apply(lambda x: 1 if str(x).upper() == 'BUY' else 0)

    data['sentiment_encoded'] = data['classification'].map({
        'Fear': 0,
        'Greed': 1,
        'Neutral': 0.5
    })

    data['profitable'] = (data['profit'] > 0).astype(int)

    # ---------------- MODEL ----------------
    features = ['is_buy', 'Execution Price', 'Size USD', 'sentiment_encoded']

    X = data[features]
    y = data['profitable']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return data, model