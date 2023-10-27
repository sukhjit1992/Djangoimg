from django.contrib import admin

# Register your models here.
from .models import member
class MemberAdmin(admin.ModelAdmin):
    pass
admin.site.register(member, MemberAdmin)
