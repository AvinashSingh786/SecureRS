from django.contrib import admin
from .models import PDE

# Register your models here.


class PDEAdmin(admin.ModelAdmin):
    list_display = ['user','date', 'machine', 'ip',  'rank', 'filename', 'hash', 'api']
    search_fields = (
        'ip', 'user', 'rank', 'date'
    )


admin.site.register(PDE, PDEAdmin)