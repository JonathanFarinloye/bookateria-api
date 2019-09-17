from rest_framework import routers
from .views import *
from django.urls import path, include

router = routers.DefaultRouter()

router.register('all', UserView)

urlpatterns = [
    path('logout/', LogoutView.as_view())
]
urlpatterns += router.urls
