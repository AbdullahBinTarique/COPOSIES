from django.contrib import admin

from Teachers.models import Teacher, Sem1,Sem2,Sem3,Sem4,Sem5,Sem6,Sem7,Sem8
from Teachers.models import Students,Batch, Branch

# Register your models here.
admin.site.register(Teacher )
admin.site.register( Students )
admin.site.register( Branch )
admin.site.register( Batch )
# admin.site.register( Subjects )
admin.site.register( Sem1)
admin.site.register( Sem2)
admin.site.register( Sem3)
admin.site.register( Sem4)
admin.site.register( Sem5)
admin.site.register( Sem6)
admin.site.register( Sem7)
admin.site.register( Sem8)



