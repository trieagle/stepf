"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from stepf.account.models import Account
from stepf.task.models import Task
from stepf.reminder.models import Reminder
from django.contrib.auth.models import User
import json
import datetime
import time


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

    def create_reminder(self):
        strp_time = time.strptime('2012/6/1 12:12', "%Y/%m/%d %H:%M")
        inner_time = datetime.datetime.fromtimestamp(time.mktime(strp_time))
        reminder = Reminder.objects.create(title='Test Reminder',
                                           owner=self.test_user,
                                           alarm_time=inner_time)
        return reminder


    def test_view_create_reminder(self):
        """
        test view function create reminder
        """
        new_reminder = json.dumps({'title': 'A NEW REMINDER',
                                   'alarm_time': '2012/6/1 12:12'})
        print new_reminder
        response = self.client.post('/reminder/create_reminder/',
                                    new_reminder,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response

    def test_view_remove_reminder(self):
        """
        test view function remove_reminder
        """
        reminder = self.create_reminder()
        rm_reminder = json.dumps({'id': reminder.pk})
        print rm_reminder 
        response = self.client.post('/reminder/remove_reminder/',
                                    rm_reminder,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response 
        self.assertTrue(Reminder.objects.get(pk=reminder.pk).alive == 0,
                        "Remove Reminder Failed")

    def test_view_done_reminder(self):
        """
        test view function done_reminder
        """
        reminder = self.create_reminder()
        dn_reminder = json.dumps({'id': reminder.pk})
        print dn_reminder
        response = self.client.post('/reminder/done_reminder/',
                                    dn_reminder,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response 
        self.assertTrue(Reminder.objects.get(pk=reminder.pk).done == 1,
                        "Done Reminder Failed")


