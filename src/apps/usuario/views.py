# -*- coding: utf-8 -*-

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.utils.timezone import utc
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.
@method_decorator(login_required, name='dispatch')
class HomeView(APIView):

	def get(self, request, format='json'):
		p = 0
		return render(request, 'web/index.html', dict(
			p=p
		))


@method_decorator(login_required, name='dispatch')
class HomeView(APIView):

	def get(self, request, format='json'):
		p = 0
		return render(request, 'web/index.html', dict(
			p=p
		))
