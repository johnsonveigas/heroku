from flask import Flask, request, jsonify,render_template
import requests
from PIL import Image
from file import ImgId
import pyrebase
import os



config={
"apiKey": "AIzaSyBvlJpkV7rcYwbx3wNEBARKvrpHMBALXuw",
    "authDomain": "allinonetools.firebaseapp.com",
   "databaseURL": "https://allinonetools-default-rtdb.firebaseio.com",
    "projectId": "allinonetools",
   "storageBucket": "allinonetools.appspot.com",
}

firebase = pyrebase.initialize_app(config)
app = Flask(__name__)
storage=firebase.storage()


@app.route('/')
def home():
	return render_template('index.html')
	

@app.route("/imgresize/<int:width>&<int:height>", methods=["POST"])
def process_image(height,width):
    file = request.files['image']
    # Read the image via file.stream
    img = Image.open(file.stream)
    new_image = img.resize((width,height))
    img_url=ImgId()
    imagechild="resizeimages"
    try:
        	   os.mkdir(imagechild)  

    except OSError as error:
        	  pass
        	  
    imagechilda=imagechild+"/"+img_url+".jpg"
    print(imagechilda)
    new_image.save(imagechilda)
    open2=Image.open(imagechilda)
    
    storage.child(imagechild).put(open2.filename)
    imageurl=storage.child(imagechild).get_url(None)
    
    os.remove(imagechilda)
    
    

    return jsonify(
    {'Original Size':[img.width,img.height],'msg': 'success', 'size': [new_image.width, new_image.height],'url':imageurl })
   


if __name__ == "__main__":
    app.run(debug=True)
    
    
