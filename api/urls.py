from django.urls import include, path, re_path

from rest_framework import routers
from rest_framework.authtoken import views as rfviews
from rest_framework.authtoken.views import obtain_auth_token

from api import views

router = routers.DefaultRouter()
router.register(r'animals', views.AnimalViewSet)
router.register(r'persons', views.PersonViewSet)
router.register(r'adopter-family', views.AdopterFamilyViewSet)
router.register(r'fosters', views.FosterViewSet)


urlpatterns = [
    path('', include((router.urls, 'api'), namespace='api')),
    re_path(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework')),
    re_path(r'^api-token-auth/', obtain_auth_token),
]
