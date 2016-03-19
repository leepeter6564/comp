from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views import generic

from .models import Article, Image

def home(request):
    all_articles = Article.objects.all()
    all_images = Image.objects.all()
    context = {'all_images':all_images, 'all_articles':all_articles}
    return render(request, 'content/home.html', context)
    

    
class ArticleView(generic.DetailView):
    model = Article
    template_name = 'content/article.html'
