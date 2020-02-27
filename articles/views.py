from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import Article
from django.urls import reverse_lazy

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    login_url = 'login'
    template_name = 'article_list.html'

class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    login_url = 'login'
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    login_url = 'login'
    fields = ('title', 'body')
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    login_url = 'login'
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin ,CreateView):
    model = Article
    login_url = 'login'
    fields = ('title', 'body')
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)