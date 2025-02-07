from django.contrib import admin
from .models import CustomUser, Child

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_parent')
    list_filter = ('is_parent',)
    search_fields = ('username', 'email')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'birth_date')
    list_filter = ('parent',)
    search_fields = ('name',)