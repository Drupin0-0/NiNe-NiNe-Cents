from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def userprofile_view(request):
    return HttpResponse("<h1>User Profile</h1>")