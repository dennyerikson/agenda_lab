from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):

    FIELDS = [
        'lab',
        'course',
        'name',
        'period',
        'create_date',
        'unidade'  
    ]
    list_display = FIELDS    
    search_fields = FIELDS
    list_filter = FIELDS

class CoursesAdmin(admin.ModelAdmin):
    FIELDS = ['value', 'name']
    list_display = FIELDS    
    search_fields = FIELDS
    list_filter = FIELDS

admin.site.register(Post, PostAdmin)
admin.site.register(Period)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Labs)
