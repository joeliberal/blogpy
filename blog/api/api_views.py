from rest_framework.views import APIView
from blog.models import Article
from rest_framework.response import Response
from rest_framework import status
from .serializers import SingleArticleSerializer,SubmitAricleSerializer,UpdateArticleSerializers,DeleteArticleSerializers


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
                    'author':article.author.user.first_name + ' ' + article.author.user.last_name,
                    'promote':article.promote,
                })
            return Response({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SingleArticleView(APIView):
    def get(self, request, format=None):
        try:
            article_title = request.GET['article_title']
            article = Article.objects.filter(title__contains = article_title)
            ser = SingleArticleSerializer(article, many = True)
            data = ser.data
            return Response({'data':data}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SearchArticleView(APIView):
    def get(self, request, format=None):
        try:
            from django.db.models import Q
            query = request.GET['query']
            articles = Article.objects.filter(Q(content__icontains=query))
            data = []
            for article in articles:
                data.append({
                    'title':article.title,
                    'cover':article.cover.url if article.cover else None,
                    'content':article.content,
                    'create_at':article.creste_at,
                    'category':article.category.title,
                    'author':article.author.user.first_name + ' ' + article.author.user.last_name,
                    'promote':article.promote,
                })
            return Response({'data':data},status=status.HTTP_200_OK)
        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubmitAricleView(APIView):
    def post(self, request, format=None):
        try:
            ser = SubmitAricleSerializer(data=request.data)
            if ser._valid():
                title = ser.data.get('title')
                cover = request.FILES['cover']
                content = ser.data.get('content')
                category_id = ser.data.get('category_id')
                author_id = ser.data.get('author_id')
                promote = ser.data.get('promote')
            else:
                return Response({'status':'Bad request ...', status=status.HTTP_200_OK})
        
            user = User.objects.get(id=author_id)
            author = UserProfile.objects.get(user=user)
            category = Category.objects.get(id=category_id)
            
            article = Article()
            article.title = title
            article.cover = cover
            article.content = content
            article.category = category 
            article.author = author
            article.promote = promote
            article.save()

            return Response('status':'OK', status = status.HTTP_200_OK)

        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UpadateArticleView(APIView):
    def post(self, request, format=None):
        try:
            ser = UpdateArticleSerializers(data=request.data)
            if ser.is_valid():
                article_id = ser.data.get('article_id')
                cover = request.FILES['cover']
            else: 
                return Response({'status':'Bad request'},status=status.HTTP_400_BAD_REQUEST)
            Article.objects.filter(id=article_id).update(cover=cover)
            return Response({'status':'OK'}, status=status.HTTP_200_OK)
        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteArticleVew(APIView):
    def post(self,request,format=None):
        try:
            ser = DeleteArticleSerializers(request.data)
            if ser.is_valid():
                article_id = ser.data.get('aritcle_id')
            else:
                return Response({'status':'Bad request'},status=status.HTTP_400_BAD_REQUEST)

            Article.objects.filter(id=article_id).delete()
            return Response({'status':'OK'}, status=status.HTTP_200_OK)
        
        except:
            return Response({'status': 'server error .....'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
