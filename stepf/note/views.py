#coding=utf-8
from django.http import HttpResponse
from django.utils import simplejson
from django.core import serializers
from django.template.loader import render_to_string

from stepf.account.models import Account
from stepf.note.models import Note


_mimetype = 'application/javascript, charset=utf8'

_DEBUG = True

if _DEBUG:
    import pdb
    from stepf.debug_tool import *


def _get_account(user):
    return Account.objects.get(user=user)


def _fetch_note_or_ajax_error(request):
    if not request.is_ajax():
        return HttpResponse('ERROR:NOT AJAX REQUEST')
    if _DEBUG:
        print simplejson.loads(request.raw_post_data)
    return simplejson.loads(request.raw_post_data)


@debug_in_out
def create_note(request):
    new_note = _fetch_note_or_ajax_error(request)
    note = Note.objects.create(
        title=new_note['title'],
        owner=_get_account(request.user))
    #respones = serializers.serialize('json', [note])
    if _DEBUG:
        print note.title
    rendered = render_to_string('main/note/note_item.html',
                                {'anote': note})
    if _DEBUG:
        print rendered
    return HttpResponse(simplejson.dumps(rendered),
                        content_type='application/json')
    #return HttpResponse(respones, _mimetype)

@debug_in_out
def remove_note(request):
    rm_note = _fetch_note_or_ajax_error(request)
    try:
        note = Note.objects.get(id=rm_note['id'])
        #FIXME RACE
        note.delete()
    except Note.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)

@debug_in_out
def done_note(request):
    dn_note = _fetch_note_or_ajax_error(request)
    try:
        note = Note.objects.get(id=dn_note['id'])
        #FIXME RACE
        note.done = 1
        note.save()
    except Note.DoesNotExist:
        return HttpResponse(simplejson.dumps(False), _mimetype)

    return HttpResponse(simplejson.dumps(True), _mimetype)
