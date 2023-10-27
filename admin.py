from django.contrib import admin
from .models import member
class MemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(member, memberAdmin)
