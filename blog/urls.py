from django.urls import path
from . import views

urlpatterns = [
    path('postlist', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('',views.index,name='index'),
    path('courses',views.courses,name='courses'),
    path('course/<int:pk>/',views.course_detail,name='course_detail'),
    path('news',views.news,name='news'),
    path('feedback',views.feedback,name='feedback'),
    path('registers/', views.register, name='register'),
    path('course/<int:pk>/students/', views.course_student_list, name='course_student_list'),
    path('course/<int:pk>/register/', views.course_register, name='course_register'),
    path('lookup_registration/', views.lookup_registration, name='lookup_registration'),
]
