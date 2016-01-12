'''
Created on 12/10/2015

@author: naruto
'''
import principal.models
from datetime import datetime
from django.contrib.auth.models import User
#User.objects.create_user("usuario1", "user@g.com", "usuario1")
User.objects.create_superuser("admin", "admin@g.com", "admin")