
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^index/$', views.article_list),
    url(r'^article/(?P<article_id>[0-9]+)$', views.article_detail,name='article_detail'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_article,name='edit_article'),
    url(r'^save/article/$', views.saveArticle,name='save_article'),
]
