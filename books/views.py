# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Books, Publisher, Author, NetworkDeviceCategory, NetworkDeviceType
from .forms import BookForm


class BookListView(ListView):
    model = Books


class BookDetailView(DetailView):
    model = Books


class BookCreateView(CreateView):
    model = Books
    # fields = ('title', 'authors', 'publisher')
    form_class = BookForm
    success_url = reverse_lazy('book_list')


class BookUpdateView(UpdateView):
    model = Books
    form_class = BookForm
    # fields = ('title', 'authors', 'publisher')

    def get_success_url(self):
        return reverse_lazy('book_detail', kwargs={'pk': self.kwargs['pk']})


class PublisherCreateView(CreateView):
    model = Publisher
    fields = ('name', 'address')
    success_url = reverse_lazy('book_list')


class AuthorCreateView(CreateView):
    model = Author
    fields = ('first_name', 'last_name')
    success_url = reverse_lazy('book_list')


class NetworkDeviceTypeCreateView(CreateView):
    model = NetworkDeviceType
    fields = ('name', 'category', 'comment')
    success_url = reverse_lazy('book_list')


class NetworkDeviceCategoryCreateView(CreateView):
    model = NetworkDeviceCategory
    fields = ('name', 'comment')
    success_url = reverse_lazy('book_list')


def get_type_by_category(request):
    category = request.GET.get('category')
    types = NetworkDeviceType.objects.filter(category=category)
    return render(request, 'books/types_dropdown.html', {'types': types})
