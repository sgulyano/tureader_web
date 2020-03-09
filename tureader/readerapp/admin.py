from django.contrib import admin
from .models import Reader, University, AcademicField

@admin.register(Reader)
class ReaderAdmin (admin.ModelAdmin):
    fields=('rank','phd', 'title','firstname','lastname','edu','spc','spc_field','contact','uni','field','tel','email','status','source')
    list_display=('id','rank','phd', 'title','firstname','lastname','edu','spc','contact','uni','field','tel','email','status','source') 
    #list_editable=('rank','phd','firstname','lastname','edu','spc','spc_field','contact','uni','field','tel','email','status','source')
    autocomplete_fields = ['uni', 'spc_field']
    search_fields = ['firstname', 'lastname']


@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display=('name',)
    ordering = ['name']
    search_fields = ['name']

@admin.register(AcademicField)
class AcademicFieldAdmin(admin.ModelAdmin):
    list_display=('code', 'name', 'engname', 'category')
    ordering = ['code']
    search_fields = ['name','code']

