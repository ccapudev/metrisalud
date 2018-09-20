# -*- coding: utf-8 -*-
from django.urls import path
from apps.analisis_clinicos import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'analisis_clinicos'

urlpatterns = [
    path('', views.AnalisisView.as_view(),
         name='analisis_list'),
    path('nuevo/<int:analisis_id>/', views.NewAnalisisView.as_view(),
         name='nuevo_resultado'),
]