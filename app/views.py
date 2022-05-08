from django.forms import ValidationError
from django.shortcuts import render,redirect
from app.forms import UsersForm
from app.models import Users

def home(request):
    data = {}
    data['db'] = Users.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = UsersForm()
    return render(request, 'form.html', data)

def create(request):
    form = UsersForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    else: 
        
        return redirect('form')
    

def edit(request,pk):
    data = {}
    data['db'] = Users.objects.get(pk=pk)
    data['form'] = UsersForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request,pk):
    data = {}
    data['db'] = Users.objects.get(pk=pk)
    form = UsersForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    else: 
        return redirect('form')

def delete(request,pk):
    db = Users.objects.get(pk=pk)
    db.delete()
    return redirect('home')
