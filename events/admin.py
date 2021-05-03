from django.contrib import admin
from .models import Event
# Register your models here.

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug','date']
