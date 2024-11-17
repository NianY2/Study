# 引用uiautomator2包
# 阅读文章安装 uiautomator2 adb（android调试桥）（Android Debug Bridge）
# https://blog.csdn.net/weixin_40901068/article/details/121242489
# 打开开发者模式
import uiautomator2 as u2
import time
# 使用设备唯一标志码链接设备，其中9phqaetw是通过adb获取的设备标志码
d = u2.connect("")
i = 0
while True:
    # d.swipe(519,1552,582,809,0.1)
    d.swipe(519,1552,582,809,0.1) # 如果不能滑动修改这个值
    # time.sleep(0.5)
    # d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/ekj"]/android.widget.ImageView[1]').click()
    # d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/ekj"]/android.widget.ImageView[1]').click()
    # d.xpath('//*[@resource-id="com.ss.android.ugc.aweme:id/ey0"]/android.widget.ImageView[1]').click()
    # d.click(974,1212)
    time.sleep(1)
    i+=1
    print(i,"条")