from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    # path('',views.department_list,name= 'department_list'),
    path('',views.department_create,name='department_create'),
    path('list',views.department_list,name= 'department_list'),
    path('update/<int:pk>',views.department_edit,name= 'department_edit'),
    path('delete/<int:pk>',views.department_delete,name= 'department_delete'),

]
