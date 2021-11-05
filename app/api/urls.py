from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from .views import ListOrPostAPIView, GetOrEditAPIView


app_name = 'api'

router = DefaultRouter()
router.register(r'users', ListOrPostAPIView)
router.register(r'users', GetOrEditAPIView)

urlpatterns = [
    path('v1/', include(router.urls))
]
