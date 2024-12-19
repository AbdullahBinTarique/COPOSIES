from django.contrib import admin
from .models import AdminUSERS, SubjectDB


class AdAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("fname","lname")}

admin.site.register(AdminUSERS, AdAdmin )
admin.site.register( SubjectDB)