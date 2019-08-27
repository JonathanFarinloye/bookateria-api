from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('all', DocumentView)
router.register('categories', TypeView)
router.register('tags', TagView)


urlpatterns = router.urls
