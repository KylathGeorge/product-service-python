from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Get PORT from environment or default to 3030
PORT = int(os.getenv("PORT", 3030))

# Create the Flask app
app = Flask(__name__)
CORS(app, resources={r"/products": {"origins": "*"}}, methods=["GET"])  # Allow any origin, only GET

# Define the /products route
@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
