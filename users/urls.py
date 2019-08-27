from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('all', UserView)

urlpatterns = router.urls
