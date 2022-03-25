from django.shortcuts import render

# Create your views here.
# display and render a template

def main(request):
    return render(request, 'index.html') 