from django.contrib import admin
from .models import NewUser
# Register your models here.

@admin.register(NewUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name','password']
