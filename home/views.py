from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'home/homepage.html')

def asur_view(request):
    return render(request,'pvtg/asur.html')