from django.contrib import admin

from Sharer.models import SharedFile


class SharedFileAdmin(admin.ModelAdmin):
    pass


admin.site.register(SharedFile, SharedFileAdmin)
