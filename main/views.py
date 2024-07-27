from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import PostModel
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView




class PostDeleteView(DeleteView):
    model = PostModel
    template_name = 'main/delete.html'
    success_url = '/'



class PostUpdateView(UpdateView):
    model = PostModel
    fields = ['name', 'body', 'image']
    template_name = 'main/create.html'
    success_url = '/'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context






class PostDetailView(DetailView):
    model = PostModel
    template_name = 'main/detail.html'


class PostCreateView(CreateView):
    model = PostModel
    template_name = 'main/create.html'
    fields = ['name', 'body', 'image']
    success_url = '/'



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context




class HomeView(ListView):

    template_name = 'main/home.html'
    paginate_by = 4




    def get_queryset(self):

        search = self.request.GET.get('search', '')
        if search:
            qs = PostModel.objects.filter(name__icontains=search)

        else:
            qs = PostModel.objects.all()

        return qs
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context