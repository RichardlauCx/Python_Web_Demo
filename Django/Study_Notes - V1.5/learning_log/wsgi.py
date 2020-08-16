"""
WSGI config for learning_log project.
Web 服务器网关接口
It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from dj_static import Cling  # 静态附着
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')

application = Cling(get_wsgi_application())
