from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message

class MessageList(ListView):
    model = Message
    ordering = ['-id']     

class MessageDetail(DetailView):
    model = Message

class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content'] 
    success_url = reverse_lazy('msg_list')      