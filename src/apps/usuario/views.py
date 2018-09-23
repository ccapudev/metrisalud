# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.utils.timezone import utc
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q


# Create your views here.
@method_decorator(login_required, name='dispatch')
class HomeView(APIView):

    def get(self, request, format='json'):
        p = 0
        return render(request, 'web/index.html', dict(
            p=p
        ))


@method_decorator(login_required, name='dispatch')
class UsersFinderView(APIView):

    def get(self, request, format='json'):
        UserModel = get_user_model()
        kw = request.GET.get('kw') or ''
        users = UserModel.objects.filter(
            Q(username__icontains=kw) |
            Q(first_name__icontains=kw) |
            Q(last_name__icontains=kw) |
            Q(last_name_two__icontains=kw) |
            Q(email__icontains=kw)
        )[:10]

        return Response(dict(
            usuarios=map(lambda u: dict(
                label=u.get_full_name() or u.username,
                value=u.id,
            ), users)
        ))


@method_decorator(login_required, name='dispatch')
class HomeView(APIView):

    def get(self, request, format='json'):
        p = 0
        return render(request, 'web/index.html', dict(
            p=p
        ))
