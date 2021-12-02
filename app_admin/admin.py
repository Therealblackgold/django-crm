from django.contrib import admin
from .models import Payment
from admin_interface.models import Theme
from django_summernote.models import Attachment

admin.site.unregister(Theme)
admin.site.unregister(Attachment)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('member', 'month', 'date', 'amount')
    search_fields = ['month', 'date']


admin.site.register(Payment, PaymentAdmin)
