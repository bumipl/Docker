from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_ip')
def get_public_ip():
    try:
        # Use an external service to get the public IP
        response = requests.get('https://api.ipify.org?format=json')
        response.raise_for_status()  # Raise an error for bad responses
        ip_info = response.json()
        return jsonify(ip=ip_info['ip'])
    except requests.RequestException as e:
        return jsonify(error=f"Error fetching IP: {e}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
