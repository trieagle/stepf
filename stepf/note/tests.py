"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from stepf.account.models import Account
from stepf.task.models import Task
from stepf.note.models import Note
from django.contrib.auth.models import User
import json


class SimpleTest(TestCase):
    def setUp(self):
        """
        create a test_user for test
        """
        self.client = Client()
        #use create_user, auto hash password
        usr = User.objects.create_user(username='test', password='test')
        self.test_user = Account.objects.create(user=usr)
        self.assertTrue(self.client.login(username='test', password='test'),
                        'LOGIN FAILED')

    def create_note(self):
    
        note = Note.objects.create(title='Test Note',
                                   owner=self.test_user)
        return note


    def test_view_create_note(self):
        """
        test view function create note
        """
        new_note = json.dumps({'title': 'A NEW NOTE'})
        print new_note
        response = self.client.post('/note/create_note/',
                                    new_note,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response

    def test_view_remove_note(self):
        """
        test view function remove_note
        """
        note = self.create_note()
        rm_note = json.dumps({'id': note.pk})
        print rm_note 
        response = self.client.post('/note/remove_note/',
                                    rm_note,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response 
        self.assertTrue(Note.objects.get(pk=note.pk).alive == 0,
                        "Remove Note Failed")

    def test_view_done_note(self):
        """
        test view function done_note
        """
        note = self.create_note()
        dn_note = json.dumps({'id': note.pk})
        print dn_note
        response = self.client.post('/note/done_note/',
                                    dn_note,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response 
        self.assertTrue(Note.objects.get(pk=note.pk).done == 1,
                        "Done Note Failed")
