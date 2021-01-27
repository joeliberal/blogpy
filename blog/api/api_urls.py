from django.urls import path
from .api_views import AllArticleApiView

app_name = 'api'

urlpatterns = [
    path('',AllArticleApiView.as_view()),
]