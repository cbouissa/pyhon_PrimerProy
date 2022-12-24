from django.shortcuts import render
from django.http import HttpResponse


from family.models import Family
# Create your views here.


def create_family(request):
    new_family = Family.objects.create(name='Facundo',age = 17, sex='M', smoker=False)
    print(new_family)
    return HttpResponse('Se creo el nuevo familiar')

def list_family(request):   
    all_family = Family.objects.all()
    print(all_family)
    context = {
        'familiares': all_family
    }
    return render(request,'list_family.html',context=context)        
