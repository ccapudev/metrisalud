from django.urls import path
from apps.web import views

app_name = 'web'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]