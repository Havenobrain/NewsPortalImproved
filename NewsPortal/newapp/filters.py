import django.forms
from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter, ModelChoiceFilter
from .models import Post, Category


class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postCategory',
        queryset=Category.objects.all(),
        label='Category',
        conjoined=True,
    )
    dateCreation = DateFilter(
        lookup_expr='gt',
        widget=django.forms.DateInput(attrs={'type': 'date'})
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            }