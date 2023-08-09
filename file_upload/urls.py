from django.urls import path
from . import views

app_name = 'file_upload'
urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload_file, name='upload_file'),
    path("upload/result/", views.upload_result, name='upload_result'),
    path("mybook/", views.mybook_list, name='mybook_list'),
    path("mybook/<int:pk>", views.mybook_detail, name='mybook_detail'),
    path("mybook/<int:pk>/delete", views.mybook_delete, name='mybook_delete'),
]
