from django.contrib import admin
from .models import Users
from rest_framework.authtoken.models import Token

admin.site.register(Users)
# admin.site.register(Token)
