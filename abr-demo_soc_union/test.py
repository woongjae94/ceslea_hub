import pyautogui as pg
import time


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


    def control_shop(self, inin):
        if inin == 'n':
            print("nnnnnn")
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

        elif inin == 'p':
            print("ppppp")
            # next item
            if self.len_points != 0 and self.cur_ptr :
                pg.scroll(-15)
                time.sleep(0.6)
                self.find_all()
                self.cur_ptr += -1
            try:
                px = self.points_list[self.cur_ptr][0] - 100
                py = self.points_list[self.cur_ptr][1] - 50
                pg.moveTo(px, py, 1)
                self.cur_ptr += 1

            except:
                print("error")

        elif inin == 'e':
            pass

        else:
            pass


if __name__ == '__main__':
    control = Shop()
    control.init_shop_page()
    while True:
        ininin = input("nnn : ")
        control.control_shop(ininin)
    print("exit!!!!")

# def init_shop_page():
#     cnt = 0
#     while True:
#         try:
#             find_first = pg.locateOnScreen('screenshot.png', confidence = 0.9)
#             pg.moveTo(find_first[0]-100, find_first[1]-80, 1)
#             print("Found")
#             return True
#         except:
#             cnt += 1
#             if cnt == 5:
#                 return False
#             pg.scroll(-15)
#             print("Not Found")
#             time.sleep(1)
#             continue


        
# def init_shop_page(self):
#         cnt = 0
#         cur_ptr = 0
#         len_points = 0
#         points_list = []
#         while True:
#             try:
#                 find_first = pg.locateOnScreen('screenshot.png', confidence = 0.9)
#                 pg.moveTo(find_first[0] - 100, find_first[1] - 80, 1)
#                 print("Found")
#                 find_all()
#                 break
#             except:
#                 cnt += 1
#                 if cnt == 4:
#                     break
#                 pg.scroll(-15)
#                 print("Not Found")
#                 time.sleep(0.6)
#                 continue

# def find_all():
#     points = list(pg.locateAllOnScreen('screenshot.png', confidence = 0.9))
#     return points


# if __name__ == '__main__':
#     checksum = init_shop_page()
#     if not checksum:
#         print("There is NOT review STAR")
#     else:
#         points = find_all()
#         print("find all, enter n")
#         num = len(points)
#         cur_ptr = 1
#         while True:
#             if num == cur_ptr:
#                 pg.scroll(-18)
#                 break
#             a = input()
#             if a=='n':
#                 x=points[cur_ptr][0]
#                 y=points[cur_ptr][1]
#                 pg.moveTo(x,y,1)
#                 cur_ptr += 1
#             else:
#                 continue
            

