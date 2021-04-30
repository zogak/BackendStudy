from django.contrib import admin
from .models import stoneUser

# Register your models here.

class StoneUserAdmin(admin.ModelAdmin) :
    list_display = ('username', 'password')

admin.site.register(stoneUser, StoneUserAdmin)