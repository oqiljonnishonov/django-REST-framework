from django.contrib import admin
from django.urls import path,include
from djangoapp.views import ActorViewSet , MovieViewSet

from rest_framework.routers import DefaultRouter

router= DefaultRouter()
router.register('actors',ActorViewSet)
router.register('movies',MovieViewSet)
urlpatterns=router.urls

# urlpatterns = [
    
#     path('',include(router.urls)),
# ]