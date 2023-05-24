from django.urls import path
from . import views

urlpatterns = [
    path('', views.form, name='form'),
    path('modify/', views.modify, name='modify'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit , name='edit'),
    
]
