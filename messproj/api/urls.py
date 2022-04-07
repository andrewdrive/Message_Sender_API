from django.db import router
from django.urls import path
from rest_framework import routers
from api import views


router = routers.SimpleRouter()
router.register('clients', views.ClientViewSet)


urlpatterns = router.urls
