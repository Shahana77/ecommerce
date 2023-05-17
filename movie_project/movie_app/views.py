from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import moviesForm
from . models import movies

# Create your views here.
def movie(request):
    movie=movies.objects.all()
    return render(request,'movie.html',{'movie_list':movie})

def detail(request,movie_id):
    movie=movies.objects.get(id=movie_id)
    return render(request,'details.html',{'movie':movie})
def add (request):
    if request.method=="POST":
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        movie=movies(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render (request,'add.html')

def update(request,id):
   movie=movies.objects.get(id=id)
   form=moviesForm(request.POST or None,request.FILES,instance=movie)
   if form.is_valid():
       form.save()
       return redirect('/')
   return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=='POST':
        movie=movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')