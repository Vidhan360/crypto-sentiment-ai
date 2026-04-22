# src/preprocess.py

def preprocess(trades, sentiment):
    # Only basic cleaning (SAFE)
    
    trades.columns = trades.columns.str.strip()
    sentiment.columns = sentiment.columns.str.strip()
    
    return trades, sentiment