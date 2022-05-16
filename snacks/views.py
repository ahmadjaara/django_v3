from django.urls import reverse
from django.shortcuts import render
from django.views.generic import ListView , DetailView ,DeleteView,UpdateView,CreateView,TemplateView
from .models import Snack
# Create your views here.


class HometView (TemplateView):
    template_name="home.html"
    model =Snack

class SnackListView (ListView):
    template_name="snack_list.html"
    model =Snack
     
class SnackDetailView(DetailView):
    template_name="snack_detail.html"
    model=Snack

class SnackCreateView(CreateView):
    template_name="snack_create.html"
    model=Snack
    fields = ["title", "purchaser", "description"]

class SnackUpdateView(UpdateView):
    template_name="snack_update.html"
    model=Snack
    fields = ["title", "description"]
    
class SnackDeleteView(DeleteView):
    template_name="snack_delete.html"
    model=Snack
    fields = ["title", "purchaser"]
    success_url="/"
