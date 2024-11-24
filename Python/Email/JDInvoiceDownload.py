import poplib
from  urllib import request
from email import policy
from email.parser import BytesParser
from email.header import decode_header, make_header
from email.headerregistry import UniqueDateHeader
from  datetime import  datetime
import re,os
from xml.dom.minidom import parse


# 定义EmailClient类，用于连接到POP3服务器并从指定的邮件地址获取邮件
class JDInvoiceDownload:
    # 在初始化函数中，设置POP3服务器的来源、用户、密码和待查询的目标邮件地址
    def __init__(self, host,pop_server_port, user, password, target_email,file_path,target_addr=None,target_time=None):
        """
        初始化EmailClient类的新实例。
        参数:
        - host: 邮件服务器的主机名或IP地址。
        - pop_server_port: POP3服务器的端口号。
        - user: 用户名，用于登录邮件服务器。
        - password: 用户密码，用于登录邮件服务器。
        - target_email: 目标电子邮件地址。
        - file_path: 附件的文件路径。
        """
        self.POP3_SSL(host,pop_server_port)
        self.login(user, password)
        self.target_email = target_email
        self.file_path = file_path
        self.target_addr = target_addr
        self.target_time = target_time
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

        # for i in range(len(mails),len(mails)-1,-1):
        for i in range(len(mails),1, -1):
            # 通过retr(index)读取第index封邮件的内容；这里读取最后一封，也即最新收到的那一封邮件
            resp, lines, octets = self.pop_server.retr(i)
            email_content = b'\r\n'.join(lines)  # 将所有行连接成一个bytes对象
            # 解析邮件内容
            email_parser = BytesParser(policy=policy.default)  # 创建一个邮件解析器
            email = email_parser.parsebytes(email_content)  # 解析邮件内容，返回一个邮件对象
            email_time = datetime.strptime(self.get_email_time(email), "%Y-%m-%d")
            target_time = datetime.strptime(self.target_time, "%Y-%m-%d")
            if email_time < target_time and  self.check_email_from(email):  # 如果发件人地址与指定的目标邮件地址一致，对邮件进行处理
                email_body = self.get_payload(email)  # 获取邮件正文

                if self.check_invoice_target_addr(email_body):
                    self.download_invoice(email_body,f"{i}.pdf",email_time)
            print("--------------------------------------------------------------------------------------")

    def check_email_from(self, email) -> bool:
        """
        对比发件人地址与指定的目标邮件地址是否一致
        :param email:
        :return:
        """
        # 解析邮件头部信息并提取发件人信息
        email_from = email.get('From').strip()  # 获取发件人信息，并去除尾部的空格
        email_from = str(make_header(decode_header(email_from)))  # 解码发件人信息，并将其转换为字符串
        print("发件人地址:", email_from," ",email_from == self.target_email)
        return  email_from == self.target_email


    def get_email_time(self,email):
        """
        解析邮件时间
        :param email:
        :return:
        """
        # 解析邮件时间
        email_time: UniqueDateHeader = email.get('Date')  # 获取邮件时间
        # 获取年月日
        return   email_time.datetime.strftime("%Y-%m-%d")

    def download_invoice(self, body, filename,email_time):
        """
        下载发票
        :param body:
        :param filename:
        :param email_time:
        :return:
        """
        pattern = r'href="([^"]*)">发票PDF文件下载</a>'
        match = re.search(pattern, body)
        if match:
            # 提取URL
            url = match.group(1)
            print("找到的-PDF-URL是:", "".join(url.split("amp;")))
            try:
                file_path = f"{self.file_path}\\{email_time}"
                # 判断文件夹是否存在
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                request.urlretrieve("".join(url.split("amp;")), f"{file_path}\\{filename}")
            except Exception as e:
                print("Error downloading:", e)


    def check_invoice_target_addr(self, body) -> bool:
        """读取XML文件，判断是否是某个地方的发票"""
        pattern = r'href="([^"]*)">发票XML文件下载</a> '
        match = re.search(pattern, body)
        if match:
            # 提取URL
            url = match.group(1)
            print("找到的-XML-URL是:", "".join(url.split("amp;")))
        try:
            file_name = f"{self.file_path}\\xml_file_test.xml"
            request.urlretrieve("".join(url.split("amp;")),file_name)
            dom = parse(file_name)
            # 获取文档元素对象
            data = dom.documentElement
            seller_addr = data.getElementsByTagName("EInvoiceData")[0].getElementsByTagName("SellerInformation")[
                0].getElementsByTagName("SellerAddr")[0].childNodes[0].nodeValue
            print("seller_addr:",seller_addr," "+self.target_addr in  seller_addr)
            if not self.target_addr in  seller_addr:
                return  False

        except Exception as e:
            print("Error parsing XML:", e)

        return  True

    def close(self):
        # 关闭连接
        self.pop_server.close()

if __name__ == '__main__':
    client = JDInvoiceDownload(
        host='pop.qq.com', # 邮箱服务器地址(qq邮箱无需改)
        pop_server_port=995, # 端口号(qq邮箱无需改)
        user=input("请输入你的邮箱地址："), # 邮箱账号
        password=input("请输入你的授权码："), # 授权码
        target_email='"京东JD.com" <customer_service@jd.com>', # 发件人
        file_path="D:\\Test", # 保存文件路径
        target_addr="广州", # 发票地址（不需要判断设置为None即可）
        target_time="2024-11-11" # 发票时间 （不需要判断设置为None即可）
    )
    client.fetch_email()
    client.close()

