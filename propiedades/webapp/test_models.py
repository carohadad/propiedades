#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test_models.py
Tests for `models.py` module.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement

import nose
from django.test import TestCase
from django.contrib.auth.models import User

from models import Preferences


class PreferencesTestCase(TestCase):
    """Tests for Preferences class."""

    def test_create_new_preference(self):
        """ Tests default Preference creation. """
        initial_count = len(Preferences.objects.all())

        user = User(email='caro@mail.com')
        user.save()

        new_prefernce = Preferences(
            user=user, max_price=123, min_price=12)

        new_prefernce.save()

        self.assertEqual(len(Preferences.objects.all()), initial_count + 1)


if __name__ == '__main__':
    nose.run(defaultTest=__name__)
