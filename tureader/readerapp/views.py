from django.shortcuts import render
from django.http import HttpResponse
from .models import Reader
from . import templates
from .forms import ItemForm
from django.views.generic import View,ListView
from django.template.loader import get_template
from .filters import ReaderFilter
from django.core.paginator import Paginator
import xlwt
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q

text_download=[]
def index(request):
    global text_download
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        column=request.GET['column']
        if column =='ชื่อจริง':
            context = Reader.objects.all().filter(firstname__icontains=search_term) 
        elif column =='นามสกุล':
            context = Reader.objects.all().filter(lastname__icontains=search_term) 
        elif column =='มหาวิทยาลัย':
            context = Reader.objects.all().filter(uni__name__icontains=search_term) 
        elif column =='สาขาวิชา':
            context = Reader.objects.all().filter(field__icontains=search_term)
        elif column =='สาขาวิชาตาม ก.พ.อ.':
            context = Reader.objects.all().filter(Q(spc_field__name__icontains=search_term) | Q(spc_field__code__icontains=search_term)).distinct()
        elif column =='ตำแหน่ง':
            context = Reader.objects.all().filter(rank__icontains=search_term) 
        elif column =='ตำแหน่ง ป.เอก':
            context = Reader.objects.all().filter(phd__icontains=search_term) 
    elif 'search'not in request.GET:        
        context= Reader.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(context,50)
    page = request.GET.get('page')
    text = paginator.get_page(page)
    text_download=text
    return render(request,'readerapp/home.html',{'text':text})







def export_page_xls(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Reader.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ตำแหน่งทางวิชาการ', 'ตำแหน่ง ป.เอก','ชื่อ','สกุล','คุณวุฒิ','ความเชี่ยวชาญ','สถานที่ติดต่อ','มหาวิทยาลัย','สาขาวิชา','โทร.','อีเมล','สถานะ','สาขาวิชาตาม ก.พ.อ.','แหล่งที่มา']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = text_download
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.rank, font_style)
        ws.write(row_num, 1, row.phd, font_style)
        ws.write(row_num, 2, row.firstname, font_style)
        ws.write(row_num, 3, row.lastname, font_style)
        ws.write(row_num, 4, row.edu, font_style)
        ws.write(row_num, 5, row.spc, font_style)
        ws.write(row_num, 6, row.contact, font_style)
        ws.write(row_num, 7, row.uni.name, font_style)
        ws.write(row_num, 8, row.field, font_style)
        ws.write(row_num, 9, row.tel, font_style)
        ws.write(row_num, 10, row.email, font_style)
        ws.write(row_num, 11, row.status, font_style)
        spc = []
        for t in row.spc_field.all():
            spc.append(t.code + " " + t.name)
        ws.write(row_num, 12, ';'.join(spc), font_style)
        ws.write(row_num, 13, row.source, font_style)

    wb.save(response)
    return response

def export_all_xls(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Reader.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Users')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['ตำแหน่งทางวิชาการ', 'ตำแหน่ง ป.เอก','ชื่อ','สกุล','คุณวุฒิ','ความเชี่ยวชาญ','สถานที่ติดต่อ','มหาวิทยาลัย','สาขาวิชา','โทร.','อีเมล','สถานะ','สาขาวิชาตาม ก.พ.อ.','แหล่งที่มา']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Reader.objects.all()
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.rank, font_style)
        ws.write(row_num, 1, row.phd, font_style)
        ws.write(row_num, 2, row.firstname, font_style)
        ws.write(row_num, 3, row.lastname, font_style)
        ws.write(row_num, 4, row.edu, font_style)
        ws.write(row_num, 5, row.spc, font_style)
        ws.write(row_num, 6, row.contact, font_style)
        ws.write(row_num, 7, row.uni.name, font_style)
        ws.write(row_num, 8, row.field, font_style)
        ws.write(row_num, 9, row.tel, font_style)
        ws.write(row_num, 10, row.email, font_style)
        ws.write(row_num, 11, row.status, font_style)
        spc = []
        for t in row.spc_field.all():
            spc.append(t.code + " " + t.name)
        ws.write(row_num, 12, ';'.join(spc), font_style)
        ws.write(row_num, 13, row.source, font_style)

    wb.save(response)
    return response
    



    