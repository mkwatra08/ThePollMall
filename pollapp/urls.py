from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),                           # Matches /
    path('<int:question_id>/', views.detail, name='detail'),       # Matches /<question_id>/
    path('<int:question_id>/results/', views.results, name='results'),  # Matches /<question_id>/results/
    path('<int:question_id>/vote/', views.vote, name='vote'),      # Matches /<question_id>/vote/
   
]
