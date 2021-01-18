import socket
import argparse
#import threading
#import multiprocessing
import time
import copy
import json
import requests
from pytz import timezone
from datetime import datetime

# control
import phue_lamp
import control_web

client_name = ['gesture', 'action', 'head']
headers = {'Content-Type': 'application/json; charset=utf-8'}
# Gesture list [ Swiping Up / Sliding Two Fingers Up / Swiping Left / Thumb Up / Sliding Two Fingers Right / Stop Sign
#                Sliding Two Fingers Left / Sliding Two Fingers Down / Rolling Hand Backward / Doing other things
#                Swiping Right / Swiping Down / Thumb Down ]
# Action list [ sitting / standing / drinking / brushing / playing instrument / speaking
#               waving a hand / working / coming / leaving / talking on the phone
#               stretching / nodding off / reading / blow nose ]
# Head pose list [ FarLeft / Left / Center / Right / FarRight ]
# Head pose list { ~left : lamp , center : pc , right~ : pc }

today = lambda: datetime.now(timezone('Asia/Seoul')).strftime('%Y-%m-%d')
time_now = lambda: datetime.now(timezone('Asia/Seoul')).strftime('%H:%M:%S')
mills = lambda: int(round(time.time() * 1000))

connect_phue = False

def add_log(msg):
    cur_time = time_now()
    cur_day = today()
    with open('./log_test/' + cur_day + ".txt", "a") as f:
        f.write(cur_day + ' | '+ cur_time + ' | (mode:{}) | (gesture:{}) | (action:{}) | (headpose:{}) | (device:{})\n'.format( \
            msg[0], msg[1], msg[2], msg[3], msg[4]))

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    return s.getsockname()[0]

