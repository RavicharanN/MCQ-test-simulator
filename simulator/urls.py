from django.conf.urls import url
from django.conf.urls import include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
    url(r'logout/$', views.logout_view, name='logout'),
    url(r'^register/', views.UserRegister.as_view(), name = 'register'),  
    url(r'choose/', views.choose_view, name='choose'),
    url(r'^$', views.first_view, name= 'first_view'),
    url(r'studentregister/', views.StudentRegister, name = 'studentregister'),
    url(r'teacherregister/', views.TeacherRegister, name = 'teacherregister'),
]