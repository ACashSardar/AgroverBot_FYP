import base64
import json                    

import requests


from time import sleep
from picamera import PiCamera
while(1):
    camera = PiCamera()
    camera.resolution = (512,512)
    camera.start_preview()

    sleep(2)
    camera.capture('send.jpg')


    api = 'http://192.168.1.193:5000/aruco'
    image_file = 'send.jpg'
    
    with open(image_file, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps({"image": im_b64, "other_key": "value"})
    response = requests.post(api, data=payload, headers=headers)
    try:
        data = response.json()     
        print(data)                
    except requests.exceptions.RequestException:
            print(response.text)

