# service/users/project/tests/base.py

from flask_testing import TestCase

from project import app, db


class BaseTestCase(TestCase):
   def create_app(self):
       app.config.from_object('project.config.TestingConfig')
       return app

   def setUp(self):
       db.create_all()
       db.session.commit()

   def tearDown(self):
       db.session.remove()
       db.drop_all()

import json
import unittest

from project.tests.base import BaseTestCase


class TestUserService(BaseTestCase):
   """Tests for the Users Service."""

   def test_users(self):
       """Ensure the /ping route behaves correctly."""
       response = self.client.get('/users/ping')
       data = json.loads(response.data.decode())
       self.assertEqual(response.status_code, 200)
       self.assertIn('pong', data['message'])
       self.assertIn('success', data['status'])


if __name__ == '__main__':
   unittest.main()
