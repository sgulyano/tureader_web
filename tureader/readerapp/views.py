from django.shortcuts import render
from django.http import HttpResponse
from .models import Reader
from . import Templates
from .forms import ItemForm
from django.views.generic import View,ListView
from .utils import render_to_pdf
from django.template.loader import get_template
from .filters import ReaderFilter


def index(request):
    context = dict()
    context['item']= Reader.objects.all()
    return render(request,'readerapp/home.html',context)
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