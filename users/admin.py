from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "nickname"]
    search_fields = ["username_istartwith"]
    list_per_page = 10
