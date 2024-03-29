from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('blog/<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('blog/search/', views.post_search, name='post_search'),
    path('blog/<int:post_id>/share/', views.post_share, name='post_share'),
]
