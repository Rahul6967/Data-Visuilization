from django.shortcuts import render

# Create your views here.
def graph(request):
    return render(request,'dashboard.html')

def table(request):
    return render(request,'reports.html')