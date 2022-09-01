from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, User
from .filters import PostFilter
from .forms import NewsForm, ArticleForm, ProfileUserForm
from django.contrib.auth.mixins import PermissionRequiredMixin


class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 5


class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
    pk_url_kwarg = 'id'


class NewsSearchList(NewsList):
    model = Post
    template_name = 'search.html'
    context_object_name = 'search'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(CreateView, PermissionRequiredMixin):
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)


class NewsEdit(UpdateView, PermissionRequiredMixin):
    form_class = NewsForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post')


class NewsDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')


class ArticleCreate(CreateView, PermissionRequiredMixin):
    form_class = ArticleForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.add_post')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'AR'
        return super().form_valid(form)


class ArticleEdit(UpdateView, PermissionRequiredMixin):
    form_class = ArticleForm
    model = Post
    template_name = 'post_edit.html'
    permission_required = ('news.change_post')


class ArticleDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news_list')


class ProfileUserEdit(LoginRequiredMixin, UpdateView):
    form_class = ProfileUserForm
    model = User
    template_name = 'profile_edit.html'
    success_url = '/'


