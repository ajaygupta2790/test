from django.contrib import admin
from .models import *

# Register your models here.
#class InvoiceAdmin(admin.ModelAdmin):


admin.site.register(Invoice)
admin.site.register(Transaction)
