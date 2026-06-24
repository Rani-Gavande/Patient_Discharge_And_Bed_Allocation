from django.contrib import admin
from .models import add_Patient,add_Doctor

# Register your models here.
admin.site.register(add_Patient)
admin.site.register(add_Doctor)