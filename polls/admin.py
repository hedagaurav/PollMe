from django.contrib import admin

from .models import Poll, Choice

# Register your models here.
admin.site.register(Choice)
admin.site.register(Poll)
