import csv
import xlsxwriter
import datetime

import datetime
from django.contrib import admin
from django.http import HttpResponse
from .models import Profile, edit_contact1, Contacts, edit_contact2, Dashboard,Legal,Activity,confirmacion,DeclaracionVeracidad
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import PrivacyPolicy, TermsOfUse,ActivityPrivacyPolicy, ActivityTermsOfUse 



def profile_pdf(obj):
    return mark_safe('<a href="{}">ver perfil</a>'.format(
        reverse('usuarios:admin_profile_pdf', args=[obj.id])))
profile_pdf.short_description = 'Perfil de usuario'

 
def export_to_csv(modeladmin, request, queryset): 
    opts = modeladmin.model._meta 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name) 
    writer = csv.writer(response) 
     
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many] 
    # Write a first row with header information 
    writer.writerow([field.verbose_name for field in fields]) 
    # Write data rows 
    for obj in queryset: 
        data_row = [] 
        for field in fields: 
            value = getattr(obj, field.name) 
            if isinstance(value, datetime.datetime): 
                value = value.strftime('%d/%m/%Y') 
            data_row.append(value) 
        writer.writerow(data_row) 
    return response 
export_to_csv.short_description = 'Export to CSV' 


def export_to_excel(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="{}.xlsx"'.format(opts.verbose_name_plural)

    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()

    # Obtener los campos del modelo
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    # Escribir encabezados
    for i, field in enumerate(fields):
        worksheet.write(0, i, field.verbose_name)

    # Escribir datos
    for row_num, obj in enumerate(queryset, start=1):
        for col_num, field in enumerate(fields):
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            worksheet.write(row_num, col_num, str(value))  # Convertir a cadena de texto

    workbook.close()
    return response

export_to_excel.short_description = 'Exportar a Excel'

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', profile_pdf]
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de perfil de usuario"
    verbose_name_plural = "Información de perfil de usuario"

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefono']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de contacto de usuario"
    verbose_name_plural = "Información de contacto de usuario"


@admin.register(Legal)
class LegalAdmin(admin.ModelAdmin):
    list_display = ['user', 'ruc', 'tipo_personeria']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de legal de usuario"
    verbose_name_plural = "Información de legal de usuario"

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['user', 'disciplina_artistica', 'registro_ruac']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de actividad cultural de usuario"
    verbose_name_plural = "Información de actividad cultural legal de usuario"

@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ['titulo']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de bienvenida al usuario"
    verbose_name_plural =  "Información de bienvenida al usuario"

@admin.register(confirmacion)
class confirmacionAdmin(admin.ModelAdmin):
    list_display = ['mensaje_de_despedida']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de bienvenida al usuario"
    verbose_name_plural =  "Información de bienvenida al usuario"

@admin.register(DeclaracionVeracidad)
class DeclaracionVeracidadAdmin(admin.ModelAdmin):
    list_display = ['user', 'acepta_terminos_condiciones']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de bienvenida al usuario"
    verbose_name_plural =  "Información de bienvenida al usuario"



@admin.register(PrivacyPolicy)
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de politicas de privacidad"
    verbose_name_plural =  "Información de politicas de privacidad"


@admin.register(TermsOfUse)
class TermsOfUseAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de terminos de uso"
    verbose_name_plural =  "Información de terminos de uso"


@admin.register(ActivityPrivacyPolicy)
class ActivityPrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de politicas de privacidad"
    verbose_name_plural =  "Información de politicas de privacidad"


@admin.register(ActivityTermsOfUse)
class ActivityTermsOfUseAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de terminos de uso"
    verbose_name_plural =  "Información de terminos de uso"
    