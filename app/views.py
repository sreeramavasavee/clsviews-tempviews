from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
class temp(TemplateView):
    template_name='temp.html'

    def get_context_data(self,**kwargs):
        sfdo=super().get_context_data(**kwargs)
        sfdo['sname']='balavikas'
        sfdo['sfdo']=schoolform
        return sfdo

    def post(self,request):
        sf=schoolform(request.POST)
        if sf.is_valid():
            sf.save()
            return HttpResponse('data inserted')

#from view 
class schoolinsertform(FormView):
    form_class=schoolform
    template_name='schoolinsertform.html'
    def form_valid(self, form) -> HttpResponse:
        form.save()
        return HttpResponse('<center>data inserted....</center>')

