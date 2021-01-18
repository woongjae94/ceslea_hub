from TF_model_cam import TFModel, CAM

import requests
import json
import numpy as np
import time
import socket
import cv2
#from socket import *
#import threading
#import multiprocessing

# rule of communication
headers = {'Content-Type': 'application/json; charset=utf-8'}
#data = {'flags':'data'}
# requests.post('ip_address', headers = headers, data = json.dumps(data))

request_ip_address = "http://192.168.0.22:59099/"
    

class Gesture:
    def main_loop(self):
        while True:
            self.run_demo()

    def run_demo(self):
        result = 'None'; confidence = 0.0
        frames = cam.get_frames(num=cam.args.video_length,
                                  fps=cam.args.fps,
                                  cam=0)
        
        if not frames:
            print("LostContact")
            try:
                requests.post(request_ip_address + 'gesture', headers = headers, data = json.dumps({'flags':'LostContact'}))
            except:
                print("Flask Server Closed, Lost Contact")
            time.sleep(5)
            pass

        if frames and cam.center_detect and cam.move_detect:
            #cv2.imshow("frameeee", frames[0])
            #cv2.waitKey(1)
            result, confidence, top_3 = model.run_demo_wrapper(np.expand_dims(frames,0))
            print("result :{}, confidence:{}, top_3:({})".format(result, confidence, top_3))
            
            if confidence >0.4 and result == "Doing other things":
                result = top_3[0]

        if confidence > 0.4:
            try:
                requests.post(request_ip_address + 'gesture', headers = headers, data = json.dumps({'flags':result}))
            except:
                print("Flask Server Closed")

if __name__ == '__main__':
    print("## load TF model")
    model = TFModel()
    print("## load complete\n## set camera")
    cam = CAM()
    print("## setting complete\n")
    multi_device = Gesture()

    print("## start demo")
    multi_device.main_loop()
