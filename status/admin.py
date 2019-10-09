from django.contrib import admin

from .forms import StatusForm
from .models import Status


class StatusAdmin(admin.ModelAdmin):
    list_display = ['user','__str__','image']
    form = StatusForm


# Register your models here.
admin.site.register(Status,StatusAdmin)