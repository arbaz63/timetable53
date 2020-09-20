from django.shortcuts import render
from django.http import response, HttpResponse

# Create your views here.
def getTeacherList(request):
    return render(request, 'scheduler_app/list.html')