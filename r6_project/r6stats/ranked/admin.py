from django.contrib import admin

# Register your models here.

from .models import Operator,Map

admin.site.register(Operator)
admin.site.register(Map)
