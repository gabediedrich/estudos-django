from django.shortcuts import render, redirect
from .forms import UserSignUpForm

# Create your views here.

def home(request):
    return(render(request, "usuarios/home.html", content_type='text/html'))

    
def add_user(request):
    form = UserSignUpForm(data=request.POST or None)
    if request.method == 'POST':
        print(form.is_bound)
        print(form.errors.as_data())
        print(form.is_valid())
        for field in form:
            print(field)
        if form.is_valid():
            form.save()
            return redirect('user_home')

    return render(request, "usuarios/add_user.html", {'form': form})