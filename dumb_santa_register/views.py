from django.shortcuts import render
from django.shortcuts import redirect
from .forms import dumb_santa_form
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

#def dumb_santa_register(request):
#	form = dumb_santa_form()
#    return render(request, 'dumb_santa_register/dumb_main.html', {})
	
@csrf_exempt
def dumb_santa_register(request):
    if request.method == "POST":
        form = dumb_santa_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dumb_santa_register')
    else:
        form = dumb_santa_form()
    return render(request, 'dumb_santa_register/dumb_main.html', {'form': form})