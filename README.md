# 🚀 Crypto Sentiment AI Dashboard

An end-to-end data analysis and machine learning project that explores the relationship between **market sentiment (Fear/Greed)** and **trader performance** using real trading data.

---

## 📌 Objective

The goal of this project is to:

* Analyze how market sentiment impacts trading outcomes
* Identify patterns in trader performance
* Build a predictive model for trade profitability
* Provide insights for smarter trading strategies

---

## 📂 Project Structure

```
crypto-sentiment-ai/
│
├── app.py                  # Streamlit dashboard (UI)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
│
├── data/
│   ├── historical_data.csv
│   └── fear_greed_index.csv
│
├── src/
│   ├── load_data.py        # Loads datasets
│   ├── preprocess.py       # Data cleaning & formatting
│   └── analysis.py         # Merging, feature engineering & ML model
│
└── analysis.ipynb          # Jupyter notebook (detailed analysis)
```

---

## ⚙️ Tech Stack

* Python
* Pandas & NumPy
* Scikit-learn (Machine Learning)
* Streamlit (Dashboard)
* Matplotlib & Seaborn (Visualization)

---

## 📊 Datasets Used

### 1. Bitcoin Market Sentiment

* Columns: `Date`, `Classification (Fear/Greed)`

### 2. Historical Trader Data

* Columns include:

  * Execution Price
  * Size
  * Side (Buy/Sell)
  * Closed PnL
  * Timestamp
  * etc.

---

## 🔄 Workflow

1. **Data Loading**

   * Loaded both datasets from CSV files

2. **Data Preprocessing**

   * Converted timestamps to datetime
   * Standardized column formats
   * Cleaned missing values

3. **Data Merging**

   * Merged datasets on date to align trades with sentiment

4. **Feature Engineering**

   * Created:

     * `profit`
     * `is_buy`
     * sentiment encoding
     * trade-related features

5. **Exploratory Data Analysis**

   * Profit vs sentiment
   * Trade distribution
   * Profit distribution

6. **Machine Learning Model**

   * Logistic Regression model
   * Predicts whether a trade will be profitable

7. **Visualization & Dashboard**

   * Built interactive dashboard using Streamlit

---

## 🤖 Machine Learning

* Model: **Logistic Regression**
* Target: Trade profitability (`profit > 0`)
* Features:

  * Sentiment value
  * Trade type (Buy/Sell)
  * Execution price
  * Trade size

---

## 📈 Key Insights

* Trades during **Fear** tend to show better profitability than Greed
* **Win rate is higher in Fear market conditions**
* Most trades are **break-even (profit = 0)**
* High-profit trades are fewer but dominate overall returns

---

## ⚠️ Important Note on Profit Visualization

The dataset contains a **large number of zero-profit trades**.

### Why this matters:

* Graphs may appear skewed (large spike at 0)
* Initial rows (e.g., using `head()`) may display only zero values

### Interpretation:

* This is **not a bug**
* It reflects real trading behavior where many trades close at break-even

### Handling:

* Zero-profit trades are filtered **only for visualization**
* Original data is preserved for analysis and modeling

---

## 📊 Dashboard Features

* Overview of key metrics
* Profit vs sentiment visualization
* Profit distribution analysis
* ML-based feature importance
* Strategy suggestions based on sentiment

---

## 📓 Notebook

The `analysis.ipynb` notebook includes:

* Step-by-step data analysis
* Intermediate outputs
* Visualizations
* Detailed insights

👉 This demonstrates the complete thought process behind the project

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🎯 Conclusion

This project demonstrates how combining **market sentiment data with trading data** can uncover meaningful insights and improve decision-making in trading systems.

---

## 👨‍💻 Author

**Vidhan Mishra**

---

## 📌 Note

This project was developed as part of a data science assignment focused on analyzing trader performance using sentiment data.
