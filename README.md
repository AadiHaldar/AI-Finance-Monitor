# AI-Finance-Monitor
AI-Finance-Monitor  is an advanced budget forecasting and anomaly detection system that helps users track financial transactions, detect unusual spending patterns, and integrate securely with bank accounts. It combines machine learning, real-time monitoring, and secure banking APIs to provide accurate insights and fraud prevention.

Budget Forecasting: Uses Fenwick Trees, LSTMs, and SARIMA models to predict future expenses.

Anomaly Detection: Identifies fraudulent transactions and unusual spending patterns.

Bank Account Integration: Securely connects to banks via OAuth 2.0 APIs (Plaid, Yodlee, TrueLayer).

Real-Time Transaction Sync: Fetches and categorizes transactions from linked accounts

Advanced Data Visualization: Uses Plotly & Streamlit for interactive graphs and reports.

Secure & Scalable: Implements AES-256 encryption, TLS security, and API rate limiting.

Tech Stack

Backend: FastAPI / Flask (Python)

Frontend: Streamlit (for interactive UI)

Database: PostgreSQL / MongoDB

Machine Learning: Isolation Forest, LSTM Autoencoders, DBSCAN

Security: OAuth 2.0, JWT Authentication, AES Encryption

APIs: Plaid, Yodlee, TrueLayer for bank integration

