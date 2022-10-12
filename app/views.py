from django.shortcuts import render

# Create your views here.
def version5(request):
    return render(request,'bootv5.html')