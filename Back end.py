from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load CSV Data
data_file = r"C:\Users\aadih\Downloads\synthetic_financial_transactions.csv"
df = pd.read_csv(data_file)

@app.route('/')
def index():
    return jsonify({"message": "Backend running with CSV data!"})

@app.route('/financial_data', methods=['GET'])
def get_financial_data():
    return jsonify(df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)