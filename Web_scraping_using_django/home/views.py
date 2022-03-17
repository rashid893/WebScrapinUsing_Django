from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
from .models import Link
from django .http import HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=='POST':
        site=request.POST.get('ss','')
        #site=request.POST['ss']
        print('sssssssssss',site)

        page=requests.get(site)

        soap=BeautifulSoup(page.text,'html.parser')
        link_addres=[]
        for link in soap.find_all('a'):
            link_addres=link.get('href')
            line_text=link.string
            Link.objects.create(address=link_addres,name= line_text)
       # return HttpResponseRedirect('')
        
    data=Link.objects.all()


    return render (request,'index.html',{'data':data})
# def delete(request):
#     Link.objects.all().delete()
#     return render(request,'index.html')