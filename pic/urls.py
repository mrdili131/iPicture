from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile')
]