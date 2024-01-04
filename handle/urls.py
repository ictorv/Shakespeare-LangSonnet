from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    path('', views.reg,name='reg'),
    # path('create/', views.create,name='create'),
]