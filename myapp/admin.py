from django.contrib import admin
from .models import myapp_db


class MyappDbAdmin(admin.ModelAdmin):
    list_display = ('topics', 'notes', 'time', 'date')  


admin.site.register(myapp_db, MyappDbAdmin)
