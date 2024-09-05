from django.conf import settings
from . import views
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('',views.campus_create,name = 'campus_create')
]
