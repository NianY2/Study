from django.shortcuts import render,HttpResponse
# from django.views import View
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
# 认证
class MyAuthentication(BasicAuthentication):
    def authenticate(self, request):
        return ("CY",None)

# 权限
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.AllowAny',
    # ]
# from rest_framework.permissions import AllowAny

'''
class AllowAny(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request, view):
        return True
'''
from rest_framework.permissions import BasePermission,AllowAny,IsAuthenticated
# class My_Permission(IsAuthenticated):
#     def has_permission(self, request, view):
#         super().has_permission()
#         return True

class BookView(APIView):
    authentication_classes = [MyAuthentication,]
    # permission_classes = [IsAuthenticated]

    # def dispatch(self, request, *args, **kwargs):
    #     print("Hello World")
    #     return  super().dispatch(request, *args, **kwargs)
    def get(self, request):
        print("user:",request.user)
        print("data",request.query_params)
        return HttpResponse("Get")
    def post(self, request):
        print("data",request.data['1'])
        return HttpResponse("Post")
    def put(self, request):
        return HttpResponse("Put")
    def delete(self, request):
        return HttpResponse("Delete")