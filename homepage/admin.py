from django.contrib import admin

# Register your models here.
from homepage.models import *

admin.site.register(Club)
admin.site.register(Notice)
admin.site.register(Manual)
admin.site.register(Calendar)
admin.site.register(Blog)
admin.site.register(List)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'user_id',
        'user_pw',
        'user_name',
        'user_email',
    )