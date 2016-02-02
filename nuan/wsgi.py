"""
WSGI config for nuan project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys
from os.path import dirname

path = dirname(dirname(__file__))
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nuan.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
