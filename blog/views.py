from django.shortcuts import render
from .models import Article, Category, UserProfile
# Create your views here.
from django.views.generic import TemplateView

class IndexPage(TemplateView):

    def get(self, request, **kwargs):
        article_data =[]
        all_articles = Article.objects.all()[:9]
        for article in all_articles:
            article_data.append({
                'title':article.title,
                'cover':article.cover.url,
                'category':article.category.title,
                'create_at':article.creste_at.date(),
            })
             
        promote_data = []
        all_promote_article = Article.objects.filter(promote=True)
        for promote in all_promote_article:
            promote_data.append({
                'catgory':promote.category.title,
                'titlle':promote.title,
                'author':promote.author.user.first_name + promote.author.user.last_name,
                'avatar':promote.author.avatar.url if promote.author.avatar else None,
                'create_at':promote.creste_at.data(),
                'cover':promote.cover.url if promote.cover else None,
            })

        context={
            'promote':promote_data,
            'article_data':article_data,
        }
        return render(request, 'index.html', context)