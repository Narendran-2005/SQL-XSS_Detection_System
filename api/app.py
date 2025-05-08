import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from flask_cors import CORS
from input_sanitizer import detect_sql_injection, detect_xss_attack, load_payloads

app = Flask(__name__)
CORS(app) 

sql_payloads = load_payloads("payloads/sql_payload.txt")
xss_payloads = load_payloads("payloads/xss_payload.txt")

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    user_input = data.get('input', '')

    result = {
        'sql_injection': detect_sql_injection(user_input, sql_payloads),
        'xss_attack': detect_xss_attack(user_input, xss_payloads),
        'message': 'Detection complete'
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)