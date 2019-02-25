from django.contrib import messages


def update_lab(modeladmin, request, queryset):
    lab = request.POST['lab']
    queryset.update(lab=lab)
    modeladmin.message_user(request, ("%d labs atualizados com sucesso") % (queryset.count(),), messages.SUCCESS)

update_lab.short_description = 'Update de Labs'