from django.contrib import admin
from .models import AdminUSERS, SubjectDB, Corelationdata, CONAMES, COPOAcheiveddata


class AdAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("fname","email")}



admin.site.register(AdminUSERS, AdAdmin )
admin.site.register( SubjectDB)
admin.site.register( Corelationdata)
admin.site.register( CONAMES)
admin.site.register( COPOAcheiveddata)



