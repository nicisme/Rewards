from django.contrib import admin
from .models import Glance, Profile, Company

# Register your models here.

admin.site.register(Glance)
admin.site.register(Profile)
admin.site.register(Company)