#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from stepf.account.models import Account
import collections;
import datetime
import calendar

def home(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/account/index/')

    account = Account.objects.get(user=request.user) 
    return render_to_response("main/index.html",
                              {"username": account.user.username},
                              context_instance=RequestContext(request))
