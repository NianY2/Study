> 在url.py中
`urlpatterns = [path('book/', views.BookView.as_view())]`

```python
    @classonlymethod#类方法 
    def as_view(cls, **initkwargs): # 谁调用cls,cls就是谁，类调用就是类本身
        ···
        def view(request, *args, **kwargs):
            # cls->类本身 实例化这个类
            self = cls(**initkwargs)
            #访问时为该对象dispatch()函数的返回值
            return self.dispatch(request, *args, **kwargs)
        #访问时为view()函数的返回值
        return view
    def dispatch(self, request, *args, **kwargs):
            #反射 一个字符串lower()转小写 -> 前往BookView类里找get方法
            handler = getattr(self, request.method.lower())
        return handler(request, *args, **kwargs)#执行 BookView->get()
```