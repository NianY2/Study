from django.urls import re_path
from chat import consumers

websocket_urlpatterns = [
    re_path(r'room', consumers.ChatConsumer),
    # re_path(r'room/(?P<group>\w+)/$', consumers.ChatConsumer),
    re_path(r'wx/chat/(?P<group>\w+)/$', consumers.ChatConsumer),
]