from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers # 序列化器
from rest_framework.response import Response
from .models import Book
#---------------------------一 基于APIView的接口实现-------------------------------------
# 针对模型设计序列化器
# class BookSerializers(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=32,source="titles")#source 数据源
#     price = serializers.IntegerField()
#     pub_date = serializers.DateField()
#     def create(self,validated_data):
#         return Book.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         Book.objects.filter(pk=instance.pk).update(**validated_data)
#         return Book.objects.get(pk=instance.pk)

# class BookSerializers(serializers.ModelSerializer):
#     title = serializers.DateField(source="titles") # 重命名
#     class Meta:
#         model = Book
#         # 过滤 或 选择
#         # fields = "__all__"  # 表示序列化数据库中的所有字段
#         # fields = ["titles","price"]
#         exclude = ["titles"] #过滤



# class BookView(APIView):
#     # 增删改查查
#     def get(self,request):
#         book_list =  Book.objects.all()#queryset[book1,book2,...]
#         # 构建序列化器对象
#         # BookSerializers(instance=序列化,data=反序列化)
#         serializer =  BookSerializers(instance=book_list,many=True)#many(是否有多个序列化对象)
#         '''
#         temp = []
#         for obj in book_list:
#             d = {}
#             d["title"] = obj.title
#             temp.append(d)
#         '''
#         return Response(serializer.data)
    
#     def post(self,request):
#         # print(request.data)
#         # 反序列器
#         # 构建序列化器对象
#         serializer = BookSerializers(data=request.data)#初始化->不进行校验
#         # 校验数据
#         # serializers.is_valid()=>serializers.validated_data or serializers.errors=>bool
#         if serializer.is_valid():# 通过
#             serializer.save()
#             '''
#             def save(self, **kwargs):
#                 if self.instance is not None:
#                     编辑
#                 else:
#                     self.instance = self.create(validated_data)
#             def create(self, validated_data):
#                 raise NotImplementedError('`create()` must be implemented.')
#             '''
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class BookDetailView(APIView):
#     def get(self,request,id):
#         book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=book)
#         return Response(serializer.data)
    
#     def put(self,request,id):
#         updata_book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=updata_book,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             # Book.objects.filter(pk=id).update(**serializer.validated_data)
#             # serializer.instance = Book.objects.get(pk=id)
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self,request,id):
#         return Response(Book.objects.get(pk=id).delete())


#---------------------------二 基于GenericAPIView的接口实现-------------------------------------
# from rest_framework.generics import GenericAPIView
# class BookSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"

# class BookView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

#     def get(self, request):
#         serializer = self.get_serializer(instance=self.get_queryset(),many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class BookDetailView(GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

#     def get(self,request,pk):
#         serializer = self.get_serializer(instance=self.get_object(),many=False)
#         return Response(serializer.data)
    
#     def put(self,request,pk):
#         serializer = BookSerializers(instance=self.get_object(),data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self,request,pk):
#         return Response(self.get_object().delete())

#---------------------------三 基于minin混合类(5个视图控制类)的接口实现-------------------------------------
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,DestroyModelMixin
'''
ListModelMixin
CreateModelMixin
UpdateModelMixin
RetrieveModelMixin
DestroyModelMixin
'''
# class BookSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"

# class BookView(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
    
# class BookDetailView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     def get(self, request,pk):
#         return self.retrieve(request,pk)

#     def put(self, request,pk):
#         return self.update(request,pk)

#     def delete(self, request,pk):
#         return self.destroy(request,pk)
#---------------------------四 基于minin混合类的再封装的接口实现-------------------------------------
# from rest_framework.generics import ListCreateAPIView
# from rest_framework.generics import RetrieveUpdateDestroyAPIView
# class BookSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"

# class BookView(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
    
# class BookDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers

#---------------------------五 基于ViewSet的接口实现-------------------------------------
from rest_framework.viewsets import ViewSet
# class BookSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"
'''
class (ViewSetMixin, views.APIView):
    pass
class ViewSetMixin:
    @classonlymethod
    def as_view(cls, actions=None, **initkwargs):
        def view(request, *args, **kwargs):
            actions:{"get":"get_all", "post":"abb_obj"}
            for method, action in actions.items():
                handler = getattr(self, action)//反射get_all=>handler
                setattr(self, method, handler)//设置函数变量get => get_all
'''

# class BookView(ViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     def get_all(self, request):
#         return Response("get_all")

#     def abb_obj(self, request):
#         return Response("abb_obj")
    
#     def get_obj(self, request,pk):
#         return Response("get_obj")

#     def update_obj(self, request,pk):
#         return Response("put_obj")

#     def delete_obj(self, request,pk):
#         return Response("delete_obj")

#---------------------------六 基于GenericViewSet的接口实现-------------------------------------
from rest_framework.viewsets import GenericViewSet

from rest_framework.viewsets import ModelViewSet#继承上面

class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

from rest_framework.permissions import BasePermission,AllowAny,IsAuthenticated
# class BookView(GenericViewSet,ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin

class BookView():
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class BookView1(BookView,GenericViewSet,ListModelMixin,CreateModelMixin):
    pass
class BookView2(BookView,RetrieveModelMixin,RetrieveModelMixin,RetrieveModelMixin):
    pass


class BookView(GenericViewSet):
    """
    list:
    返回所有图书信息.

    create:
    新建图书.
    """

    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    
