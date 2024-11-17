"""book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
# from cbv import views
from sers import views
from drf import views as drf_view
# 注册路由
from rest_framework import routers
router = routers.DefaultRouter()
router.register("api/book",views.BookView,"book")
# router.register("前缀",views.BookView,"book")
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    path('drf/book/', drf_view.BookView.as_view()),
    path('docs/', include_docs_urls(title='临时接口文档')),
    # re_path('def/book/(\d+)', drf_view.BookDetailView.as_view())
    # 序列号器
    # path('sers/book/', views.BookView.as_view()),
    # re_path('sers/book/(\d+)', views.BookDetailView.as_view())
    # re_path('sers/book/(?P<pk>\d+)', views.BookDetailView.as_view())

    # path('sers/book/', views.BookView.as_view({"get":"list", "post":"abb_obj"})),
    # re_path('sers/book/(?P<pk>\d+)', views.BookView.as_view({"get":"get_obj","put":"update_obj","delete":"delete_obj"}))
    
    # path('sers/book/', views.BookView.as_view({"get":"list", "post":"create"})),
    # re_path('sers/book/(?P<pk>\d+)', views.BookView.as_view(
    # {"get":"retrieve","put":"update","delete":"destroy"}))
    # 路由组件
]
urlpatterns += router.urls