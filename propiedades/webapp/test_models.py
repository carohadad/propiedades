#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_models.py
Tests for `models.py` module.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement

from django.test import TestCase

from webapp.models import Preferences
from django.contrib.auth.models import User


import unittest
import nose


class PreferencesTestCase(TestCase):
    """Tests for Preferences class."""

    def test_create_new_preference(self):
        user = User(email='caro@mail.com')
        user.save()

        new_prefernce = Preferences(
            user_id=user.id, max_price=123, min_price=12)

        new_prefernce.save()

        self.assertEqual(len(Preferences.objects.all()), 1)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
