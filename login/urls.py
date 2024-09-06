from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
   path('register_admin/', views.register_admin, name='register_admin'),
   path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
