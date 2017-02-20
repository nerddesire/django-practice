from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<p>In Index view</p>')
    
def item_detail(request, id):
    retval = int(id) + 1000
    return HttpResponse('<p>In detail view with id number: {0} and retval: {1}</p>'.format(id, retval))