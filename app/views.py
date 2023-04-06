from django.shortcuts import render
from app.models import *
# Create your views here.
def display_Topic(request):
    LOT=Topic.objects.all()
    d={'topics':LOT}
    return render(request,'display_Topic.html',d)

def display_webpage(request):
    LOW=Webpage.objects.all()
    d={'webpage':LOW}
    return render(request,'display_webpage.html',context=d)

def display_AccessRecord(request):
    LOA=AccessRecord.objects.all()
    d={'AcessRecord':LOA}
    return render(request,'display_AccessRecord.html',context=d)    