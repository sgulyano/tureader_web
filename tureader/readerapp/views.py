from django.shortcuts import render
from django.http import HttpResponse
from .models import Reader
from . import templates
from .forms import ItemForm
from django.views.generic import View,ListView
from .utils import render_to_pdf
from django.template.loader import get_template
from .filters import ReaderFilter
from django.core.paginator import Paginator

def index(request):
    search_term = ''
    if 'search' in request.GET:
        search_term = request.GET['search']
        column=request.GET['column']
        if column =='ชื่อจริง':
            context = Reader.objects.all().filter(firstname__icontains=search_term) 
        elif column =='นามสกุล':
            context = Reader.objects.all().filter(lastname__icontains=search_term) 
        elif column =='มหาวิทยาลัย':
            context = Reader.objects.all().filter(uni__icontains=search_term) 
        elif column =='สาขาวิชา':
            context = Reader.objects.all().filter(field__icontains=search_term) 
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
    return render(request,'readerapp/home.html',{'text':text})


def test (request):
    return render(request,'readerapp/test.html')

def edit(request,pk):
    context = dict()
    item=Reader.objects.get(pk=pk)
    form = ItemForm(instance=item)
    if request.method =='POST':
        form = ItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()  
    context['form'] = form
    return render (request,'readerapp/edit.html',context)

def add_item(request):
    context = dict()
    if request.method=='POST':
        form= ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form= ItemForm()
    context['form']=form

    return render(request,'readerapp/edit.html',context)

def editpage(request):
    context = dict()
    context['item']= Reader.objects.all()
    return render(request,'readerapp/editpage.html',context)
    




class GeneratePDF(View):
    def get(self,request,*agrs,**kwargs):
        template= get_template('readerapp/invioce.html')
        context = dict()
        context['item']= Reader.objects.all()
        html = template.render(context)
        pdf = render_to_pdf('readerapp/invioce.html',context)
        return HttpResponse(pdf,content_type='application/pdf')


class search(ListView):
    model = Reader
    template_name= 'readerapp/filter.html'
   

    def get_context_data(self,**kwargs):
        context = dict()
        context['item']= Reader.objects.all()

        context['filter']=ReaderFilter(self.request.GET,queryset=self.get_queryset())
        return context