from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.Index.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.Detail_class.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.Res.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote')
]
