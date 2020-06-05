from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from . import forms

# Create your views here.
def index(request):
    my_dict={'help_doc':'This is the help of this site: follow me !'}
    return HttpResponse("<em>This is Users Demo,Please click <a href=\"/users\">User</a>/em>")


def users(request):
    form = forms.FormUser()

    if request.method == 'POST':
        form = forms.FormUser(request.POST)
        if form.is_valid():
            # process form data
            obj = User() #gets new object
            obj.first_name = form.cleaned_data['first_name']
            obj.last_name = form.cleaned_data['last_name']
            obj.email = form.cleaned_data['email']
            #finally save the object in db
            obj.save()
    form = forms.FormUser()
    users_list = User.objects.order_by('first_name')
    data_list = {'users_records':users_list,'form':form}
    return render(request,'AppTwo/users.html',context=data_list)

 