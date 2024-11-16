"""
获取课程表
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple requests
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple lxml
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple rsa
pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple six
"""
import requests
import time
from lxml import etree
from hex2b64 import HB64
import RSAJS

class Longin():

    def __init__(self,user,password,login_url,login_KeyUrl):
        # 初始化程序数据
        self.Username = user
        self.Password = password
        nowTime = lambda:str(round(time.time()*1000))
        self.now_time = nowTime()

        self.login_url = login_url
        self.login_Key = login_KeyUrl

    def Get_indexHtml(self):
        # 获取教务系统网站
        self.session = requests.Session()
        # self.session.headers.update({
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
        #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #     "Accept-Encoding": "gzip, deflate",
        #     "Accept-Language": "zh-CN,zh;q=0.9",
        #     "Cache-Control": "max-age=0",
        #     "Connection": "keep-alive",
        #     "Referer": self.login_url+ self.now_time,
        #     "Upgrade-Insecure-Requests": "1"
        # })
        self.response = self.session.get(self.login_url+ self.now_time).content.decode("utf-8")

    def Get_csrftoken(self):
        # 获取到csrftoken
        lxml = etree.HTML(self.response)
        self.csrftoken = lxml.xpath("//input[@id='csrftoken']/@value")[0]

    def Get_PublicKey(self):
        # 获取到加密公钥
        key_html = self.session.get(self.login_Key + self.now_time)
        key_data = key_html.json()
        self.modulus = key_data["modulus"]
        self.exponent = key_data["exponent"]

    def Get_RSA_Password(self):
        # 生成RSA加密密码
        rsaKey = RSAJS.RSAKey()
        rsaKey.setPublic(HB64().b642hex(self.modulus),HB64().b642hex(self.exponent))
        self.enPassword = HB64().hex2b64(rsaKey.encrypt(self.Password))

    def Longin_Home(self):
        # 登录信息门户,成功返回session对象
        self.Get_indexHtml()
        self.Get_csrftoken()
        self.Get_PublicKey()
        self.Get_RSA_Password()
        login_data = [("csrftoken", self.csrftoken),("yhm", self.Username),("mm", self.enPassword),("mm", self.enPassword)]
        login_html = self.session.post(self.login_url + self.now_time,data=login_data)
        print(self.session.cookies)
        # 当提交的表单是正确的，url会跳转到主页，所以此处根据url有没有跳转来判断是否登录成功
        if login_html.url.find("login_slogin.html") == -1: # -1没找到，说明已经跳转到主页
            print("登录成功")
            return self.session
        else:
            print("用户名或密码不正确，登录失败")
            exit()

class TimeTable():
    def __init__(self,session,table_url):
        data = {"xnm":2024,"xqm":3}
        table_info = session.post(table_url,data = data).json()
        # print(table_info)
        # x = input("回车")
        kbList = table_info["kbList"]
        for kb in kbList:
            print(kb["kcmc"],end="\t\t\t")
            print(kb["jcor"],end="\t")
            print(kb["cdmc"],end="\t")
            print(kb["xqjmc"],end="\t")
            print(kb["zcd"],end="\t")
            print("\n")

if __name__ == "__main__":
    # 登录API
    login_url = "http://jwxt.gcc.edu.cn/xtgl/login_slogin.html?time="
    # 请求PublicKey的URL
    login_KeyUrl = "https://jwxt.gcc.edu.cn/xtgl/login_getPublicKey.html?time="
    # 登录后的课表URL
    table_url = "http://jwxt.gcc.edu.cn/kbcx/xskbcx_cxXsgrkb.html"
    num = input("学号：")
    pwd = input("密码：")
    zspt = Longin(num, pwd, login_url, login_KeyUrl)
    response_cookies = zspt.Longin_Home()
    table = TimeTable(response_cookies, table_url)