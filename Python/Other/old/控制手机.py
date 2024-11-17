import uiautomator2 as u2
import time


def main():
    android = Android()# 只有一个设备时//使用设备唯一标志码d = u2.connect('ANP4C20513001456')
    # android.drag(90)
    start = time.time()
    while True:
        remain = int(time.time() - start)
        print(remain)
        android.long_click(627,2202,3)
        # android.onedrag()
        android.click(548,1744)
        android.click(559,1910)

class Android():
    def __init__(self,id=None):
        self.d = u2.connect(id)
    def onedrag(self):
        self.d.drag(563,1568,571,1143,0.2)#滑动屏幕 x,y->x,y
    def drag(self,t:float)->None:
        "多次滚动"
        time.sleep(0.5)
        start = time.time()
        while True:
            remain = int(t - (time.time() - start))
            print(remain)
            if remain <= 0:
                break
            self.d.drag(563,1568,571,1143,0.2)#滑动屏幕 x,y->x,y
            time.sleep(1)
    def click(self,x,y):
        time.sleep(0.5)
        self.d.click(x,y)
    def long_click(self,x,y,t):
        time.sleep(0.5)
        self.d.long_click(x,y,t)
# def FQmain():
#     "番茄小说3点刷"
#     android = Android()
#     android.click(952,1628)  # 增加次数
    
#     android.click(904,1467) # 逛街
#     android.drag(65) # 开始滚动
#     android.click(100,130) # 退出

#     android.click(925,1712)#浏览爆款
#     android.drag(95) # 开始滚动
#     android.click(68,206) # 退出

#     android.click(946,1962)#广告
#     time.sleep(65)
#     android.click(990,162)#退出



if __name__ == "__main__":
    main()
    # FQmain()
