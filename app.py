import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.load_data import load_data
from src.analysis import process_data

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Crypto AI Dashboard", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 15px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- LOAD ----------------
trades, sentiment = load_data()
data, model = process_data(trades, sentiment)

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Controls")
option = st.sidebar.selectbox(
    "Select View",
    ["Overview", "Analysis", "ML Insights"]
)

# ---------------- HEADER ----------------
st.title("📊 Crypto Sentiment AI Dashboard")
st.markdown("### Analyze how market sentiment affects trading performance")

# ---------------- OVERVIEW ----------------
if option == "Overview":

    st.subheader("📌 Key Metrics")

    col1, col2, col3 = st.columns(3)

    avg_profit = data.groupby('classification')['profit'].mean()

    col1.metric("Fear Profit", f"{avg_profit.get('Fear',0):.2f}")
    col2.metric("Greed Profit", f"{avg_profit.get('Greed',0):.2f}")
    col3.metric("Total Trades", len(data))

    st.markdown("---")

    st.subheader("📊 Trade Distribution")

    st.bar_chart(data['classification'].value_counts())

# ---------------- ANALYSIS ----------------
elif option == "Analysis":

    st.subheader("📈 Profit vs Sentiment")

    fig, ax = plt.subplots(figsize=(8,5))
    sns.boxplot(x='classification', y='profit', data=data, ax=ax)
    st.pyplot(fig)

    st.subheader("📉 Profit Distribution")

    fig2, ax2 = plt.subplots()
    sns.histplot(data['profit'], bins=50, ax=ax2)
    st.pyplot(fig2)

# ---------------- ML INSIGHTS ----------------
elif option == "ML Insights":

    st.subheader("🤖 Model Insights")

    features = ['is_buy', 'Execution Price', 'Size USD', 'sentiment_encoded']

    import pandas as pd
    importance = pd.Series(model.feature_importances_, index=features)

    st.write("### Feature Importance")
    st.bar_chart(importance)

    st.markdown("---")

    st.subheader("🧠 Strategy Suggestions")

    summary = data.groupby('classification')['profit'].mean()

    def suggest_strategy(sentiment):
        if summary[sentiment] > 0:
            return "✅ Profitable → Trade"
        else:
            return "⚠️ Risky → Avoid"

    data['strategy'] = data['classification'].apply(suggest_strategy)

    st.dataframe(data[['classification', 'profit', 'strategy']].head(20))

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown("🚀 Vidhan Project")