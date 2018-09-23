from django.urls import path
from apps.usuario import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'user'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('finder/', views.UsersFinderView.as_view(), name='home'),
    path('jwt/', obtain_jwt_token, name='token')
]