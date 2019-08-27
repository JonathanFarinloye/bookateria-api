from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('profile', ProfileView)


urlpatterns = router.urls
