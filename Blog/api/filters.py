from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    owner = filters.CharFilter(field_name='owner__username')
    title = filters.CharFilter(field_name='title')

    class Meta:
        model = Post
        exclude = ('activ', )
        filter_field = ('owner', 'title')

