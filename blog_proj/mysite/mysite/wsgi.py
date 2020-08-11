"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/django_blog_demo/blog_proj/mysite/mysite/')
load_dotenv(os.path.join(project_folder,'.env'))

#
## assuming your django settings file is at '/home/bradleydb/mysite/mysite/settings.py'
## and your manage.py is is at '/home/bradleydb/mysite/manage.py'
path = '/home/bradleydb/django_blog_demo/blog_proj/mysite/'
if path not in sys.path:
    sys.path.append(path)

os.chdir(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE","mysite.settings")
#
#os.environ['DJANGO_SETTINGS_MODULE'] = 'LVL4.settings'
#
## then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
