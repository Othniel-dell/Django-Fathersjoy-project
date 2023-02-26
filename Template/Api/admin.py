from django.contrib import admin



import routeros_api

# Register your models here.
from .models import RouterOS


class RouterOSAdmin(admin.ModelAdmin):
    list_display = ['Name','IP']

    def Queue(self, request):
        connection = routeros_api.RouterOsApiPool('102.69.220.22', username='othniel', password='Pa55w0rd')
        api = connection.get_api()
        
    
admin.site.register(RouterOS/RouterOSAdmin)