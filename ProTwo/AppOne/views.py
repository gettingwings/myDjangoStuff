from django.shortcuts import render
from django.http import HttpResponse
from AppOne.models import User
from AppOne.forms import NewUserForm

# Create your views here.
def index(request):
    # return HttpResponse("Index Page")
    return render(request, 'AppOne/index.html')

def help(request):
    my_dict = {"name":"Dipti", "age": 42}
    return render(request,'AppOne/help.html',context=my_dict)

def users(request):
    user_list = User.objects.order_by('fname')
    user_dict = {'users': user_list}
    return render(request, 'AppOne/users.html', context=user_dict)

def signUp(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FROM INVALID')

    return render(request, 'AppOne/signUp.html', {'form':form})
