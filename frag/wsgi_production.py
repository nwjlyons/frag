"""
WSGI config for frag project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
import sys
import site

# add virtualenv path
site.addsitedir("/home/nwjlyons/.virtualenvs/frag/lib/python2.7/site-packages")
sys.path = ['/home/nwjlyons/webapps/frag/frag'] + sys.path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frag.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
