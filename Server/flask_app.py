import io
import json                    
import base64                  
import logging             
import numpy as np
from PIL import Image
import cv2
from flask import Flask, request, jsonify, abort
from aruco_from_img import predict
app = Flask(__name__)          
app.logger.setLevel(logging.DEBUG)
  
  
@app.route("/aruco", methods=['POST'])
def test_method():         
    # print(request.json)      
    if not request.json or 'image' not in request.json: 
        abort(400)
             
    # get the base64 encoded string
    im_b64 = request.json['image']

    # convert it into bytes  
    img_bytes = base64.b64decode(im_b64.encode('utf-8'))

    # convert bytes data to PIL Image object
    img = Image.open(io.BytesIO(img_bytes))

    # PIL image object to numpy array
    img_arr = np.asarray(img)      
    print('img shape', img_arr.shape)
    cv2.imwrite("img.jpg",img_arr)

    out,t1=predict(img_arr)
    return {"output":str(out),"timeout":t1}

def run_server_api():
    app.run(host='0.0.0.0', port=5000)
  
  
if __name__ == "__main__":     
    run_server_api()