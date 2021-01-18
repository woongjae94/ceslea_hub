import pyautogui as pg
import time
#from selenium import webdriver


class Web():
    def __init__(self):
        #self.options = webdriver.ChromeOptions()
        #self.options.add_argument('--no-sandbox')
        #self.options.add_argument("lang=ko_KR")
        #self.options.add_argument("disable-gpu")
        #self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #self.browser = None
        self.screenW, self.screenH = pg.size()
        #self.tabs = None
        #self.my_tab_num = -1

    def control_pc(self, pre_gesture, now_gesture):
        if pre_gesture == now_gesture:
            pass

        else:
            if now_gesture == 'Thumb Up':
                # browser open
                # if self.my_tab_num == -1:
                #     self.browser = webdriver.Chrome(chrome_options=self.options, executable_path = './chromedriver')
                #     self.browser.set_window_position(self.screenW//2, 0)
                #     self.browser.set_window_size(self.screenW//2, self.screenH)
                #     self.browser.get('http://google.com')
                #     self.tabs = self.browser.window_handles
                #     self.my_tab_num += 1
                # else:
                #     self.browser.execute_script('window.open("http://google.com", "_blank");')
                #     self.tabs = self.browser.window_handles
                #     self.my_tab_num =len(self.browser.window_handles) + 1
                # click
                pg.click()
                pass

            elif now_gesture == 'Sliding Two Fingers Up':
                # mouse up
                cur_x, cur_y = pg.position()
                pg.moveTo(cur_x, cur_y -100, 1)
                if not pg.onScreen(cur_x, cur_y -100):
                    pg.moveTo(cur_x, 0)

            elif now_gesture == 'Stop Sign':
                # exit
                # self.tabs = self.browser.window_handles
                # for i in range(self.my_tab_num, -1, -1):
                #     self.browser.switch_to_window(self.tabs[i])
                #     self.browser.close()
                # self.browser = None
                # self.tabs = None
                # self.my_tab_num = 0
                pass

            elif now_gesture == 'Swiping Right':
                # mouse righr fast
                cur_x, cur_y = pg.position()
                pg.moveTo(cur_x + 250, cur_y, 1)
                if not pg.onScreen(cur_x + 250, cur_y):
                    pg.moveTo(self.screenW, cur_y)
                
            elif now_gesture == 'Swiping Left':
                # mouse left fast
                cur_x, cur_y = pg.position()
                pg.moveTo(cur_x - 250, cur_y, 1)
                if not pg.onScreen(cur_x - 250, cur_y):
                    pg.moveTo(0, cur_y)

            elif now_gesture == 'Sliding Two Fingers Right':
                # mouse right
                cur_x, cur_y = pg.position()
                pg.moveTo(cur_x + 100, cur_y, 1)
                if not pg.onScreen(cur_x + 100, cur_y):
                    pg.moveTo(self.screenW, cur_y)
            
            elif now_gesture == 'Sliding Two Fingers Left':
                # mouse left
                cur_x, cur_y = pg.position()
                pg.moveTo(cur_x - 100, cur_y, 1)
                if not pg.onScreen(cur_x - 100, cur_y):
                    pg.moveTo(0, cur_y)

            elif now_gesture == 'Sliding Two Fingers Down':
                # mouse down
                cur_x, cur_y = pg.position()
                pg.moveTo(cur_x, cur_y +100, 1)
                if not pg.onScreen(cur_x, cur_y +100):
                    pg.moveTo(cur_x, self.screenH)

            elif now_gesture == 'Swiping Up':
                # close tab
                # self.browser.switch_to_window(self.tabs[self.my_tab_num])
                # self.browser.close()
                # self.my_tab_num += -1
                # if self.my_tab_num<0:
                #     self.my_tab_num = 0
                # scroll Down
                pg.scroll(20)

            elif now_gesture == 'Swiping Down':
                # scroll Up
                pg.scroll(-20)

            elif now_gesture == 'Rolling Hand Backward':
                # go back
                #self.browser.back()
                
                pass

            else:
                #
                pass


class Shop():
    def __init__(self):
        self.screenW, self.screenH = pg.size()
        self.cur_ptr = 0
        self.len_points = 0
        self.points_list = []

    def init_shop_page(self):
        cnt = 0
        self.cur_ptr = 0
        self.len_points = 0
        self.points_list = []
        while True:
            try:
                find_first = pg.locateOnScreen('screenshot.png', confidence = 0.9)
                pg.moveTo(find_first[0] - 100, find_first[1] - 50, 1)
                print("Found")
                self.find_all()
                print(self.len_points)
                break
            except:
                cnt += 1
                if cnt == 4:
                    break
                pg.scroll(-15)
                print("Not Found")
                time.sleep(0.6)
                continue
    
    def find_all(self):
        try:
            self.points_list = list(pg.locateAllOnScreen('screenshot.png', confidence = 0.9))
            self.len_points = len(self.points_list)
            self.cur_ptr = 0
        except:
            self.len_points = 0
            self.cur_ptr = 0


    def control_shop(self, pre_gesture, now_gesture):
        if pre_gesture == now_gesture:
            pass

        else:
            if now_gesture == 'Sliding Two Fingers Up':
                #
                pass

            elif now_gesture == 'Stop Sign':
                # 
                pass

            elif now_gesture == 'Swiping Right':
                # prev item
                pass

                

            elif now_gesture == 'Swiping Left':
                # next item
                if self.len_points == self.cur_ptr+1:
                    pg.scroll(-15)
                    time.sleep(0.6)
                    self.find_all()
                try:
                    self.cur_ptr += 1
                    px = self.points_list[self.cur_ptr][0] - 100
                    py = self.points_list[self.cur_ptr][1] - 50
                    pg.moveTo(px, py, 1)

                except:
                    print("error")
                    pass


            
            elif now_gesture == 'Sliding Two Fingers Right':
                # 
                pass
            
            elif now_gesture == 'Sliding Two Fingers Left':
                # 
                pass

            elif now_gesture == 'Sliding Two Fingers Down':
                # 
                pass

            elif now_gesture == 'Swiping Up':
                #
                pass

            elif now_gesture == 'Swiping Down':
                #
                pass

            elif now_gesture == 'Rolling Hand Backward':
                # 
                pass

            elif now_gesture == 'Thumb Up':
                #
                pass

            else:
                #
                pass