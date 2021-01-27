from rest_framework.views import APIView
from blog.models import Article
from rest_framework.response import Response
from rest_framework import status


class AllArticleApiView(APIView):
    def get(self, request):
        try:
            all_articles = Article.objects.all().order_by('-creste_at')[:10]
            data = []
            for article in all_articles:
                data.append({
                    'title':article.title,
                    'cover':article.cover.url if article.cover else None,
                    'content':article.content,
                    'create_at':article.creste_at,
                    'category':article.category.title,
                    'author':article.author.user.first_name + article.author.user.last_name,
                    'promote':article.promote,
                })
            return Response({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
