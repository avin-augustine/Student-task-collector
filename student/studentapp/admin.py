from django.contrib import admin
from.models import Task,Course,Student,Days

# # Register your models here.

admin.site.register(Course)
admin.site.register(Task)
admin.site.register(Days)


class Students(admin.ModelAdmin):
    list_display=('Name','Course','Days','Task','Image')
admin.site.register(Student,Students)