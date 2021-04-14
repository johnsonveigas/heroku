from flask import Flask, request, jsonify
import requests
from PIL import Image

app = Flask(__name__)

@app.route("/size", methods=["POST"])
def process_image():
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    
    new_image = img.resize((400, 400))

    return jsonify({'msg': 'success', 'size': [new_image.width, new_image.height]})
   


if __name__ == "__main__":
    app.run(debug=True)
    
    
