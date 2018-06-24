# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from books.models import Books, Author, Publisher


admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Publisher)
