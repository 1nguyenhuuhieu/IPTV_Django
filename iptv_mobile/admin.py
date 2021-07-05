from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Stream)
class StreamAdmin(admin.ModelAdmin):
    pass
@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    pass