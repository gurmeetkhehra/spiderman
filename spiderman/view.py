# from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

class SpiderMan(TemplateView):
    template_name = 'home.html'

class PeterParker(TemplateView):
    template_name = 'about.html'

# def spiderman(request):
#     return HttpResponse('With Great Power Comes Great Responsibility')




