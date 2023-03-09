from django.urls import path
from leave_tracker import views

urlpatterns = [
    path('', views.index_view, name='index_view'),
    path('register/', views.register, name='index_view'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
