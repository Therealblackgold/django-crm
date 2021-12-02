from django.contrib import admin
from .models import Member, Spouse, Family
from django.contrib.auth.admin import UserAdmin
from .forms import MemberCreationForm


class MemberAdmin(UserAdmin):
    model = Member
    add_form = MemberCreationForm
    fieldsets = (*UserAdmin.fieldsets, ('Exteded Personal info', {
        'fields': (
            'status',
            'package',
            'id_number',
            'phone_number',
            'phone_number_2',
            'address',
            'id_copy',
            'proof_of_address',
            'recieved_by',
            'burial_date',
            'slug',
        )
    }))


class SpouseAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = (
        'first_name',
        'last_name',
        'id_number',
        'created',
        'member',
    )


list_display_links = ['first_name']
search_fields = (
    'first_name',
    'last_name',
    'id_number',
    'email',
    'phone_number',
    'phone_number_2',
    'address',
)
list_per_page = 10

search_field = (
    'member',
    'first_name',
    'last_name',
    'id_number',
    'created',
)


class FamilyAdmin(admin.ModelAdmin):
    exclude = ['slug']
    list_display = (
        'first_name',
        'last_name',
        'id_number',
        'created',
        'member',
    )


list_display_links = ['first_name']
search_fields = (
    'first_name',
    'last_name',
    'id_number',
    'email',
    'phone_number',
    'address',
)
list_per_page = 10

admin.site.register(Member, MemberAdmin)
admin.site.register(Spouse, SpouseAdmin)
admin.site.register(Family, FamilyAdmin)
