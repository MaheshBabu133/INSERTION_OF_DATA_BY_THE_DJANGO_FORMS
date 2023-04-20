from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
from app.models import *




def insert_topic(request):
    TOF=TopicForm()
    d={'TOF':TOF}
    if request.method=='POST':
        TF=TopicForm(request.POST)
        if TF.is_valid():
            tn=TF.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            d1={'topic':Topic.objects.all()}
            return render(request,'display_topic.html',d1)
    return render(request,'insert_topic.html',d)

#insert_webpage

def insert_webpage(request):
    WOF=WebpageForm()
    d={'WOF':WOF}
    if request.method=='POST':
        WF=WebpageForm(request.POST)
        if WF.is_valid():
            tn=WF.cleaned_data['topic_name']
            n=WF.cleaned_data['name']
            e=WF.cleaned_data['email']
            u=WF.cleaned_data['email']
        TO=Topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        WO=Webpage.objects.get_or_create(topic_name=TO,name=n,email=e,url=u)[0]
        WO.save()
        webpage=Webpage.objects.all()
        d={'webpage':webpage}
        return render(request,'display_webpage.html',d)
    return render(request,'insert_webpage.html',d)

def insert_accesccrecord(request):
    AOF=AccessRecordForm()
    d={'AOF':AOF}
    if request.method=='POST':
        AF=AccessRecordForm(request.POST)
        if AF.is_valid():
            n=AF.cleaned_data['name']
            a=AF.cleaned_data['author']
            d=AF.cleaned_data['date']
        WO=Webpage.objects.get_or_create(name=n)[0]
        AO=AccessRecord.objects.get_or_create(name=WO,author=a,date=d)[0]
        AO.save()
        d1={'access':AccessRecord.objects.all()}
        #return HttpResponse(f"{a} data  is inserted")
        return render(request,'display_access.html',d1)
    return render(request,'insert_accesccrecord.html',d)