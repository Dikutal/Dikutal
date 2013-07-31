#!/usr/bin/env python

import sys
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'dikutal.settings'

import django
from django.contrib.auth.models import User


def import_user(username, password, name, email):
    user = User(username=username,
                password=password,
                first_name=name,
                email=email)
    user.save()

if __name__ == '__main__':
    try:
        import_user(*map(lambda s: s.decode('utf-8'), sys.argv[1:5]))
    except IndexError:
        print '''\
Usage: %s USERNAME PASSWORD NAME EMAIL''' % sys.argv[0]
