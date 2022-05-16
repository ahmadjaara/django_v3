from django.contrib import admin
from .models import Snack
# Register your models here.

# admin.site.register(Snack)
@admin.register(Snack)
class AdminSnack(admin.ModelAdmin):
    list_display=["title","purchaser","description"]

