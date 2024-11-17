from django.shortcuts import render,HttpResponse
from django.views import View

class BookView(View):
    def dispatch(self, request, *args, **kwargs):
        print("Hello World")
        return  super().dispatch(request, *args, **kwargs)
        # return HttpResponse("dispatch")# 重写 所有访问返回dispatch
        # handler = getattr(self, request.method.lower())
        # return handler(request, *args, **kwargs)#执行 BookView->get()
    def get(self, request):
        return HttpResponse("Get")
    def post(self, request):
        return HttpResponse("Post")
    def put(self, request):
        return HttpResponse("Put")
    def delete(self, request):
        return HttpResponse("Delete")