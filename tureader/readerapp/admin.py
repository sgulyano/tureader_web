from django.contrib import admin
from .models import Reader

class ReaderAdmin (admin.ModelAdmin):
    fields=('rank','phd','firstname','lastname','edu','spc','spc_field','contact','uni','field','tel','email','status','source')
    list_display=('id','rank','phd','firstname','lastname','edu','spc','spc_field','contact','uni','field','tel','email','status','source') 
    #list_editable=('rank','phd','firstname','lastname','edu','spc','spc_field','contact','uni','field','tel','email','status','source')
admin.site.register(Reader,ReaderAdmin)


