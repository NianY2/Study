# Django REST 框架 构建WebAPI
1. 相关知识
   * django
   * 前后端分离（restful接口规范）
   * FBV(函数型视图函数)与CBV
2. 安装`pip install djangorestframework`
3. APIView
   * `from rest_framework.views import APIView`
   * 继承Django的View
   ```python
   class APIView(View):
      @classmethod
      def as_view(cls, **initkwargs):
         ···
         view = super().as_view(**initkwargs)# 执行父类的 as_view
         ···
         return csrf_exempt(view)# 使返回的视图不受csrf跨域保护
      def dispatch(self, request, *args, **kwargs):
         ···
         # 创建新的request对象
         request = self.initialize_request(request, *args, **kwargs)
         self.request = request
         '''
         "contentType:urlencoded \r\v\r\na=1&b=2" Django request.POST针对的是urlencoded数据
         "contentType:json \r\v\r\n{"a":1,"b":2}" DRF request
         让request获取参数更为方便
         get：request.query_params
         post：request.data
         '''
         #初始化：认证、权限、限流组件三件套
         self.initial(request, *args, **kwargs)
         #分发逻辑
         handler = getattr(self, request.method.lower())
         response = handler(request, *args, **kwargs)
   ```
4. 序列化器-Serializer
6. 视图
7. 认证权限
```python
class A:
   def __init__(self,name):
      self.name = name
   def __getattr__(self,item):
      print("item",item)
      return "属性不存在"
a = A("CY")
print(a.name)#CY
print(a.xxx)# item xxx => 属性不存在
```


```python
DEFAULTS = {
   'DEFAULT_AUTHENTICATION_CLASSES': [
      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication'
   ]
}
api_settings = APISettings(None, DEFAULTS, IMPORT_STRINGS)

class APISettings:
   @property#前往用户全局配置文件找REST_FRAMEWORK
   def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, 'REST_FRAMEWORK', {})
        return self._user_settings

   def __getattr__(self, attr):#在调用没有的属性时执行
         '''
         判断是否含有该属性=>前往用户配置文件找REST_FRAMEWORK=>前往默认字典
         '''
         if attr not in self.defaults:#判断在默认属性中是否存在
            raise AttributeError("Invalid API setting: '%s'" % attr)
         try:
            val = self.user_settings[attr]#前往用户配置文件找REST_FRAMEWORK
         except KeyError:
            val = self.defaults[attr]#否则前往默认字典

class APIView(View):
   '''
   在子类中可以重写authentication_classes,重写后将不再调用用户配置的
   顺序：子类(BookView)=>Django配置文件REST_FRAMEWORK=>默认配置DEFAULTS
   '''
   authentication_classes = api_settings.DEFAULT_AUTHENTICATION_CLASSES#属性不存在时__getattr__
   
   def dispatch(self, request, *args, **kwargs):
      ···
      request = self.initialize_request(request, *args, **kwargs)#初始化新的request
      try:
         self.initial(request, *args, **kwargs)#权限和认证
      ···
   
   def initialize_request(self, request, *args, **kwargs):
         ···
         return Request(
            ···
            authenticators=self.get_authenticators(),
         )
   
   def get_authenticators(self):
        return [auth() for auth in self.authentication_classes]

   def initial(self, request, *args, **kwargs):
      ···
      self.perform_authentication(request)#认证
      self.check_permissions(request)#权限
      self.check_throttles(request)#限流

   def perform_authentication(self, request):#认证
      request.user#新的request

class ForcedAuthentication:
   def authenticate(self, request):
      return (self.force_user, self.force_token)

class Request:
   # 权限认证
   @property
   self.authenticators = authenticators or ()

   def user(self):
      if not hasattr(self, '_user'):
         with wrap_attributeerrors():
               self._authenticate()
      return self._user

   def _authenticate(self):
      '''
      authenticators=>
         'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework.authentication.SessionAuthentication()',
            'rest_framework.authentication.BasicAuthentication()'
         ]
      '''
      for authenticator in self.authenticators:
         try:
               user_auth_tuple = authenticator.authenticate(self)#认证逻辑
         except exceptions.APIException:
               self._not_authenticated()
               raise
         
         if user_auth_tuple is not None: # 认证通过
               self._authenticator = authenticator
               self.user, self.auth = user_auth_tuple# 赋值user
               return

      self._not_authenticated()
#默认认证类BaseAuthentication=>相当于一个接口（基于session完成）
class SessionAuthentication(BaseAuthentication):
    def authenticate(self, request):
         #从django的原生request获取user
         user = getattr(request._request, 'user', None)#没有时返回None

         #为空则返回None
         if not user or not user.is_active:
               return None
         
         self.enforce_csrf(request)

         #返回一个元组 user None
         return (user, None)

    def enforce_csrf(self, request):
        """
        Enforce CSRF validation for session based authentication.
        """
        def dummy_get_response(request):  # pragma: no cover
            return None

        check = CSRFCheck(dummy_get_response)
        # populates request.META['CSRF_COOKIE'], which is used in process_view()
        check.process_request(request)
        reason = check.process_view(request, None, (), {})
        if reason:
            # CSRF failed, bail with explicit error message
            raise exceptions.PermissionDenied('CSRF Failed: %s' % reason)
```