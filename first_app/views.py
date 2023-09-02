from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from first_app import models

class IndexVidew(ListView):
    context_object_name = 'musitian_list'
    model = models.Musitian
    template_name = 'first_app/index.html'
  
  
    
class MusitianDetail(DetailView):
    context_object_name = 'musitian'
    model = models.Musitian
    template_name = 'first_app/musitian_detail.html'

  
  
  
  
  
  
  
  
  
  
        






























# from django.http import HttpResponse 
# from first_app.models import Musitian, Album
# from first_app import forms
# from django.db.models import Avg

# def index(request):
#     musitian_list = Musitian.objects.order_by("first_name")

#     diction = {'title': "Home Page", 'musitian_list' : musitian_list}
#     return render(request, 'first_app/index.html', context= diction)



# def album_list(request, artist_id):
#     artist_info = Musitian.objects.get(pk=artist_id)
#     album_list = Album.objects.filter(artist=artist_id).order_by('name')
#     artist_rating = Album.objects.filter(artist = artist_id).aggregate(Avg('num_stars'))
#     diction = {'title': "Music Form", 'artist_info': artist_info, 'album_list': album_list, 'artist_rating': artist_rating}
#     return render(request, 'first_app/album_list.html', context = diction)


# def musitian_form(request):
#     form = forms.MusitianForm() 


#     if request.method == 'POST':
#         form = forms.MusitianForm(request.POST) 

#         if form.is_valid():
#             form.save(commit = True)
#             return index(request)

#     diction = {'title': "Music Form", 'musitian_from': form}
#     return render(request, 'first_app/musitian_form.html', context = diction)

# def album_form(request):
#     form = forms.AlbumForm()
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST)

#         if form.is_valid():
#             form.save(commit=True)
#             return index(request)
        

#     diction = {'title': "Add Album", 'album_form': form}
#     return render(request, 'first_app/album_form.html', context= diction)

# def edit_artist(request, artist_id):
#     artist_info = Musitian.objects.get(pk=artist_id)
#     form = forms.MusitianForm(instance=artist_info)

#     if request.method == 'POST':
#         form = forms.MusitianForm(request.POST,instance=artist_info)

#         if form.is_valid():
#             form.save(commit=True)
#             return album_list(request, artist_id)

#     diction={'edit_form': form}
#     return render(request, 'first_app/edit_artist.html', context= diction)
    
# def edit_album(request, album_id):
#     album_info = Album.objects.get(pk=album_id)
#     form = forms.AlbumForm(instance=album_info)
#     diction={}
#     if request.method == 'POST':
#         form = forms.AlbumForm(request.POST, instance=album_info)

#         if form.is_valid():
#             form.save(commit=True)
#             diction.update({'success_text': "Successfully Updated!"})


#     diction.update({'edit_form': form})
#     diction.update({'album_id': album_id})
#     return render(request, 'first_app/edit_album.html', context=diction)

# def delete_album(request, album_id):
#     album =  Album.objects.get(pk=album_id).delete()
#     diction={'delete_success': 'Album Deleted Successfully!'}
#     return render(request, 'first_app/delete.html', context=diction)


# def delete_musitian(request, artist_id):
#     artist = Musitian.objects.get(pk = artist_id).delete()
#     diction={'delete_success':'Musitian Deleted Successfully!'}
#     return render(request, 'first_app/delete.html', context=diction)