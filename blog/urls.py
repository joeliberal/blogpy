from django.urls import path
from .views import IndexPage

app_name = 'blog'

urlpatterns =[
    path('',IndexPage.as_view()),
]