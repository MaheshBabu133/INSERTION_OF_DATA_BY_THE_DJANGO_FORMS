from django import forms
from app.models import *

TO=Topic.objects.all()
d=[]
for a in TO:
    d.append((a.topic_name,str(a.topic_name)))
print(d)


WO=Webpage.objects.all()
d1=[]
for a in WO:
    d1.append((a.name,str(a.name)))
print(d1)


class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)


class WebpageForm(forms.Form):
    #topic_name=forms.CharField(max_length=100)
    topic_name=forms.ChoiceField(choices=d)
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    url=forms.URLField()

class AccessRecordForm(forms.Form):
    #name=forms.CharField(max_length=100)
    name=forms.ChoiceField(choices=d1,widget=forms.RadioSelect)
    author=forms.CharField()
    date=forms.DateField()