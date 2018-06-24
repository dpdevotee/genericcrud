"""genericcrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from books import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/$', views.BookListView.as_view(), name='book_list'),
    url(r'^home/$', views.BookListView.as_view(), name='home'),
    url(r'^books/(?P<pk>\d+)/$', views.BookDetailView.as_view(),
        name='book_detail'),
    url(r'^books/(?P<pk>\d+)/update/$', views.BookUpdateView.as_view(),
        name='book_update'),
    url(r'^create/$', views.BookCreateView.as_view(),
        name='book_create'),
    url(r'^books/add_publisher/$',
        views.PublisherCreateView.as_view(), name='add_publisher'),
    url(r'^books/add_author/$',
        views.AuthorCreateView.as_view(), name='add_author'),
    url(r'^add_type/$', views.NetworkDeviceTypeCreateView.as_view(), name='add_type'),
    url(r'^add_category/$', views.NetworkDeviceCategoryCreateView.as_view(),
        name='add_category'),
    url(r'^load_type/$', views.get_type_by_category,
        name='load_types')
]