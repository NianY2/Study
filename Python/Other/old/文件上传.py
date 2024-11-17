

import paramiko
import time
import os
import threading

def progressBar():
    global sc_size,sc_name
    size_all = 0
    for root, dirs, files in os.walk(".", topdown=False):
        if ".git" in root:
            continue
        for name in files:
            localpath =  root+ "\\" + name
            localpath = localpath.replace("\\","/")
            size  =  os.path.getsize(localpath)
            size_all = size + size_all
    start = time.perf_counter()
    print(("*"* 55)  + "任务开始" + ("*"* 55))
    while True:
        progress = (sc_size / size_all) * 100
        finsh = "▓" * int(progress)
        need_do = "-" * (100 - int(progress))
        dur = time.perf_counter() - start
        
        file_name = str(sc_name)
        if len(file_name) > 20:
            file_name = file_name[0:17]
            file_name = file_name + "···"
        else:
            while len(file_name)!=20:
                file_name=file_name + " "
            
        print("\r{:^3.0f}%[{}->{}]{:.2f}s（共 {} B,完成 {} B）{}".format(progress, finsh, need_do, dur,size_all,sc_size-1,file_name), end="")
        if(progress >= 100):
            print("\n"+("*"* 55)  + "任务完成" + ("*"* 55))
            break


global sc_size,sc_name
sc_size = 1
sc_name = ""
threading.Thread(target=progressBar).start()

time_start =  time.perf_counter()
pathHome = "/our/Test/"
# pathHome = "/our/DjangoServer/CarCarServer/" #服务器存放文件地址
hostname = '121.37.66.46'#服务器地址
username = 'root'
password = 'Remote.666'
tran = paramiko.Transport(hostname,22)

#连接SSH服务端
tran.connect(username=username,password=password)
#获取SFTP实例
sftp = paramiko.SFTPClient.from_transport(tran)

#创建文件夹时会使用到
sshclt = paramiko.SSHClient()
sshclt.set_missing_host_key_policy(paramiko.AutoAddPolicy())
sshclt.connect(hostname=hostname, port=22, username=username, password=password,
            allow_agent=False, look_for_keys=False)

git_num = 0
file_num = 0


for root, dirs, files in os.walk(".", topdown=False):
    if ".git" in root:
        git_num = git_num + 1
        # print("git文件取消上传,第",git_num,"个")
        continue

    for name in files:
        #检查路径中的文件夹是否存在，不存在则创建
        try:
            remotepath=pathHome +root#上传对象保存的文件路径
            remotepath = remotepath.replace(".\\","")
            remotepath = remotepath.replace("/.","/")
            remotepath = remotepath.replace("\\","/")
            sftp.stat(remotepath)
        except Exception as e:
                sshclt.exec_command("mkdir -p %s"%remotepath)
                # print("创建路径"+root)
                
        # 上传文件
        localpath =  root+"/" + name
        localpath = localpath.replace("\\","/")
        remotepath = remotepath + "/" + name
        
        sftp.put(localpath,remotepath)
        size  =  os.path.getsize(localpath)
        sc_size = sc_size+size
        sc_name = name

time_end =  time.perf_counter()

tran.close()
