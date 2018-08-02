from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from . import views
from django.contrib.auth import views as auth_views

router = SimpleRouter()
router.register(r'computer', views.ComputerViewSet, base_name='ComputerViewSet')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    ]
