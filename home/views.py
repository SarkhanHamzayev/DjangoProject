from django.shortcuts import render,HttpResponse

# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        return render(request,'home.html',{ 'name':'Sarkhan Hamzayev'})
    else:
         return render(request, 'home.html', {'name': 'New USER'})

