#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers

from stepf.account.models import Account
from stepf.note.models import Note

_mimetype = 'application/javascript, charset=utf8'


def _get_account(user):
    return Account.objects.get(user=user)


def _fetch_note_or_ajax_error(request):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    return simplejson.loads(request.raw_post_data)


def create_note(request):
    new_note = _fetch_note_or_ajax_error(request)
    note = Note.objects.create(
        title=new_note['title'],
        owner=_get_account(request.user))
    respones = serializers.serialize('json', [note])
    return HttpResponse(respones, _mimetype)


def remove_note(request):
    rm_note = _fetch_note_or_ajax_error(request)
    try:
        note = Note.objects.get(id=rm_note['id'])
        #FIXME RACE
        note.delete()
    except note.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)


def done_note(request):
    dn_note = _fetch_note_or_ajax_error(request)
    try:
        note = Note.objects.get(id=dn_note['id'])
        #FIXME RACE
        note.done = 1
        note.save()
    except note.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)
