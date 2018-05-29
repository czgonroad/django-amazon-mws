from django.contrib import admin

from .models import MWSCredentials


@admin.register(MWSCredentials)
class MWSCredentialsAdmin(admin.ModelAdmin):
    list_display = (
        'seller_id',
        'region',
        'user',
    )
