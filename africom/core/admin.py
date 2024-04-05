from django.contrib import admin

# Register your models here.
from .models import RequestQuoteContact


@admin.register(RequestQuoteContact)
class RequestQuoteContactAdmin(admin.ModelAdmin):
    list_display = [
        "service",
        "full_name",
        "email",
        "occupation",
        "package",
        "timestamp",
        "closed",
    ]
    list_editable = [
        "closed",
    ]
