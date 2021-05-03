from django.contrib import admin
from .models import BroswerUsage
# Register your models here.
@admin.register(BroswerUsage)
class BroswerUsageAdmin(admin.ModelAdmin):
    list_display = ['id','name','users']