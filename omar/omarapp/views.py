from django.shortcuts import render
 
def myname_view(request):
    return render(request, "myname.html")
 
def myclasses_view(request):
    return render(request, "myclasses.html")
 
def mylinks_view(request):
    return render(request, "mylinks.html")

# Create your views here.
