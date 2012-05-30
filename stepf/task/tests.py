"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.client import Client
from stepf.account.models import Account
from stepf.task.models import Task
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

    def create_task(self):

        task = Task.objects.create(title='test title',
                                   owner=self.test_user,
                                   nstep=11,
                                   frequence=3)
        return task

    def test_view_creat_task(self):
        """
        test view function create_task
        """

        task_data = json.dumps({'title': 'a task',
                                'nstep': 10,
                                'frequence': 3})
        print task_data
        response = self.client.post('/task/create_task/',
                                    task_data,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response

    def test_view_remove_task(self):
        """
        test view function remove_task
        """

        task = self.create_task()
        rm_task_id = json.dumps({'id': task.pk})
        response = self.client.post('/task/remove_task/',
                                    rm_task_id,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response
        self.assertTrue(Task.objects.get(pk=task.pk).alive == 0,
                        "REMOVE FAILED")

    def test_view_update_step_forward(self):
        """
        test view function update_step with arg 1
        """
        task = self.create_task()
        stp_task = json.dumps({'id': task.pk,
                               'step': 1})
        old_step = task.curr_step
        response = self.client.post('/task/update_step/',
                                    stp_task,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response
        self.assertTrue(Task.objects.get(pk=task.pk).curr_step == old_step + 1,
                        "Step +1 FAILD")

    def test_view_update_step_backward(self):
        """
        test view function update_step with arg -1
        """
        task = self.create_task()
        task.update_step(1)
        task.save()

        stp_task = json.dumps({'id': task.pk,
                               'step': -1})
        old_step = task.curr_step
        response = self.client.post('/task/update_step/',
                                    stp_task,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True)
        print response
        self.assertTrue(Task.objects.get(pk=task.pk).curr_step == old_step - 1,
                        "Step -1 FAILD")

    def test_view_update_title(self):
        """
        test view function update_title
        """
        task = self.create_task()

        req_title = json.dumps({'id': task.pk,
                                'title': 'A NEW TITLE'})

        response = self.client.post('/task/update_title/',
                                    req_title,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True) 

        self.assertTrue(Task.objects.get(pk=task.pk).title == 'A NEW TITLE',
                        "Task Title Doesn't Match!!!")
 
    def test_view_update_message(self):
        """
        test view function update_message
        """
        task = self.create_task()
        task.update_step(1)
        task.save()
        msg = task.message_set.get(step_id=1)

        self.assertTrue(msg.content == "", "Message Init Content Incorrect")

        req_msg = json.dumps({'id': msg.pk,
                              'content': "HELLO WORLD"})

        response = self.client.post('/task/update_message/',
                                    req_msg,
                                    'test/json',
                                    HTTP_X_REQUESTED_WITH='XMLHttpRequest',
                                    follow=True) 
        print response
        self.assertTrue(task.message_set.get(pk=msg.pk).content == "HELLO WORLD",
                        "Message Content Doesn't Match!!!")
