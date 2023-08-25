from django.shortcuts import render
from app .models import *

from django.http import HttpResponse

# Create your views here.

def Insert_Topic(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    return HttpResponse('Data is Inserted')
def Insert_Webpage(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter Url: ')
    WO=Webpage.objects.get_or_create(topic_name=to,name=n,url='http://abcd.com')[0]
    WO.save()
    return HttpResponse ('Data Inserted')
def Insert_AccessRecord(request):
    tn=input('Enter topic_name: ')
    to=Topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('Enter name: ')
    u=input('Enter Url: ')
    WO=Webpage.objects.get_or_create(topic_name=to,name=n,url='http://abcd.com')[0]
    WO.save()
    d=input('enter date: ')
    a=input('enter date: ')
    e=input('enter email: ')
    ao=AccessRecord.objects.get_or_create(name=WO,date=d,author='dhoni',email='dhoni@12.com')[0]
    ao.save()
    return HttpResponse('Data Inserted')


