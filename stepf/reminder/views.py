#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

from stepf.account.models import Account
from stepf.reminder.models import Reminder

import datetime
import time

_minetype = 'application/javascript, charset=utf8'

def _get_account(user):
    return Account.objects.get(user=user)

def _fetch_reminder_or_ajax_error(requst):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)

def create_reminder(request):
    new_reminder = _fetch_reminder_or_ajax_error(requst)
    strp_time = time.strptime(new_reminder['alarm_time'], "%Y/%m/%d %H:%M")
    inner_time = datetime.datetime.fromtimestamp(time.mktime(strp_time))
    reminder = Reminder.objects.create(
        title=new_reminder['title'],
        owner=_get_account(request.user),
        alarm_time=inner_time)
    respones = serializers.serialize('json', reminder)
    return HttpResponse(respones, _minetype)


def remove_reminder(request):
    rm_reminder = _fetch_reminder_or_ajax_error(request)
    try:
        reminder = Reminder.objects.get(id=rm_reminder['id'])
        #FIXME RACE
        reminder.delete()
    except reminder.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _minetype)

    return HttpResponse(simplejson.dumps(True), _minetype)

def done_reminder(request):
    dn_reminder = _fetch_reminder_or_ajax_error(request)
    try:
        reminder = Reminder.objects.get(id=dn_reminder['id'])
        #FIXME RACE
        reminder.delete()
    except reminder.Doesreminderxist:
        return HttpResponse(simplejson.dumps(False), _minetype)

    return HttpResponse(simplejson.dumps(True), _minetype)
