from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users import views


router = routers.DefaultRouter()
router.register(r'movies', views.MoviesViewSet)
router.register(r'castes', views.CastViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', include(router.urls))
]