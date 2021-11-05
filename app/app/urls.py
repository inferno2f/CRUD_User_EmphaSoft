from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.authtoken import views

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
]

# API Documentation
schema_view = get_schema_view(
   openapi.Info(
      title='User API',
      default_version='v1',
      description='Документация для тестового задания от EmphaSoft',
      contact=openapi.Contact(email='nikitinv91@gmail.com'),
      license=openapi.License(name='BSD License'),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$', 
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), 
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), 
       name='schema-redoc'),
]
