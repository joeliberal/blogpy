from django.urls import path
from .api_views import AllArticleApiView,SingleArticleView,SubmitAricleView,UpdateArticleView

app_name = 'api'

urlpatterns = [
    path('',AllArticleApiView.as_view()),
    path('article/',SingleArticleView.as_view()),
    path('article/search/',SearchArticleView.as_view()),
    path('article/submit/',SubmitAricleView.as_view()),
    path('article/update/',UpdateArticleView.as_view()),
]