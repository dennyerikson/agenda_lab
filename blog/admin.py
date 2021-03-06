from django.contrib import admin
from .models import *
from django.contrib.admin.helpers import ActionForm
from django import forms
from .actions import update_lab
from django.forms.widgets import Select
from django.contrib.auth.models import User


class AuthUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name','is_staff', 'last_login']
    search_fields = ['username', 'email', 'first_name']
    list_filter = ['is_staff', 'is_active','is_superuser','last_login']

class UpdateLabForm(ActionForm):

    # LABS = Labs.objects.all()
    lab = forms.CharField(required=False)
    # widgets={
    #     'lab':Select(choices=((choice.value, choice.name) for choice in LABS )),
    # }



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
    action_form = UpdateLabForm
    actions = [update_lab]

class CoursesAdmin(admin.ModelAdmin):
    FIELDS = ['value', 'name']
    list_display = FIELDS    
    search_fields = FIELDS
    list_filter = FIELDS


admin.site.unregister(User)
admin.site.register(User, AuthUserAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(Period)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(Labs)
