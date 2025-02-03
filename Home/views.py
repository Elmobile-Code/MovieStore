from django.shortcuts import render

def index(request):
    template_data = {}
    template_data['title'] = 'Movies Store'
    return render(request, 'Home/index.html', {'template_data': template_data})

