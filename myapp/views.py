from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import View
from myapp.models import Movie
from myapp.forms import Movieform, MovieModelForm

class Movielistview(View):
    
    def get(self,request,*args,**kwargs):
        qs=Movie.objects.all()

        return render(request,"Movielist.html",{"data":qs})
    


class MovieCreateView(View):
    def get(self,request,*args,**kwargs):
        #form_instance=MovieForm()

        form_instance=MovieModelForm()
        return render(request,"movie_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        #form_instance=Movieform(request.POST)
        
        form_instance=MovieModelForm(request.POST)

        if form_instance.is_valid():
            # data=form_instance.cleaned_data

        
            # Movie.objects.create(**data)
            
            form_instance.save()

            return redirect("movie-list")
        else:
            return render(request,"movie_add.html",{"form":form_instance})
        
#path("movie/<int:pk>/")
#localhost:8000/movie/2/

class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Movie.objects.get(id=id)
        return render(request,"movie_detail.html",{"data":qs})
    

#remove

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Movie.objects.get(id=id).delete()
        return redirect("movie-list")

#localhost:8000/movies/{id}/change/
#method:get post

class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_object=Movie.objects.get(id=id)
        # dist={
        #     "title":movie_object.title,
        #     "year":movie_object.year,
        #     "run_time":movie_object.run_time,
        #     "language":movie_object.language,
        #     "director":movie_object.director,
        #     "producer":movie_object.producer,
        #     "genre":movie_object.genre
        # }

        # form_instance=Movieform(initial=dist)
        
        form_instance=MovieModelForm(instance=movie_object)

        return render(request,"movie_edit.html",{"form":form_instance})    

    def post(self,request,*args,**kwargs):
        form_instance=Movieform(request.POST)
        id=kwargs.get("pk")
        if form_instance.is_valid():
            data=form_instance.cleaned_data
            Movie.objects.filter(id=id).update(**data)
            return redirect("movie-list")
        else:
            return render(request,"movie_edit.html",{"form":form_instance})