if __name__ == '__main__':
    request_ip_address = "http://192.168.0.22:59099/"
    Hue_ip = '192.168.0.19'
    device = 'None'
    #device = [None lamp pc shop]
    control_mode = 'Action'
    #control_mode = [ Action Gesture ]
    shop_web_open =  'false'

    # connect phue
    if connect_phue:
        wait_for_phue_connect=input("press phue link button and then press enter : ")
        device_lamp = phue_lamp.Phue(Hue_ip)
        print(device_lamp.get_light_state())
        if device_lamp.get_light_state():
            device_lamp.power_switch(False)

    # when web page is opened
    device_pc = control_web.Web()

    # when shopping host is called
    device_shop = control_web.Shop()

    while True:
        pre_gesture = "None"
        pre_action = "None"
        pre_head = "None"
        reset_time = 0
        prev_time = mills()
        pre_gesture = 'None'
        if_pre_reading = False
        pre_web_control = False
        try:
            while True:
                # receive data from flask
                now_time = mills()

                if (now_time - prev_time) > 1000:
                    try:
                        shop_open_from_chat = requests.get(request_ip_address + "get_value")
                        #print(shop_open_from_chat.text)
                        shop_web_open = shop_open_from_chat.text
                    except:
                        print("local flask closed")

                    try:
                        gesture_temp = requests.get(request_ip_address + "get_gesture")
                        gesture_msg = gesture_temp.text
                    except:
                        gesture_msg = "NoFlask"

                    try:
                        action_temp = requests.get(request_ip_address + "get_action")
                        action_msg = action_temp.text
                    except:
                        action_msg = "NoFlask"

                    try:
                        head_temp = requests.get(request_ip_address + "get_head")
                        head_msg = head_temp.text
                    except:
                        head_msg = "NoFlask"

                    try:
                        requests.get('http://192.168.0.22:3001/api/v1/actions/action/{}/Mode:{}_Gesture:{}_Action:{}_Head:{}_Device:{}'.format( \
                            'home', control_mode, gesture_msg, action_msg, head_msg, device))
                        print('Mode: ', control_mode, ' |Gesture: ',gesture_msg,' |Action: ', action_msg,' |Head: ', head_msg, ' |Device: ', device)
                        print("BackEnd Signal { web_open:", shop_web_open, " |  }")
                    except:
                        print("http connect unstable... ")
                        print('** Mode: ', control_mode, ' |Gesture: ',gesture_msg,' |Action: ', action_msg,' |Head: ', head_msg, ' |Device: ', device)
                        print("** BackEnd Signal { web_open:", shop_web_open, " |  }")
                    prev_time = now_time

                    if shop_web_open == "shop":
                        if not pre_web_control:
                            pre_web_control = True
                            time.sleep(4)
                            device_shop.init_shop_page()
                            device = "shop"
                            control_mode = 'Gesture'
                    elif shop_web_open == "web":
                        if not pre_web_control:
                            pre_web_control = True
                            time.sleep(4)
                            device = "pc"
                            control_mode = 'Gesture'
                    elif shop_web_open == "False":
                        if pre_web_control:
                            pre_web_control = False
                            device = 'None'
                            control_mode = 'Action'
                    
                    else:
                        pre_web_control = False
                        device = 'None'
                        control_mode = 'Action'


        # Gesture list [ Swiping Up / Sliding Two Fingers Up / Swiping Left / Thumb Up / Sliding Two Fingers Right / Stop Sign
        #                Sliding Two Fingers Left / Sliding Two Fingers Down / Rolling Hand Backward / Doing other things
        #                Swiping Right / Swiping Down / Thumb Down ]
        # Action list [ sitting / standing / drinking / brushing / playing instrument / speaking
        #               waving a hand / working / coming / leaving / talking on the phone
        #               stretching / nodding off / reading / blow nose ]
        # device = [None lamp pc shop]          
                    if control_mode == 'Action':

                        if action_msg == 'reading':
                            # light on
                            if connect_phue:
                                if not device_lamp.get_light_state():
                                    device_lamp.power_switch(True)
                                device_lamp.bri_value = 254
                                device_lamp.change_bri()
                                device_lamp.change_color_rgb([0.9, 0.7, 0.2])
                            control_mode = 'Gesture'
                            device = 'lamp'
                            if_pre_reading = True

                        elif action_msg == 'stretching':
                            if if_pre_reading:
                                if connect_phue:
                                    if device_lamp.get_light_state():
                                        device_lamp.power_switch(False)
                                control_mode = 'Action'
                                device = 'None'
                                if_pre_reading = False
                        
                        else:
                            #
                            pass    

                        if gesture_msg == 'Thumb Up':
                            control_mode = 'Gesture'
                            if head_msg =='FarLeft' or head_msg == 'Left':
                                device = 'lamp'
                            elif head_msg == 'Center':
                                device = 'pc'
                            elif head_msg == 'FarRight' or head_msg == 'Right':
                                device = 'pc'
                            else:
                                device = 'None'
                                control_mode = 'Action'

                    elif control_mode == 'Gesture':
                        
                        if action_msg == 'stretching':
                            if if_pre_reading:
                                if connect_phue:
                                    if device_lamp.get_light_state():
                                        device_lamp.power_switch(False)
                                control_mode = 'Action'
                                device = 'None'
                                if_pre_reading = False

                        if gesture_msg == 'Thumb Down':

                            control_mode = 'Action'
                            device = 'None'
                            continue

                        if device == 'lamp':
                            if connect_phue:
                                device_lamp.control_lamp(pre_gesture, gesture_msg)
                            #print("lamp")
                            continue

                        elif device == 'pc':
                            device_pc.control_pc(pre_gesture, gesture_msg)
                            #print("pc")

                        elif device == 'shop':
                            device_shop.control_shop(pre_gesture, gesture_msg)
                            #print("shop")

                        else:
                            print("there is no selected device")
                            control_mode = 'Action'
                    
                    else:
                        control_mode = 'Action'
                        device = 'None'
                    
                    pre_gesture = gesture_msg
                    pre_action = action_msg
                    pre_head = head_msg

                    reset_time += 1
                    if reset_time > 5:
                        for client in client_name:
                            try:
                                requests.post(request_ip_address + client, headers = headers, data = json.dumps({'flags':'None'}))
                            except:
                                print("Flask Server Closed -- response in *reset_time*")
                        reset_time = 0
        
        except KeyboardInterrupt:
            while True:
                choice = input("\n#############\n    q : quit\n    r : restart\n#############\nq or r :")
                if choice == 'q':
                    break
                elif choice == 'r':
                    break
                else:
                    continue
            if choice == 'q':
                break
            else:
                continue
