from django.contrib import admin

# Register your models here.
import authapp.models

admin.site.register(authapp.models.User)
