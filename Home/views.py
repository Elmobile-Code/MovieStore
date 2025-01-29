from django.shortcuts import render

# Create your views here.
def home(request):
    template_data = {"title" : "Movie Store"}
    return render(request, 'Home/home.html', {"template_data": template_data})

def about(request):
    template_data = {"title": "About"}
    return render(request, 'About/about.html', {"template_data": template_data})