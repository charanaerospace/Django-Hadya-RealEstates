from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_mvp', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_filter = ('is_mvp', 'hire_date')
    list_per_page = 25
    readonly_fields = ('hire_date',)

admin.site.register(Realtor, RealtorAdmin)
