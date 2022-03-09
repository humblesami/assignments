from django.shortcuts import render
from django.views.generic import (
    ListView,
)
from .models import Subject
# Create your views here.


class PostListView(ListView):
    model = Subject
    template_name = 'subjects/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'subjects'
    

