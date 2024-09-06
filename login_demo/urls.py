from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('',views.login_create,name = 'login_create')
]
