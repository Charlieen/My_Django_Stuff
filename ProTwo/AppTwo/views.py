from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict={'help_doc':'This is the help of this site: follow me !'}
    return HttpResponse("<em>This is just index demo</em>")


def help(request):
    my_dict={'help_doc':'This is the help of this site: follow me !'}
    return render(request,'AppTwo/help.html',context=my_dict)

def show(request):
    my_dict= {'show_doc':'This is the show of this site: follow me !'}
    return render(request,'AppTwo/show.html',context = my_dict)