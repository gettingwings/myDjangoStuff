from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import Topic, Webpage, AccessRecord

from . import forms

# Create your views here.
# def index(request):
#       return HttpResponse("Hello world")


# def index(request):
#     my_dict = {'insert_me':"Hi views.py!",
#     'name_please':"GettingWings"}
#     return render(request, 'first_app/index.html', context=my_dict)

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)

def form_name_view(request):
    # create obj of the form class
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

    return render(request, 'first_app/myform.html', {'form':form})
