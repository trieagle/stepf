#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from stepf.account.models import Account
import collections;
import datetime
import calendar

def home(request):
    return HttpResponse('this is in home')
