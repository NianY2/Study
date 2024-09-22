import json
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    group = 'default'
    def websocket_connect(self, message):
        
        # 连接请求
        # 允许连接
        print("web_socket连接请求")
        self.accept()
        self.group = self.scope['url_route']['kwargs'].get('group', 'default')
        # print(f"群号:{group}")
        print("web_socket连接成功")

        # 拒绝连接
        # raise StopConsumer()

        # 加入连接对象到缓存

        # 异步转同步
        async_to_sync(self.channel_layer.group_add)(self.group, self.channel_name)
        

    def websocket_receive(self, message):
        # 接收数据
        print(message)
        # 通知组内所有人
        async_to_sync(self.channel_layer.group_send)(self.group,{
            "type":"xx.oo",
            "message":message
        })
        # 服务端主动断开连接
        # self.close()

    def xx_oo(self, event):
        text =  event["message"]['text']
        self.send(text)

    def websocket_disconnect(self, message):
        # 断开连接
        
        print("断开连接")
        async_to_sync(self.channel_layer.group_discard)(self.group, self.channel_name)
        raise StopConsumer()