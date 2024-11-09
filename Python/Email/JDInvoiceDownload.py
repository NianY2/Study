import poplib
from  urllib import request
from email import policy
from email.parser import BytesParser
from email.header import decode_header, make_header
import re
from xml.dom.minidom import parse


# 定义EmailClient类，用于连接到POP3服务器并从指定的邮件地址获取邮件
class EmailClient:
    # 在初始化函数中，设置POP3服务器的来源、用户、密码和待查询的目标邮件地址
    def __init__(self, host,pop_server_port, user, password, target_email,file_path):
        self.POP3_SSL(host,pop_server_port)
        self.login(user, password)
        self.target_email = target_email
        self.file_path = file_path


    def POP3_SSL(self,pop_server_host,pop_server_port):
        try:
            # 连接pop服务器。如果没有使用SSL，将POP3_SSL()改成POP3()即可其他都不需要做改动
            self.pop_server = poplib.POP3_SSL(host=pop_server_host, port=pop_server_port, timeout=10)
            print("pop3----连接服务器成功，现在将检查用户名")
        except:
            print("pop3----对不起，给定的电子邮件服务器地址连接超时")
            exit(1)

    def login(self,user,password):
        try:
            # 验证邮箱是否存在
            self.pop_server.user(user)
            print("pop3----用户名已存在，现在将检查密码")
        except:
            print("pop3----对不起，给定的电子邮件地址似乎不存在")
            exit(1)
        try:
            # 验证邮箱密码是否正确
            self.pop_server.pass_(password)
            print("pop3----密码正确，现在将列出电子邮件")
        except:
            print("pop3----对不起，给定的用户名似乎不正确")
            exit(1)

    # 定义一个函数，用以清除文件名中的无效字符
    def sanitize_folder_name(self, name):
        invalid_characters = "<>:\"/\\|?*@"
        for char in invalid_characters:  # 遍历所有无效字符
            name = name.replace(char, "_")  # 将无效字符替换为下划线
        return name  # 返回清理后的名称

    # 定义一个函数，用以提取邮件的payload（有效载荷，即邮件主体内容）
    def get_payload(self, email_message):
        if email_message.is_multipart():  # 判断邮件是否为多部分邮件
            for part in email_message.iter_parts():  # 如果是，则遍历其中的每一部分
                content_type = part.get_content_type()  # 获取该部分的内容类型
                if content_type == 'text/html':  # 如果内容类型为HTML，则返回该部分内容
                    return part.get_content()
                elif content_type == 'text/plain':  # 如果内容类型为纯文本，则返回该部分内容
                    return part.get_content()
        elif email_message.get_content_type() == 'text/html':  # 如果邮件非多部分形式，且为HTML类型，则返回邮件内容
            return email_message.get_content()
        elif email_message.get_content_type() == 'text/plain':  # 如果邮件非多部分形式，且为纯文本类型，则返回邮件内容
            return email_message.get_content()

    def fetch_email(self):
        # 邮箱中其收到的邮件的数量
        email_count = len(self.pop_server.list()[1])
        print("email_num: ",email_count)
        # list()返回所有邮件的编号:
        _, mails, _ = self.pop_server.list()

        # for i in range(len(mails),0,-1):
        for i in range(len(mails),1, -1):
            # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
            resp, lines, octets = self.pop_server.retr(i)
            email_content = b'\r\n'.join(lines)  # 将所有行连接成一个bytes对象
            # 解析邮件内容
            email_parser = BytesParser(policy=policy.default)  # 创建一个邮件解析器
            email = email_parser.parsebytes(email_content)  # 解析邮件内容，返回一个邮件对象

            # 解析邮件头部信息并提取发件人信息
            email_from = email.get('From').strip()  # 获取发件人信息，并去除尾部的空格
            email_from = str(make_header(decode_header(email_from)))  # 解码发件人信息，并将其转换为字符串
            print(email_from)
            if email_from == self.target_email:  # 如果发件人地址与指定的目标邮件地址一致，对邮件进行处理
                # 解析邮件时间
                email_time = email.get('Date')  # 获取邮件时间

                # 提取邮件正文
                email_body = self.get_payload(email)  # 获取邮件正文
                if self.check_invoice(email_body):
                    self.download_invoice(email_body,f"{i}.pdf")

        #         # return email_body, email_time  # 返回邮件正文和时间
        #
        # print("No new emails from", self.target_email)  # 如果没有从目标邮件地址收到新邮件，打印相应信息
        # return None, None  # 返回None

    def download_invoice(self, body, filename):
        pattern = r'href="([^"]*)">发票PDF文件下载</a>'
        match = re.search(pattern, body)
        if match:
            # 提取URL
            url = match.group(1)
            print("找到的URL是:", "".join(url.split("amp;")))
            try:
                request.urlretrieve("".join(url.split("amp;")), f"{self.file_path}\\{filename}")
            except Exception as e:
                print("Error downloading:", e)


    def check_invoice(self, body) -> bool:
        """读取XML文件，判断是否是广州的发票"""
        pattern = r'href="([^"]*)">发票XML文件下载</a> '
        match = re.search(pattern, body)
        if match:
            # 提取URL
            url = match.group(1)
            print("找到的URL是:", "".join(url.split("amp;")))
        try:
            file_name = f"{self.file_path}\\xml_file_test.xml"
            request.urlretrieve("".join(url.split("amp;")),file_name)
            dom = parse(file_name)
            # 获取文档元素对象
            data = dom.documentElement
            seller_addr = data.getElementsByTagName("EInvoiceData")[0].getElementsByTagName("SellerInformation")[
                0].getElementsByTagName("SellerAddr")[0].childNodes[0].nodeValue
            print(seller_addr,"广州" in seller_addr)
            if "广州" in seller_addr:
                return  True
        except Exception as e:
            print("Error parsing XML:", e)
        return  False
    def close(self):
        # 关闭连接
        self.pop_server.close()
if __name__ == '__main__':
    client = EmailClient('pop.qq.com',995, '1871263099@qq.com',input("请输入你的授权码："), '"京东JD.com" <customer_service@jd.com>',"D:\\Test")
    client.fetch_email()
    client.close()

