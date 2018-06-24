from django import forms
from django.forms import widgets
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib.staticfiles.templatetags import staticfiles

from .models import Books, Publisher, Author, NetworkDeviceType, NetworkDeviceCategory


class RelatedFieldWidgetCanAdd(widgets.Select):
    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = list()
        output.append(super(RelatedFieldWidgetCanAdd, self).render(
            name, value, *args, **kwargs))
        output.append(
            u'<a href="%s" id="add_id_%s"><img src="%s" alt="My image"/>Добавить</a>' %
            (self.related_url, name, staticfiles.static('books/img/icon-addlink.svg'))
        )
        return mark_safe(u''.join(output))


class RelatedFieldWidgetCanAddMultiple(widgets.SelectMultiple):
    def __init__(self, related_model, related_url=None, *args, **kw):
        super(RelatedFieldWidgetCanAddMultiple, self).__init__(*args, **kw)

        if not related_url:
            rel_to = related_model
            info = (rel_to._meta.app_label, rel_to._meta.object_name.lower())
            related_url = 'admin:%s_%s_add' % info

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url

    def render(self, name, value, *args, **kwargs):
        self.related_url = reverse(self.related_url)
        output = list()
        output.append(super(RelatedFieldWidgetCanAddMultiple, self).render(
            name, value, *args, **kwargs))
        output.append(
            u'<a href="%s" id="add_id_%s"><img src="%s" alt="My image"/>Добавить</a>' %
            (self.related_url, name, staticfiles.static('books/img/icon-addlink.svg'))
        )
        return mark_safe(u''.join(output))


class BookForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget=RelatedFieldWidgetCanAddMultiple(Author,
                                                related_url='add_author'),
        label='Авторы'
    )
    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all(),
        widget=RelatedFieldWidgetCanAdd(Publisher,
                                        related_url='add_publisher'),
        label='Издательство'
    )
    category = forms.ModelChoiceField(
        queryset=NetworkDeviceCategory.objects.all(),
        widget=RelatedFieldWidgetCanAdd(NetworkDeviceCategory,
                                        related_url='add_category'),
        label='Категория'
    )
    manually_set_type = forms.ModelChoiceField(
        queryset=NetworkDeviceType.objects.none(),
        widget=RelatedFieldWidgetCanAdd(
            NetworkDeviceType,
            related_url='add_type'
        ),
        label='Тип'
    )

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)

        if 'category' in self.data:
            try:
                category = int(self.data.get('category'))
                self.fields['manually_set_type'].queryset = (
                    NetworkDeviceType.objects.filter(category=category))
            except (ValueError, TypeError):
                pass  # invalid input from the client, ignore

    class Meta:
        model = Books
        fields = ('title', 'authors', 'publisher',
                  'category', 'manually_set_type')
