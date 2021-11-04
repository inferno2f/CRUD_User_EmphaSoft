from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import GetOrPostAPI


app_name = 'api'

router = DefaultRouter()
router.register(r'users', GetOrPostAPI)

urlpatterns = [
    path('v1/', include(router.urls))
]
