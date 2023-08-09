from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.account_index, name='index'),
    path('register/', views.SignUpView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(), name='login'),
]
