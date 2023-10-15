from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Bug
from django.shortcuts import get_object_or_404, render

# Create your views here.

def bug(request):
    return HttpResponse("Welcome to bug app.")

def register_bug(request):
    if request.method == 'POST':
        bug_des=request.POST['text']
        bug_type=request.POST['bug_type']
        report_date=request.POST['date']
        status=request.POST['status']
        add_bug=Bug(description=bug_des,bug_type=bug_type,report_date=report_date,status=status)
        add_bug.save()
        return redirect(list_bug)
    return render(request, "register_bug.html")

def list_bug(request):
    bug_data = Bug.objects.all().values()
    return render(request, 'list_bug.html', {'bug_data': bug_data})

def view_bug(request,id):
    data = get_object_or_404(Bug,id=id)
    return render(request, "view_bug.html", {"data": data})





