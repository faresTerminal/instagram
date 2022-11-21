from django.shortcuts import render
from clone.forms import createForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, JsonResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')

def Get_passworder(request):
   
  
    if request.method == 'POST':
        f = createForm(request.POST or None,)
        if f.is_valid():
            c = f.save(commit = False)
            
          
            c.save()

   
    return HttpResponseRedirect('/')